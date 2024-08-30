import sys
import matplotlib.colors
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import itertools
from IPython.display import clear_output
import itertools
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QDesktopServices
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt, QUrl

class ScrolLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.label = QLabel(content)
        # self.label.setWordWrap(True)
        # self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # self.image = QPixmap('Text_1.pdf')
        # self.label.setPixmap(self.image)

        # self.label2 = QLabel(content)
        # self.label2.setWordWrap(True)
        # self.label2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # self.image2 = QPixmap('Screenshot from 2024-08-14 08-39-25.png')
        # self.label2.setPixmap(self.image2)

        self.label = QLabel(content)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image = QPixmap('textfiles/p1.pdf')
        self.label.setPixmap(self.image)

        self.label2 = QLabel(content)
        self.label2.setWordWrap(True)
        self.label2.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image2 = QPixmap('textfiles/p2.pdf')
        self.label2.setPixmap(self.image2)

        self.label3 = QLabel(content)
        self.label3.setWordWrap(True)
        self.label3.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image3 = QPixmap('textfiles/p3.pdf')
        self.label3.setPixmap(self.image3)

        self.label4 = QLabel(content)
        self.label4.setWordWrap(True)
        self.label4.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image4 = QPixmap('textfiles/p4.pdf')
        self.label4.setPixmap(self.image4)


        self.label5 = QLabel(content)
        self.label5.setWordWrap(True)
        self.label5.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image5 = QPixmap('textfiles/p5.pdf')
        self.label5.setPixmap(self.image5)

        self.label6 = QLabel(content)
        self.label6.setWordWrap(True)
        self.label6.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image6 = QPixmap('textfiles/p6.pdf')
        self.label6.setPixmap(self.image6)

        self.label7 = QLabel(content)
        self.label7.setWordWrap(True)
        self.label7.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image7 = QPixmap('textfiles/p7.pdf')
        self.label7.setPixmap(self.image7)

        self.label8 = QLabel(content)
        self.label8.setWordWrap(True)
        self.label8.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image8 = QPixmap('textfiles/p8.pdf')
        self.label8.setPixmap(self.image8)
    
        self.label9 = QLabel(content)
        self.label9.setWordWrap(True)
        self.label9.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image9 = QPixmap('textfiles/p9.pdf')
        self.label9.setPixmap(self.image9)

        self.label10 = QLabel(content)
        self.label10.setWordWrap(True)
        self.label10.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.image10 = QPixmap('textfiles/p10.pdf')
        self.label10.setPixmap(self.image10)

        lay.addWidget(self.label)
        lay.addWidget(self.label2)
        lay.addWidget(self.label3)
        lay.addWidget(self.label4)
        lay.addWidget(self.label5)
        lay.addWidget(self.label6)
        lay.addWidget(self.label7)
        lay.addWidget(self.label8)
        lay.addWidget(self.label9)
        lay.addWidget(self.label10)

        

    def setText(self, text):
        self.label.setText(text)


