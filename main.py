import datetime
import os
import speech_recognition as sr
import subprocess
import pyttsx3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from funcs.movie import movie
from funcs.Translate import translate
from Ui.root_page import Ui_Root_page

NOTE_STR = ['make a note', 'remember this', 'type this', 'type']
SLEEP_STR = ['sleep']
SHUT_STR = ['shut down']
RESTART_STR = ['restart']
MOVIE_STR = ['search movie', 'movie']
TRANSLATE_STR = ['translate']


class Root(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Root_page()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.ui.set_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))
        self.ui.set_button_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))
        self.ui.set_button_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))
        self.ui.set_button_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))
        self.ui.set_button_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.setting))

        self.ui.rec_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.rec_button.clicked.connect(self.work)
        self.ui.rec_button_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.rec_button_2.clicked.connect(self.work)
        self.ui.rec_button_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.rec_button_3.clicked.connect(self.work)
        self.ui.rec_button_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.rec_button_4.clicked.connect(self.work)
        self.ui.rec_button_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))
        self.ui.rec_button_5.clicked.connect(self.work)

        self.ui.help_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help))
        self.ui.help_button_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help))
        self.ui.help_button_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help))
        self.ui.help_button_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help))
        self.ui.help_button_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.help))

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def speak(self, txt):
        engine = pyttsx3.init()
        engine.say(txt)
        engine.runAndWait()

    def get_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ''

            try:
                said = r.recognize_google(audio)
            except:
                pass
        return said.lower()

    def note(self, txt):
        date = datetime.datetime.now()
        name = str(date).replace(':', '-')
        filename = name[20:] + '-note.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(txt)

        subprocess.Popen(['notepad.exe', filename])

    def work(self):
        self.speak('I am ready')
        text = self.get_audio()
        count = 0

        for phrase in NOTE_STR:
            if phrase in text:
                self.speak('What would you like me to write down?')
                write_down = self.get_audio()
                self.note(write_down)
                self.speak("I've  made a note of that.")
                count += 1

        for phrase in SLEEP_STR:
            if phrase in text:
                self.speak('Are you sure?')
                result = self.get_audio()
                if result == 'yes':
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                else:
                    self.speak('The operation was canceled')
                count += 1

        for phrase in SHUT_STR:
            if phrase in text:
                self.speak('Are you sure?')
                result = self.get_audio()
                if result == 'yes':
                    os.system("shutdown /s /t 1")
                else:
                    self.speak('The operation was canceled')

        for phrase in RESTART_STR:
            if phrase in text:
                self.speak('Are you sure?')
                result = self.get_audio()
                if result == 'yes':
                    os.system("shutdown /r /t 1")
                else:
                    self.speak('The operation was canceled')

        for phrase in MOVIE_STR:
            if phrase in text:
                self.ui.stackedWidget.setCurrentWidget(self.ui.movie)
                self.speak('Say the name of your favorite movie')
                name = self.get_audio()
                movies = movie(name)
                self.ui.n0.setText(name)
                count = 0
                for movie_name in movies:
                    if count == 1:
                        self.ui.lst0.setText(movie_name)
                    elif count == 2:
                        self.ui.lst1.setText(movie_name)
                    elif count == 3:
                        self.ui.lst2.setText(movie_name)
                    elif count == 4:
                        self.ui.lst00.setText(movie_name)
                    elif count == 5:
                        self.ui.lst11.setText(movie_name)
                    elif count == 6:
                        self.ui.lst22.setText(movie_name)
                    elif count == 7:
                        self.ui.lst000.setText(movie_name)
                    elif count == 8:
                        self.ui.lst111.setText(movie_name)
                    elif count == 9:
                        self.ui.lst222.setText(movie_name)
                    elif count == 10:
                        self.ui.lst0000.setText(movie_name)
                    elif count == 11:
                        self.ui.lst1111.setText(movie_name)
                    elif count == 12:
                        self.ui.lst2222.setText(movie_name)
                    count += 1

        for phrase in TRANSLATE_STR:
            if phrase in text:
                self.speak('Say your word')
                word = self.get_audio()
                translated = translate(word)
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
                self.ui.translated.setText(translated)

        # for phrase in PRIVATE1:
            # if phrase != '@am@#':
                # if phrase in text:
                    # pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
