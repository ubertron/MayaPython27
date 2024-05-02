import platform
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QHBoxLayout, QTextEdit, QVBoxLayout
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QIcon
from shiboken2 import wrapInstance, getCppPointer
from core_tools import system_utils

if system_utils.is_using_maya_python():
    from maya_tools import MAYA_MAIN_WINDOW

DARWIN_LABEL = "Darwin"


class GenericWidget(QWidget):
    button_size = 24
    margin = 2
    spacing = 2

    def __init__(self, title=None, vertical=True):
        parent = MAYA_MAIN_WINDOW if system_utils.is_using_maya_python() else None
        super(GenericWidget, self).__init__(parent=parent)
        self.title = title
        self.setWindowTitle(title)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(QVBoxLayout() if vertical else QHBoxLayout())
        self.layout().setSpacing(self.margin)
        self.layout().setMargin(self.spacing)
        self.layout().setContentsMargins(self.margin, self.margin, self.margin, self.margin)
        self.layout().setAlignment(Qt.AlignLeft)
        self.setWindowFlags(Qt.Tool if platform.system() == DARWIN_LABEL else Qt.Window)
        self.expand_ui()

    def expand_ui(self, value=True):
        """
        Set this to True to expand the contents to fill the container
        @param value:
        """
        policy = QSizePolicy.Expanding if value else QSizePolicy.Maximum
        widget_types = [QPushButton, QLabel, QTextEdit]
        reg_exp = QRegExp(r".*")

        for widget in [item for sublist in [self.findChildren(t, reg_exp) for t in widget_types] for item in sublist]:
            widget.setSizePolicy(policy, policy)

    def add_button(self, text="", event=None, tool_tip=None, icon=None, fixed_size=False):
        """
        Add button to layout
        @param text:
        @param event:
        @param tool_tip:
        @param icon:
        @param fixed_size:
        @return:
        """
        button = QPushButton(text)
        button.setToolTip(tool_tip)

        if icon:
            button.setIcon(QIcon(icon))

        if icon or fixed_size:
            button.setFixedSize(QSize(self.button_size, self.button_size))
        else:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)

        if event:
            button.clicked.connect(event)

        self.layout().addWidget(button)
        return button

    def add_label(self, text=None, selectable=False, align_center=True):
        """
        Add label to layout
        @param text:
        @param selectable:
        @param align_center:
        @return:
        """
        label = QLabel(text)

        if selectable:
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        if align_center:
            label.setAlignment(Qt.AlignCenter)

        self.layout().addWidget(label)
        return label

    def add_widget(self, widget):
        """
        Add widget to layout
        @param widget:
        @return:
        """
        self.layout().addWidget(widget)
        return widget

    def replace_layout(self, layout):
        """
        Replace layout with a different layout
        @param layout:
        """
        QWidget().setLayout(self.layout())
        self.setLayout(layout)

    def add_stretch(self):
        """
        Add stretch to layout
        """
        self.layout().addStretch(True)

    def add_spacing(self, value):
        """
        Add spacing to layout
        @param value:
        """
        self.layout().addSpacing(value)

    def clear_layout(self, layout=None):
        """
        Empty the layout
        @param layout:
        """
        if not layout:
            layout = self.layout()

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())


class TestWidget(GenericWidget):
    def __init__(self):
        super(TestWidget, self).__init__('Test Widget')
        self.label = self.add_label('Label')
        self.add_button('Get time', event=self.set_date)

    def set_date(self):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.label.setText("Current time is {}".format(current_time))


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    from datetime import datetime

    app = QApplication()
    test_widget = TestWidget()
    test_widget.show()
    app.exec_()