class MainWindow(QMainWindow):

    def link(self, linkStr):

        QDesktopServices.openUrl(QUrl(linkStr))

    def sim_init(self):
        
        self.time = 0
        self.grid_width = int(self.gridslider.value())
        self.features = int(self.featureslider.value())
        self.traits = int(self.traitslider.value())
        self.nearestneighbors = ['4', '8', '12', 'all']
        self.neighbors = self.nearestneighbors[self.neighborslider.value()]
        self.linestyles = {0 : 'solid', 1 : (0, (5, 1)), 2 : 'dashed', 3 : 'dotted', 4 : ''}
        self.gridslidertext.setText(f"Grid size: {self.grid_width}")
        self.featureslidertext.setText(f"Features: {self.features}")
        self.traitslidertext.setText(f"Traits: {self.traits}")
        self.neighborslidertext.setText(f"Neighbors: {self.neighbors}")
        #state = [np.array(i) for i in itertools.product(np.linspace(0, self.traits-1, self.traits, dtype=int), repeat=self.features)]
        #self.state = np.array(state)
        #np.random.shuffle(self.state)
        self.mat = np.random.randint(0, self.traits, (self.grid_width, self.grid_width, self.features))
        self.colormaplist = []
        self.mat2 = np.zeros((self.grid_width, self.grid_width, self.features), dtype= str)
        self.mat3 = np.zeros((self.grid_width, self.grid_width), dtype = int)
        self.dict = {}
        for i in range(self.grid_width):
            for j in range(self.grid_width):
                self.mat2[i, j] = [str(np.base_repr(k, self.traits)) for k in self.mat[i, j]]
                self.mat3[i, j] = int(''.join(self.mat2[i, j]), self.traits)
        for val in np.unique(self.mat3):
            if val not in self.dict.keys():
                self.dict[val] = len(self.dict.keys()) + 1
                self.colormaplist.append([np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1), 1])
        self.cmap = matplotlib.colors.ListedColormap(self.colormaplist)
        for i in range(self.grid_width):
            for j in range(self.grid_width):
                self.mat3[i, j] = self.dict[self.mat3[i, j]]
        # from random import randint
        # colors = []

        # #self.cmap = self.matplotlib.cm.get_cmap('gist_rainbow', len(self.state))
        # self.self.mat2 = np.zeros((self.grid_width, self.grid_width, self.features), dtype= str)
        # self.init = np.zeros((self.grid_width, self.grid_width), dtype = int)
        # for i in range(self.grid_width):
        #     for j in range(self.grid_width):
        #         self.self.mat2[i, j] = [str(k) for k in self.state[i, j]]
        #         self.init[i, j] = int(''.join(self.self.mat2[i, j]), self.features)
        # self.cmap = self.matplotlib.cm.get_cmap('gist_rainbow', self.grid_width**2)
        

    def similarity(self, a, b):
        sim = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                sim += 1
        return (sim/len(a))
    
    def changeLines(self):
        if self.showLines == False:
            self.showLines = True
        else:
            self.showLines = False
    
    def changeBoundary(self):
        self.periodicBoundary = not self.periodicBoundary

    def grid(self):
        if self.showLines == True:
            for i in range(self.grid_width-1):
                for j in range(self.grid_width):
                    self.dyn_ax.plot([j-0.5, j+0.5], [i+0.5, i+0.5],linestyle = self.linestyles[int((self.similarity(self.mat[i, j], self.mat[i + 1, j]) * 4) // 1)], color = 'black')
            for i in range(self.grid_width):
                for j in range(self.grid_width-1):
                    self.dyn_ax.plot([j+0.5, j+0.5], [i-0.5, i+0.5], linestyle = self.linestyles[int((self.similarity(self.mat[i, j], self.mat[i, j + 1]) * 4) // 1)], color = 'black')
            self.dyn_ax.plot([-0.5, self.grid_width-0.5], [-0.5, -0.5], color = 'black')
            self.dyn_ax.plot([-0.5, self.grid_width-0.5], [self.grid_width-0.5, self.grid_width-0.5], color = 'black')
            self.dyn_ax.plot([-0.5, -0.5], [-0.5, self.grid_width-0.5], color = 'black')
            self.dyn_ax.plot([self.grid_width-0.5, self.grid_width-0.5], [-0.5, self.grid_width-0.5], color = 'black')
        else:
            return
        

    def update(self):
        self.time += 1 #/ self.grid_width
        for iter in range(self.grid_width**2):
            self.updategrid()
        for i in range(self.grid_width):
            for j in range(self.grid_width):
                self.mat2[i, j] = [str(np.base_repr(k, self.traits)) for k in self.mat[i, j]]
                self.mat3[i, j] = int(''.join(self.mat2[i, j]), self.traits)
        for val in np.unique(self.mat3):
            if val not in self.dict.keys():
                self.dict[val] = len(self.dict.keys()) + 1
                self.colormaplist.append([np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1), 1])
        self.cmap = matplotlib.colors.ListedColormap(self.colormaplist)
        for i in range(self.grid_width):
            for j in range(self.grid_width):
                self.mat3[i, j] = self.dict[self.mat3[i, j]]
        self.dyn_ax.cla()
        self.matshow = self.dyn_ax.imshow(self.mat3, cmap=self.cmap, vmin = 1, vmax = len(self.dict.keys()))
        self.grid()
        self.dyn_ax.get_yaxis().set_ticks([])
        self.dyn_ax.get_xaxis().set_ticks([])
        self.dyn_ax.set_title(f"t = {int(self.time)}", fontsize = 14)
        self.matshow.figure.canvas.draw()

    def updategrid(self):
        #self.time += 1/self.grid_width**2
        pick = np.random.randint(0, self.grid_width, 2)
        end = self.grid_width - 1
        if self.periodicBoundary == True:
            if self.neighborslider.value() == 0:
                neighbor = [[np.mod(pick[0]-1, end), pick[1]], [np.mod(pick[0]+1, end), pick[1]], [pick[0], np.mod(pick[1]-1, end)], [pick[0], np.mod(pick[1]+1, end)]]
                neighbor = neighbor[np.random.randint(0, 4)]
            elif self.neighborslider.value() == 1:
                neighbor = [[np.mod(pick[0]-1, end), pick[1]], [np.mod(pick[0]+1, end), pick[1]], [pick[0], np.mod(pick[1]-1, end)], [pick[0], np.mod(pick[1]+1, end)], [np.mod(pick[0]-1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]+1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]-1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]+1, end), np.mod(pick[1]+1, end)]]
                neighbor = neighbor[np.random.randint(0, 8)]
            elif self.neighborslider.value() == 2:
                neighbor = [[np.mod(pick[0]-1, end), pick[1]], [np.mod(pick[0]+1, end), pick[1]], [pick[0], np.mod(pick[1]-1, end)], [pick[0], np.mod(pick[1]+1, end)], [np.mod(pick[0]-1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]+1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]-1, end), np.mod(pick[1]-1, end)], [np.mod(pick[0]+1, end), np.mod(pick[1]+1, end)], [np.mod(pick[0] -2, end), pick[1]], [np.mod(pick[0] + 2, end), pick[1]], [pick[0], np.mod(pick[1]-2, end)], [pick[0], np.mod(pick[1]+2, end)]]
                neighbor = neighbor[np.random.randint(0, 12)]
            elif self.neighborslider.value() == 3:
                neighbor = np.random.randint(0, self.grid_width, 2)
                while sum(pick == neighbor) == 2:
                    neighbor = np.random.randint(0, self.grid_width, 2)
        else:
            if self.neighborslider.value() == 0:
                neighbor = [[np.abs(pick[0]-1), pick[1]], [pick[0]+1, pick[1]], [pick[0], np.abs(pick[1]-1)], [pick[0], pick[1]+1]]
                neighbor = neighbor[np.random.randint(0, 4)]
            elif self.neighborslider.value() == 1:
                neighbor = [[np.abs(pick[0]-1), pick[1]], [pick[0]+1, pick[1]], [pick[0], np.abs(pick[1]-1)], [pick[0], pick[1]+1], [np.abs(pick[0]-1), np.abs(pick[1]-1)], [pick[0]+1, np.abs(pick[1]-1)], [np.abs(pick[0]-1), np.abs(pick[1]-1)], [pick[0]+1, pick[1]+1]]
                neighbor = neighbor[np.random.randint(0, 8)]
            elif self.neighborslider.value() == 2:
                neighbor = [[np.abs(pick[0]-1), pick[1]], [pick[0]+1, pick[1]], [pick[0], np.abs(pick[1]-1)], [pick[0], pick[1]+1], [np.abs(pick[0]-1), np.abs(pick[1]-1)], [pick[0]+1, np.abs(pick[1]-1)], [np.abs(pick[0]-1), np.abs(pick[1]-1)], [pick[0]+1, pick[1]+1], [pick[0], pick[1] - 2], [pick[0], pick[1] + 2], [pick[0]-2, pick[1]], [pick[0]+2, pick[1]]]
                neighbor = neighbor[np.random.randint(0, 12)]
            elif self.neighborslider.value() == 3:
                neighbor = np.random.randint(0, self.grid_width, 2)
                while sum(pick == neighbor) == 2:
                    neighbor = np.random.randint(0, self.grid_width, 2)
        if sum(np.array(neighbor) <= np.array([self.grid_width-1, self.grid_width-1])) == 2:
            similarity = np.sum(np.where(self.mat[*pick] == self.mat[*neighbor], 1, 0))/self.features
            differences = np.where(self.mat[*pick] != self.mat[*neighbor])[0]
            chance = np.random.uniform(0, 1)
            if chance <= similarity and similarity < 1:
                dummy = np.array(self.mat[*neighbor])
                randdiff = np.random.randint(0, len(differences))
                self.mat[*pick][differences[randdiff]] = dummy[differences[randdiff]]
        else:
            return
        
    def button_click(self):
        if self.button1.text() == 'Pause':
            self.timer.stop()
            # self.timer2.stop()
            self.button1.setText('Continue')
        else:
            self.timer.start()
            #self.timer2.start()
            self.button1.setText('Pause')

    def savenprint(self):
         self.timer.stop()
         self.timer2.stop()
         print(self.init, len(self.state), self.features, self.traits)
         
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet('background-color: rgb(255, 255, 255);') #rgb(247, 235, 232)

        self.layout = QGridLayout(self.central_widget)


        # self.textLabel = QLabel("Axelrod's Dissemination of Culture")
        # self.textLabel.setAlignment(Qt.AlignCenter)
        # self.layout.addWidget(self.textLabel, 0, 0, 1, 5)


        self.gridslider = QSlider(Qt.Horizontal)
        self.gridslider.setMaximum(50)
        self.gridslider.setMinimum(2)
        self.gridslider.setValue(10)
        self.gridslider.valueChanged.connect(self.sim_init)
        self.layout.addWidget(self.gridslider, 0, 0, 1, 1)
        self.gridslidertext = QLabel(f"Grid size: {self.gridslider.value()}")
        self.gridslidertext.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.gridslidertext, 0, 1, 1, 1)
    

        self.featureslider = QSlider(Qt.Horizontal)
        self.featureslider.setMaximum(15)
        self.featureslider.setMinimum(2)
        self.featureslider.setValue(5)
        self.featureslider.valueChanged.connect(self.sim_init)
        self.layout.addWidget(self.featureslider, 1, 0, 1, 1)
        self.featureslidertext = QLabel(f"Features: {self.featureslider.value()}")
        self.featureslidertext.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.featureslidertext, 1, 1, 1, 1)


        self.traitslider = QSlider(Qt.Horizontal)
        self.traitslider.setMaximum(15)
        self.traitslider.setMinimum(2)
        self.traitslider.setValue(3)
        self.traitslider.valueChanged.connect(self.sim_init)
        self.layout.addWidget(self.traitslider, 2, 0, 1, 1)
        self.traitslidertext = QLabel(f"Traits: {self.traitslider.value()}")
        self.traitslidertext.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.traitslidertext, 2, 1, 1, 1)


        self.neighborslider = QSlider(Qt.Horizontal)
        self.neighborslider.setMaximum(3)
        self.neighborslider.setMinimum(0)
        self.neighborslider.setValue(0)
        self.neighborslider.valueChanged.connect(self.sim_init)
        self.layout.addWidget(self.neighborslider, 3, 0, 1, 1)
        self.neighborslidertext = QLabel(f"Neighbors: {self.neighborslider.value()}")
        self.neighborslidertext.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.neighborslidertext, 3, 1, 1, 1)

        self.button1 = QPushButton()
        # self.button1.value = 1
        self.button1.setText("Pause")
        self.button1.clicked.connect(self.button_click)
        self.layout.addWidget(self.button1, 0, 2, 1, 1)


        self.button2 = QPushButton()
        self.button2.setText("Reset")
        self.button2.clicked.connect(self.sim_init)
        self.button2.clicked.connect(self.update)
        self.layout.addWidget(self.button2, 0, 3, 1, 1)

        self.dyn_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout.addWidget(self.dyn_canvas, 4, 0, 3, 3)
        
        self.checkLines = QCheckBox()
        self.showLines = False
        self.checkLines.setText("Show separation lines")
        self.checkLines.stateChanged.connect(self.changeLines)
        self.layout.addWidget(self.checkLines, 2, 2, 1, 2)

        self.checkBoundary = QCheckBox()
        self.periodicBoundary = False
        self.checkBoundary.setText("Periodic Boundary")
        self.checkBoundary.stateChanged.connect(self.changeBoundary)
        self.layout.addWidget(self.checkBoundary, 1, 2, 1, 2)


        self.Link = QLabel('<a href="https://github.com/Lenny-Mueller/ComplexSystemsAxelrod/">Find the code in GitHub!</a>')
        self.Link.setAlignment(Qt.AlignCenter)
        self.Link.linkActivated.connect(self.link)
        self.layout.addWidget(self.Link, 3, 2, 1, 2) 

        self.dyn_canvas.figure.set_facecolor([1, 1, 1])#0.96862745, 0.92156863, 0.90980392

        # self.button3 = QPushButton()
        # self.button3.setText("Stop && Print")
        # self.button3.clicked.connect(self.savenprint)
        # self.layout.addWidget(self.button3)


        self.scrollable = ScrolLabel()
        #self.scrollable.setText(text)
        self.layout.addWidget(self.scrollable, 0, 4, 7, 2)

        

        self.dyn_ax = self.dyn_canvas.figure.subplots()

        self.sim_init()
        self.matshow = self.dyn_ax.imshow(self.mat3, cmap=self.cmap)
        

        self.timer = self.dyn_canvas.new_timer(50)
        #self.timer2 = self.dyn_canvas.new_timer(1)
        self.timer.add_callback(self.update)
        #self.timer2.add_callback(self.updategrid)
        self.timer.start()
        #self.timer2.start()

        self.setWindowTitle('Axelrod\'s Dissemination of Culture')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec_())