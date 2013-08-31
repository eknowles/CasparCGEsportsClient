from PyQt4 import QtCore, QtGui


class DigitalClock(QtGui.QLabel):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        #self.setSegmentStyle(QtGui.QLCDNumber.Filled)

        clocktimer = QtCore.QTimer(self)
        clocktimer.timeout.connect(self.showTime)
        clocktimer.start(1000)

        self.showTime()

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.setText(text)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())