from PyQt5 import QtCore, QtGui, QtWidgets


class Gauge(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, angle):
        super().__init__()
        self.angle = angle

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 100, 100)

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget):
        QPainter.setRenderHint(QtGui.QPainter.Antialiasing)

        gradient = QtGui.QConicalGradient()
        gradient.setCenter(self.x() + self.boundingRect().width() / 2, self.y() + self.boundingRect().height() / 2 + 13)
        gradient.setAngle(180)

        gradient.setColorAt(1, QtGui.QColor(255, 250, 0, 50))
        # gradient.setColorAt(0.5, QtGui.QColor(255, 0, 0, 25))
        gradient.setColorAt(0, QtGui.QColor(255, 250, 0, 50))

        pen = QtGui.QPen(QtGui.QBrush(gradient), 25)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        QPainter.setPen(pen)
        QPainter.drawArc(self.x(), self.y(), 100, 100, 16 * 180, 16 * -self.angle)
        print(16 * - self.angle)

    pass

    def setAngle(self, angle):
        self.angle = angle
