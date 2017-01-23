from PyQt5 import (QtWidgets, QtGui, QtCore)
import time, sys, os, datetime

'''Herro! '''

def hourlyrate():
    global activated

    try:
        fee = float(payamt.text())
        button.setText('Pause')
    except ValueError:
        payamt.setText('Must be a Rumber!')
        activated = False
        return

    tstart = time.time()
    pausedelta = 0

    while activated:

        #here we'll time how long it's been in a paused state for, then add that time to the initial start (tstart) time
        if paused:
            pausestart = time.time()
            while paused:
                tnow = time.time()
                pausedelta = tnow - pausestart
                app.processEvents()

        else:
            tstart += pausedelta #adding any recorded pausedelta onto the initial start time
            tnow = time.time()
            elapsed = (tnow - tstart)
            startdelta = datetime.datetime.fromtimestamp(round(tstart))
            nowdelta = datetime.datetime.fromtimestamp(round(tnow))
            displayelapsed = str(nowdelta - startdelta)

            pausedelta = 0 #resetting pausedelta to 0 because it's now been applied now, and isn't needed on 2nd cycle

            if elapsed <= 0.1:
                hourlyrate = 0.0
            else:
                hourlyrate = float(fee) / (elapsed / 3600)
                if hourlyrate == 7.20:
                    os.system('afplay BWOM.mp3')
                hourlyrate = format(hourlyrate, ',.2f')

            display_rate.setText('£' + str(hourlyrate))
            display_time.setText(displayelapsed)
            app.processEvents()
            time.sleep(0.1)

def thebutton():
    global paused
    global activated

    if not activated:
        activated = True
        hourlyrate()

    if activated:
        if paused:
            paused = False
            button.setText('Pause')
        else:
            paused = True
            button.setText('Resume')

'''PROGRAM AND GUI START HERE'''

app = QtWidgets.QApplication(sys.argv)
gui = QtWidgets

# couple of cheeky wae global variables here nai
paused = False
activated = False


#mainframe window ting
mainframe = gui.QWidget()
mainframe.setFixedSize(400, 550)
mainframe.setWindowTitle('Hourry Rate')

#cre8tin widgetz
payamt = gui.QLineEdit()
scooby = QtGui.QPixmap('scooby.png').scaled(224, 400, QtCore.Qt.KeepAspectRatioByExpanding)
scooby_l = gui.QLabel()
scooby_l.setPixmap(scooby)
rate_l = gui.QLabel('Hourry Rate:')
display_rate = gui.QLabel()
time_l = gui.QLabel('Time Erapsed:')
display_time = gui.QLabel()
button = gui.QPushButton('Ret\'s Go!')

grid = gui.QGridLayout()
maingrid = gui.QGridLayout()

#givin functionz
button.clicked.connect(thebutton)

#placin widgetz
grid.addWidget(payamt, 0, 0)
grid.addWidget(scooby_l, 0, 1)
grid.addWidget(rate_l, 1, 0)
grid.addWidget(display_rate, 1, 1)
grid.addWidget(time_l, 2, 0)
grid.addWidget(display_time, 2, 1)

#placin layoutz
maingrid.addLayout(grid, 0, 0)
maingrid.addWidget(button, 1, 0)
mainframe.setLayout(maingrid)

mainframe.show()
sys.exit(app.exec_())
