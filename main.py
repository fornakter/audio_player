from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
from PyQt5.QtCore import Qt, QUrl
import os
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.dlg = uic.loadUi("untitled.ui", self)
        self.show()
        self.horizontalSlider.setValue(100)
        self.player = QMediaPlayer()
        self.playButton.clicked.connect(self.play_song)
        self.pauseButton.clicked.connect(self.pause_song)
        self.v_upButton_3.clicked.connect(self.vol_up)
        self.v_downButton_4.clicked.connect(self.vol_down)
        self.horizontalSlider.valueChanged.connect(self.slider_voumle)

    def slider_voumle(self, value):
        self.player.setVolume(value)

    def play_song(self):
        full_path = os.path.join(os.getcwd(), 'test.mp3')
        file_url = QUrl.fromLocalFile(full_path)
        content = QMediaContent(file_url)
        self.player.setMedia(content)
        self.player.play()

    def pause_song(self):
        self.player.setMuted(not self.player.isMuted())

    def vol_up(self):
        current_voumle = self.player.volume()
        print(current_voumle)
        self.horizontalSlider.setValue(current_voumle)
        self.player.setVolume(current_voumle + 5)

    def vol_down(self):
        current_voumle = self.player.volume()
        print(current_voumle)
        self.horizontalSlider.setValue(current_voumle)
        self.player.setVolume(current_voumle - 5)

def main():
    app = QApplication([])
    window = MainWindows()
    app.exec_()


if __name__ == '__main__':
    main()
