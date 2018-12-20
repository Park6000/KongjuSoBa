from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from mainUi import Ui_MainWindow
from KSB_Board import Board
from KSB_Tool import Tool
from KSB_INI import iniTower
import webbrowser
import sys
import threading
import time


class ThreadBoard(QThread):
    # 쓰레드의 커스텀 이벤트
    # 데이터 전달 시 형을 명시해야 함
    threadEvent: pyqtSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.isRun = False

    def activate_refresh_button(self, bool):
        if bool is False:
            self.main.bt_refresh.setEnabled(False)
            self.main.bt_refresh.setIcon(self.main.iconNull)
            self.main.bt_refresh.setText('불러오는 중..')
        elif bool is True:
            self.main.bt_refresh.setEnabled(True)
            self.main.bt_refresh.setText('')
            self.main.bt_refresh.setIcon(self.main.iconRefresh)

    def run(self):  # start()로 시작
        if self.isRun:
            self.activate_refresh_button(False)

            if Tool.connected_to_internet() is False:
                self.activate_refresh_button(True)
                self.isRun = False
                self.threadEvent.emit(0)
                return

            threads = []
            for board in self.main.ob_boards:
                thread = threading.Thread(target=board.update, args=())
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            self.activate_refresh_button(True)
            self.isRun = False
            self.threadEvent.emit(1)
            return


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # True: 항상 위로 설정함, False: 항상 위로 설정 안함
        self.setWindowFlag(Qt.WindowStaysOnTopHint, iniTower.stayOnTop)
        del iniTower.stayOnTop

        self.setupUi(self)

        self.boards = iniTower.board
        del iniTower.board
        self.loadNum = iniTower.loadNum
        del iniTower.loadNum

        self.ob_boards = []
        for board in self.boards:
            self.ob_boards.append(Board(board, self.loadNum))

        self.li_boards = [self.li_student_news, self.li_executive_news,
                          self.li_work_news, self.li_hot_news, self.li_career]


        self.dietCode = iniTower.diet
        del iniTower.diet
        # h: 홍은해, b: BTL, s: 신관캠 (<기술상 보류> c: 천안캠, y: 예산캠)
        self.dietUrl = {'h': 'https://dormi.kongju.ac.kr/main/contents/food.php?mid=39&k=1',
                        'b': 'https://dormi.kongju.ac.kr/main/contents/food.php?mid=40&k=2',
                        's': 'http://www.kongju.ac.kr/service/food_list.jsp'}

        self.tabCurrentIndex = 0

        # 쓰레드 인스턴스 생성
        self.th = ThreadBoard(self)
        self.th.threadEvent.connect(self.append_list)

        self.startTime = 0

    """
    def check_first_time(self):
        first = int(self.ini.read('SettingValue', 'first'))
        if first == 1:  # 첫 구동
            re = ''
            while 1:
                diet = input(re + '원하는 식단을 입력하세요.\n'
                             'h: 홍은해, b: BTL, s: 신관캠\n')
                if diet == 'h' or diet == 'H' or diet == 'b' or diet == 'B' or diet == 's' or diet == 'S':
                    break
                else:
                    re = '잘못된 입력입니다.\n'
                    continue

            re = ''
            while 1:
                startup = input(re + '시작프로그램으로 등록하겠습니까?\n'
                                     '1: 한다. 0: 안한다.\n'
                                     '숫자를 입력하세요\n')
                if startup == '1' or startup == '0':
                    startup = int(startup)
                    break
                else:
                    re = '잘못된 입력입니다.\n'
                    continue

            Tool.create_ini_file(diet, startup)
            return

        else:
            return
    """

    def location_on_the_screen(self):
        ag = QDesktopWidget().availableGeometry()
        widget = self.geometry()
        x = ag.width() - widget.width()
        self.move(x, 0)
        return

    """
    def set(self):
        pass
    """

    def diet(self):
        """식단 페이지를 연다"""
        webbrowser.open(self.dietUrl[self.dietCode])
        return

    """
    def search(self):
        pass
    """

    def refresh(self):
        if not self.th.isRun:
            self.startTime = time.time()
            print('<start refresh>')
            self.th.isRun = True
            self.th.start()
            return

    def append_list(self, internet):
        """각 객체의 웹 정보를 리스트(pyQt)에 넣는다"""
        if internet == 0:  # 인터넷 연결 확인 (ThreadBoard.run의 반환값으로 판단)
            QMessageBox.critical(self, '인터넷 연결 실패',
                                 '인터넷이 연결되지 않았습니다.\n연결 후 다시 시도해주세요.')
            return

        i = 0
        selected_tab = False
        for board in self.ob_boards:
            reversed_web_info = board.reversed_web_info()
            web_info_title = []
            if not reversed_web_info:
                i += 1
                continue
            self.li_boards[i].clear()
            if board.webInfoNum != 0:
                self.tab_main.setTabIcon(int(i), self.iconDot)
            for info in reversed_web_info:
                web_info_title.append(info[1])
            self.li_boards[i].addItems(web_info_title)

            if board.webInfoNum != 0 and selected_tab is False:
                self.tab_main.setCurrentIndex(i)
                self.tabCurrentIndex = i
                self.li_boards[i].setCurrentRow(0)
                self.li_boards[i].setFocus()
                selected_tab = True  # 시작 탭 정해짐
            i += 1

        iniTower.write_last_id()
        print('<finish refresh: %f>' % (time.time() - self.startTime))
        return

    def to_page(self, board_index, title):
        idx = self.ob_boards[board_index].search(title)
        url = 'http://www.kongju.ac.kr/lounge/view.jsp?board=%s&idx=%s' % (self.boards[board_index], idx)
        webbrowser.open(url)
        return

    def to_home(self):
        url = 'http://www.kongju.ac.kr'
        webbrowser.open(url)
        return

    def remove_dot(self):
        self.tab_main.setTabIcon(self.tabCurrentIndex, self.iconNull)
        self.tabCurrentIndex = self.tab_main.currentIndex()
        return

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F5:
            # F5 눌렀을 때, 새로고침
            self.refresh()
            return

        elif event.key() == Qt.Key_Return:
            # 리스트 아이템 항목 선택 되었을 때, 엔터키로 열기
            if self.li_boards[self.tab_main.currentIndex()].currentItem() != None:
                self.to_page(self.tab_main.currentIndex(),
                             self.li_boards[self.tab_main.currentIndex()].currentItem().text())
                return

        elif event.key() == Qt.Key_Right:
            now_index = self.tab_main.currentIndex()
            if now_index == 4:
                now_index = 0
            else:
                now_index += 1
            self.tab_main.setCurrentIndex(now_index)
            return

        elif event.key() == Qt.Key_Left:
            now_index = self.tab_main.currentIndex()
            if now_index == 0:
                now_index = 4
            else:
                now_index -= 1
            self.tab_main.setCurrentIndex(now_index)
            return

        # elif event.key() == Qt.Key_Down:
        #     if self.li_boards[self.tab_main.currentIndex()].currentItem() == None:
        #         print("aaa")
        #         self.li_boards[self.tab_main.currentIndex()].setCurrentIndex(model_index)


# Tool.exit_duplicate_program('KongjuSoBa.exe')  # 이미 실행중인 프로그램이 있다면 현 프로그램 종료
app = QApplication([])
mainWindow = MainWindow()
mainWindow.location_on_the_screen()
mainWindow.show()

mainWindow.refresh()
sys.exit(app.exec_())
