from PyQt5.QtWidgets import QWidget, QGraphicsScene, QApplication, QGraphicsView, QGraphicsPixmapItem
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QObject
from Button import Button
from Gauge import Gauge
import time
import sys


class MyThread(QtCore.QThread):

    my_thread = QtCore.pyqtSignal(int)

    def run(self):
        counter = 0

        while counter < 1000:
            counter += 1

            time.sleep(0.03)

            self.my_thread.emit(counter)




class Computer(QWidget, QObject):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        QObject.__init__(self)

        self.__title = 'BMW'
        self.__icon = 'BMW_icon.png'
        self.__x = 700
        self.__y = 300
        self.__width = 500
        self.__height = 500
        self.__scene = None
        self.__view = None

        self.InitializeGui()

        self.show()

    def InitializeGui(self):
        self.setWindowTitle(self.__title)
        self.setWindowIcon(QtGui.QIcon(self.__icon))
        self.setGeometry(self.__x, self.__y, self.__width, self.__height)

        self.__scene = QGraphicsScene()
        self.__view = QGraphicsView(self.__scene, self)
        self.__view.setFixedSize(self.__width, self.__height)
        self.__view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.__scene.setSceneRect(0, 0, self.__width, self.__height)

        self.__view.setBackgroundBrush(QtGui.QBrush(QtGui.QImage('x.png').scaled(self.__width, self.__height)))


        self.button1 = Button('okienko.png')
        self.button1.clicked.connect(self.DisplayMainMenu)
        #self.__scene.addItem(self.button1)
        self.button2 = Button('okienko.png')
        self.button2.clicked.connect(self.DisplayMainMenu)
       # self.__scene.addItem(self.button2)

        self.gauge = Gauge(0)
        self.__scene.addItem(self.gauge)

        self.button1.setPos(50, 150)
        self.button2.setPos(200, 150)
        self.gauge.setPos(100, 100)

        self.thread = MyThread()
        self.thread.my_thread.connect(self.setGauge)
        self.thread.start()


    def setGauge(self, ang):
        self.gauge.setAngle(ang % 340)
        self.__scene.update()
        print(ang)



    def DisplayMainMenu(self):
        self.__scene.clear()

    def DisplayPinPad(self):
        print('test2')

    def DisplaySettings(self):
        pass

    def DisplayCarInfo(self):
        pass

    def DisplayDriveInfo(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    computer = Computer()
    sys.exit(app.exec())
