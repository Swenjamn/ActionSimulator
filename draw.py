import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Simulation globals
# g_maxCycle = 10
# g_characterList = ["The Herta", "Robin", "Aventurine", "Jade"]

# g_characterList = [HSRCharacter("The Herta", 99, 5, 33, 220),
                 # HSRCharacter("Robin", 102, 0, 0, 160),
                 # HSRCharacter("Aventurine", 106, 0, 0, 110),
                 # HSRCharacter("Jade", 103, 0, 0, 140),
                 # ]

# global size settings
g_width=7
g_height=4
g_dpi=100

def draw(maxCycle, characterNameList, cycleCountPerCharacter, energyCyclePerCharacter):

    class MplCanvas(FigureCanvasQTAgg):

        def __init__(self, parent=None, width=g_width, height=g_height, dpi=g_dpi):
            fig = Figure(figsize=(width, height), dpi=dpi)
            self.ax1 = fig.add_subplot(2,1,(1,1))
            self.ax2 = fig.add_subplot(2,1,(2,2))
            super().__init__(fig)


    class MainWindow(QtWidgets.QMainWindow):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Create the maptlotlib FigureCanvas object,
            # which defines a single set of axes as self.axes.
            sc = MplCanvas(self, width=g_width, height=g_height, dpi=g_dpi)
            ax1 = sc.ax1
            ax2 = sc.ax2

            # hide the automatic border although no longer needed for some reason?
            # matplotlib.rcParams['axes.spines.left'] = False
            # matplotlib.rcParams['axes.spines.right'] = False
            # matplotlib.rcParams['axes.spines.top'] = False
            # matplotlib.rcParams['axes.spines.bottom'] = False
            # turn off x and y axis
            ax1.set_axis_off()
            ax1.set_title("Action Count per Cycle")
            ax2.set_axis_off()
            ax2.set_title("Energy at end of Cycle")

            labelc = [f"{i}" for i in range(maxCycle)]
            labelr = [f"{character}" for character in characterNameList]

            cycles = [["" for c in range(maxCycle)] for r in range(len(characterNameList))]
            for i in range(len(cycleCountPerCharacter)):
                for j in range(maxCycle):
                    cycles[i][j] = cycleCountPerCharacter[i][j]


            table1 = ax1.table(
                cellText=cycles,
                rowLabels=labelr,
                colLabels=labelc,
                rowColours=["lightblue"] * 16,
                colColours=["palegreen"] * 16,
                cellColours=[[".95" for c in range(maxCycle)] for r in range(len(characterNameList))],
                cellLoc='center',
                loc='upper left',
            )


            energy = [["" for c in range(maxCycle)] for r in range(len(characterNameList))]
            for i in range(len(energyCyclePerCharacter)):
                for j in range(maxCycle):
                    energy[i][j] = energyCyclePerCharacter[i][j]

            table2 = ax2.table(
                cellText=energy,
                rowLabels=labelr,
                colLabels=labelc,
                rowColours=["lightblue"] * 16,
                colColours=["palegreen"] * 16,
                cellColours=[[".95" for c in range(maxCycle)] for r in range(len(characterNameList))],
                cellLoc='center',
                loc='upper left',
            )
            self.setCentralWidget(sc)

            self.show()


    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()

# test value
# draw(g_maxCycle, g_characterList, [[1]*10,[2]*10,[3]*10,[2]+[4]*9])

