from KSB_INI import iniTower
import requests
from bs4 import BeautifulSoup
import time


class Board:

    """네이밍 규칙
    1. 함수명: 소문자 사용, '_'로 구분  ex) apple_pie
    2. 클래스내 변수명(init): 시작은 소문자, 대문자로 구분  ex) applePieNum
    3. 함수내 변수명: 소문자 사용, '_'로 구분  ex) apple_pie_num
    """
    __slots__ = ['board', 'loadNum', 'webLastId', 'iniLastId', 'webInfo', 'webInfoNum', 'webInfoLastId']

    def __init__(self, board, load_num):
        self.board = board
        self.loadNum = load_num

        self.webLastId = 0  # 웹상의 마지막 id
        self.iniLastId = 0  # ini의 마지막 id
        self.webInfo = []  # 게시물의 웹 정보 [[id, title, author, created],..]
        self.webInfoNum = 0
        self.webInfoLastId = 0  # 게시물의 웹 정보의 마지막 id

    def update(self):
        start_time = time.time()
        self.webLastId = self.read_web_last_id()
        self.iniLastId = iniTower.read_last_id_of_board(self.board)
        self.create_web_info()
        iniTower.write_last_id_of_board(self.board, self.webInfoNum, self.webInfoLastId)
        print('%s 총 찾은 페이지 수: %d' % (self.board, self.webInfoNum))
        print("%s 총 걸린 시간: %f" % (self.board, time.time() - start_time))
        return

    def search(self, title):
        print(title)
        for article in self.webInfo:
            if article[1] == title:
                return article[0]
        print('항목 없음.')
        return

    def reversed_web_info(self):
        posts = self.webInfo
        posts.sort(reverse=True)
        return posts

    def read_web_last_id(self):
        start_time = time.time()
        url = 'http://www.kongju.ac.kr/lounge/board.jsp?board=%s&page=0' % self.board
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        ids = []
        for table in soup.select('tr.table_tr'):
            ids.append(int(table.select("td")[0].text))
        ids.sort(reverse=True)
        print("1: %f" % (time.time() - start_time))
        print(ids, ids[0])
        return ids[0]

    '''
    def read_web_last_id(self):
        """웹상의 마지막 id를 반환"""
        url = 'http://www.kongju.ac.kr/lounge/board.jsp?page=0&board=%s' % self.board
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')

        ids = str(soup.find_all("td", {"class": "table_td1"}))  # Web page1의 모든 id
        ids = re.sub('<.+?>', '', ids, 0).strip()  # tag 제거
        ids = ids[1:-1].replace(" ", "").split(',')
        ids.sort(reverse=True)
        print(ids)

        return int(ids[0])
    '''
    '''
    def create_web_info(self):
        """
        새로운 게시물을 webInfo에 추가
        webInfoLastId 에 추가된 게시물의 마지막 id 부여
        현재 load_num 활용 부분 지움
        """

        if self.webLastId == self.iniLastId:  # 새로운 게시물 없음
            return

        self.webInfoNum = 0
        max_num = self.webLastId
        id = self.iniLastId + 1

        threads = []
        for i in range(id, max_num + 1):
            thread = threading.Thread(target=self.append_web_info, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        self.webInfo.sort(reverse=False)
        last_idx = self.webInfo[-1][0]

        self.webInfoLastId = last_idx
        print('총 찾은 페이지 수: %d' % self.webInfoNum)
        return

    def append_web_info(self, idx):
        url = 'http://www.kongju.ac.kr/lounge/view.jsp?board=%s&page=0&idx=%d' % (self.board, idx)
        try:
            req = requests.get(url)
        except:
            print("이유불명의 오류")
            return

        html = req.text

        # if html.strip()[:8] == '<script>':  # 페이지의 유효 검사
        #     return

        soup = BeautifulSoup(html, 'lxml')

        try:  # 페이지 유효 검사
            id = soup.select('.content_main_view')[0]
        except IndexError:
            return

        print(idx)

        id = id.select('td')[2].text
        title = soup.select('span.table_tit1')[0].text
        author = soup.select('.content_main_view')[0].select('td')[3].text
        created_date = soup.select('.content_main_view')[0].select('td')[4].text[:10]  # 날짜: yyyy-mm-dd
        # created_time = soup.select('.content_main_view')[0].select('td')[4].text[10:]  # 시간: hh:mm:ss
        # created = created_date + ' ' + created_time

        info = [id, title, author, created_date]
        print(info)
        self.webInfo.append(info)
        self.webInfoNum += 1
        return
        '''

    def create_web_info(self):
        """
        새로운 게시물을 web_info에 추가
        webInfoLastId 에 추가된 게시물의 마지막 id 부여
        현재 load_num 활용 부분 지움
        """
        self.webInfoNum = 0
        if self.webLastId == self.iniLastId:  # 새로운 게시물 없음
            return

        last_id = 0
        page = 0
        stop = False
        while True:
            url = 'http://www.kongju.ac.kr/lounge/board.jsp?board=%s&page=%d' % (self.board, page)

            try:
                req = requests.get(url)
            except:
                return

            html = req.text
            soup = BeautifulSoup(html, 'lxml')

            page_info_num = 0
            for table in soup.select('tr.table_tr'):
                id = int(table.select("td")[0].text)
                title = str(table.select("a")[0]['title'])
                if id > self.iniLastId:
                    print("%s %d" % (self.board, id))
                    self.webInfo.append([id, title])
                    self.webInfoNum += 1
                    if id > last_id:
                        last_id = id
                    page_info_num += 1

            # 1번
                if page != 0 and id <= self.iniLastId:
                    stop = True
                    print("stop!")
                    break

            if stop is True:
                break
            else:
                page += 1

            # 2번
            # if page_info_num == 0:
            #     break
            # else:
            #     print("page up")
            #     page += 1

        self.webInfoLastId = last_id
        return

    # def read_ini_last_id(self):
    #     """ini파일의 마지막 id를 반환"""
    #     last_id = int(self.config.get('LastId', self.board))
    #     return last_id
    #
    # def create_ini_last_id(self):
    #     """ini파일에 불러온 마지막 id를 저장"""
    #     if self.webInfoNum is not 0:
    #         self.config.set('LastId', self.board, str(self.webLastId))
    #         with open('KSB.ini', 'w') as configfile:
    #             self.config.write(configfile)
    #     return