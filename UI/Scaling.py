
import sys
from pprint import pprint as pp
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()
        values = [  '1', '2', '3', 
                    '4', '5', '6',
                    '7', '8', '9'   ]   

        positions = [(r, c) for r in range(3) for c in range(3)]

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)

        for positions, value in zip(positions, values):
            print('Coordinate: ' + str(positions) + ' with value of '+ str(value))
            button = QPushButton(value)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutGrid.addWidget(button, *positions) # widget, position --> row index, column index

def main():
    app = QApplication(sys.argv)
    demo = GridDemo()
    demo.show()
    sys.exit(app.exec_())

main()