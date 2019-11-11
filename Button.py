from PyQt5 import QtCore, QtGui, QtWidgets


class Button(QtWidgets.QGraphicsObject):
    clicked = QtCore.pyqtSignal()

    def __init__(self, pixmap, parent=None):
        super(Button, self).__init__(parent)
        self.picture = QtGui.QPixmap(pixmap).scaled(100, 100)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 100, 100)


    def mousePressEvent(self, *args, **kwargs):
        self.clicked.emit()

    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):
        QPainter.drawPixmap(QtCore.QPoint(0, 0), self.picture)
        pen = QtGui.QPen()
        pen.setWidth(10)
        brush = QtGui.QBrush()
        brush.setColor(QtCore.Qt.yellow)
        QPainter.setPen(pen)
        QPainter.setBrush(QtCore.Qt.yellow)
        QPainter.drawArc(0, 0, 100, 100, 16 * 180, 16 * -90)
        # QPainter.drawRect(0, 0, self.boundingRect().width(), 100)
