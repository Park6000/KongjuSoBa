from KSB_Tool import Tool
from configparser import ConfigParser


class INITower:
    __slots__ = ['config', 'stayOnTop', 'board', 'loadNum', 'diet',
                 'lastIdOfStudentNews', 'lastIdOfExecutiveNews', 'lastIdOfWorkNews',
                 'lastIdOfHotNews', 'lastIdOfCareer']

    def __init__(self):
        self.config = ConfigParser(allow_no_value=True)
        self.config.read('KSB.ini', encoding='UTF8')

        self.check_first()

        self.stayOnTop = bool(int(self.config.get("SettingValue", "stay_on_top")))
        self.board = self.config.get("SettingValue", "board").replace(' ', '').split(',')
        self.loadNum = int(self.config.get("SettingValue", "load_num"))
        self.diet = self.config.get("SettingValue", "diet")

        self.lastIdOfStudentNews = int(self.config.get("LastId", "student_news"))
        self.lastIdOfExecutiveNews = int(self.config.get("LastId", "executive_news"))
        self.lastIdOfWorkNews = int(self.config.get("LastId", "work_news"))
        self.lastIdOfHotNews = int(self.config.get("LastId", "hot_news"))
        self.lastIdOfCareer = int(self.config.get("LastId", "career"))

    def check_first(self):
        if self.read("SettingValue", "first") is "1":
            self.create_ini_file()

    def create_ini_file(self):
        print('<create ini file>')
        # diet = input('h, b, s')
        # startup = int(input('1: ok, 0:no'))

        f = open('KSB.ini', 'w')
        data = u'[README]\n\n' \
               '[SettingValue]\n' \
               'first = 0\n' \
               'stay_on_top = 0\n' \
               'board = student_news, executive_news, work_news, hot_news, career\n' \
               'load_num = 0\n' \
               'diet = h\n' \
               'startup = 0\n\n' \
               '[LastId]\n' \
               'student_news = %d\n' \
               'executive_news = %d\n' \
               'work_news = %d\n' \
               'hot_news = %d\n' \
               'career = %d\n' \
               % (Tool.read_web_last_id('student_news')-10,
                  Tool.read_web_last_id('executive_news')-10,
                  Tool.read_web_last_id('work_news')-10,
                  Tool.read_web_last_id('hot_news')-10,
                  Tool.read_web_last_id('career')-10)
        f.write(data)
        f.close()

        self.config.read('KSB.ini', encoding='UTF8')
        return

    def read(self, section, option):
        value = self.config.get(section, option)
        return value

    def write(self, section, option, value):
        self.config.set(section, option, value)
        with open('KSB.ini', 'w') as configfile:
            self.config.write(configfile)
        return

    def read_last_id_of_board(self, board):
        """ini 파일의 마지막 id를 반환"""
        if board == "student_news":
            return self.lastIdOfStudentNews
        elif board == "executive_news":
            return self.lastIdOfExecutiveNews
        elif board == "work_news":
            return self.lastIdOfWorkNews
        elif board == "hot_news":
            return self.lastIdOfHotNews
        elif board == "career":
            return self.lastIdOfCareer
        else:
            return

    def write_last_id_of_board(self, board, web_info_num, web_last_id):
        """INITower 객체의 lastIdOf[board] 변수를 업데이트"""
        if web_info_num != 0:
            if board == "student_news":
                self.lastIdOfStudentNews = web_last_id
            elif board == "executive_news":
                self.lastIdOfExecutiveNews = web_last_id
            elif board == "work_news":
                self.lastIdOfWorkNews = web_last_id
            elif board == "hot_news":
                self.lastIdOfHotNews = web_last_id
            elif board == "career":
                self.lastIdOfCareer = web_last_id
            else:
                return

    def write_last_id(self):
        """각각의 보드의 마지막 id를 ini 파일에 작성"""
        self.config.set('README', '; KongjuSoBa 3.1-a')
        self.config.set('README', ';\n; Park Yucheon\n; vgy7bhu9@naver.com')

        self.config.set('SettingValue', '\n; first: Do not modify it!')
        self.config.set('SettingValue', '; stay_on_top: 1_True, 0_False')
        self.config.set('SettingValue', '; board: Do not modify it!')
        self.config.set('SettingValue', '; load_num: Do not modify it!')
        self.config.set('SettingValue', '; diet: h_Hongiksa, b_BTL, s_SinkwanCampus')
        self.config.set('SettingValue', '; startup: Do not modify it!')

        self.config.set("LastId", "student_news", str(self.lastIdOfStudentNews))
        self.config.set("LastId", "executive_news", str(self.lastIdOfExecutiveNews))
        self.config.set("LastId", "work_news", str(self.lastIdOfWorkNews))
        self.config.set("LastId", "hot_news", str(self.lastIdOfHotNews))
        self.config.set("LastId", "career", str(self.lastIdOfCareer))

        with open('KSB.ini', 'w') as configfile:
            self.config.write(configfile)


iniTower = INITower()
