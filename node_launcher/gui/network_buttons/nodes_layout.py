from PySide2 import QtWidgets

from node_launcher.gui.components.layouts import QGridLayout
from node_launcher.gui.horizontal_line import HorizontalLine
from node_launcher.gui.image_label import ImageLabel
from node_launcher.gui.network_buttons.section_name import SectionName
from node_launcher.node_set import NodeSet


class NodesLayout(QGridLayout):
    def __init__(self, node_set: NodeSet):
        super(NodesLayout, self).__init__()
        self.node_set = node_set
        self.columns = 2
        image_label = ImageLabel(f'bitcoin-{self.node_set.network}.png')
        self.addWidget(image_label, row_span=5)

        self.addWidget(SectionName('Nodes'), column=self.columns)
        # Bitcoin-Qt button
        self.bitcoin_qt_button = QtWidgets.QPushButton('Launch Bitcoin')
        # noinspection PyUnresolvedReferences
        self.bitcoin_qt_button.clicked.connect(self.node_set.bitcoin.launch)
        self.addWidget(self.bitcoin_qt_button, column=self.columns)

        # LND button
        self.lnd_button = QtWidgets.QPushButton('Launch LND')
        # noinspection PyUnresolvedReferences
        self.lnd_button.clicked.connect(self.node_set.lnd.launch)
        self.addWidget(self.lnd_button, column=self.columns)

        self.addWidget(HorizontalLine(), column=self.columns)
