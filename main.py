import os
import sys
from src.ui_interface import *
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from src.Functions import GuiFunctions


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})      # Specify your json file(s) path/name

        # Show Window #
        self.show()

        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)

        # Application functions and events #
        self.app_functions = GuiFunctions(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Install the QCustomQToolTipFilter event to the app in order to use custom tooltip #
    app_tooltip_filter = QCustomQToolTipFilter(tailPosition="auto")
    app.installEventFilter(app_tooltip_filter)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
