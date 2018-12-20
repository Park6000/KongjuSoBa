import requests
from bs4 import BeautifulSoup
import time
"""
import glob
import os
import sys
import winshell
from win32com.client import Dispatch
from pywinauto import findwindows
from pywinauto.win32functions import SetForegroundWindow
"""

class Tool:
    __slots__ = []
    """
    @staticmethod
    def exit_duplicate_program(program):
        try:
            findwindows.find_window(title=program)
        except findwindows.WindowNotFoundError:  # 0개, 불가능
            return
        except findwindows.WindowAmbiguousError:  # 2개 이상
            Tool.activate_program(program)
            return sys.exit()

    @staticmethod
    def activate_program(progaram):
        SetForegroundWindow(findwindows.find_window(title=progaram, found_index=0))
        return
    """

    @staticmethod
    def connected_to_internet(url='http://www.google.com/', timeout=5):
        try:
            _ = requests.get(url, timeout=timeout)
            print('Internet connection available.')
            return True
        except requests.ConnectionError:
            print('No internet connection available.')
            return False

    """
    @staticmethod
    def check_ini_file(file_name='KSB.ini'):
        for file in glob.glob('*.ini'):  # '*'은 모든 값을 의미
            if file == file_name:
                return True
        return False
    """

    @staticmethod
    def read_web_last_id(board):
        start_time = time.time()
        url = 'http://www.kongju.ac.kr/lounge/board.jsp?board=%s&page=0' % board
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        ids = []
        for table in soup.select('tr.table_tr'):
            ids.append(int(table.select("td")[0].text))
        ids.sort(reverse=True)
        print("time: %f" % (time.time() - start_time))
        print(ids, ids[0])
        return ids[0]

    """
    @staticmethod
    def create_startup():
        startup = winshell.startup(common=0)
        path = os.path.join(startup, "KongjuSoBa.lnk")
        target = os.path.dirname(os.path.realpath(__file__)) + "\KongjuSoBa.exe"
        wDir = os.path.dirname(os.path.realpath(__file__))
        icon = os.path.dirname(os.path.realpath(__file__)) + "\KongjuSoBa.exe"

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()
        return

    @staticmethod
    def delete_startup():
        startup = winshell.startup(common=0) + '\KongjuSoBa.lnk'
        os.remove(startup)
        return
    """
