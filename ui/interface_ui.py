# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import _icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(942, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.left_menu = QCustomSlideMenu(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.left_menu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 5, 0, 5)
        self.widget_4 = QWidget(self.left_menu)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(46, 42))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.menu_btn = QPushButton(self.widget_4)
        self.menu_btn.setObjectName(u"menu_btn")
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menu_btn)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_5 = QWidget(self.left_menu)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(118, 140))
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 0, 5)
        self.home_btn = QPushButton(self.widget_5)
        self.home_btn.setObjectName(u"home_btn")
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.home_btn)

        self.create_json_btn = QPushButton(self.widget_5)
        self.create_json_btn.setObjectName(u"create_json_btn")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/file-plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_json_btn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.create_json_btn)

        self.reports_btn = QPushButton(self.widget_5)
        self.reports_btn.setObjectName(u"reports_btn")
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/printer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reports_btn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.reports_btn)

        self.graphs_btn = QPushButton(self.widget_5)
        self.graphs_btn.setObjectName(u"graphs_btn")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/pie-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphs_btn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.graphs_btn)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_6 = QWidget(self.left_menu)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(114, 108))
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.settings_btn = QPushButton(self.widget_6)
        self.settings_btn.setObjectName(u"settings_btn")
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.settings_btn)

        self.info_btn = QPushButton(self.widget_6)
        self.info_btn.setObjectName(u"info_btn")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_btn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.info_btn)

        self.help_btn = QPushButton(self.widget_6)
        self.help_btn.setObjectName(u"help_btn")
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help_btn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.help_btn)


        self.verticalLayout.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.left_menu)

        self.center_menu = QCustomSlideMenu(self.centralwidget)
        self.center_menu.setObjectName(u"center_menu")
        self.center_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.center_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, -1)
        self.widget = QWidget(self.center_menu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.center_menu_close_btn = QPushButton(self.widget)
        self.center_menu_close_btn.setObjectName(u"center_menu_close_btn")
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.center_menu_close_btn.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.center_menu_close_btn)


        self.verticalLayout_5.addWidget(self.widget)

        self.center_menu_pages = QCustomQStackedWidget(self.center_menu)
        self.center_menu_pages.setObjectName(u"center_menu_pages")
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_6 = QVBoxLayout(self.settings_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.widget_2 = QWidget(self.settings_page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.theme_list = QComboBox(self.frame)
        self.theme_list.setObjectName(u"theme_list")

        self.horizontalLayout_3.addWidget(self.theme_list)


        self.verticalLayout_7.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.center_menu_pages.addWidget(self.settings_page)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.verticalLayout_8 = QVBoxLayout(self.info_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.info_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.center_menu_pages.addWidget(self.info_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.verticalLayout_9 = QVBoxLayout(self.help_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.help_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.center_menu_pages.addWidget(self.help_page)

        self.verticalLayout_5.addWidget(self.center_menu_pages)


        self.horizontalLayout.addWidget(self.center_menu)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.main_body)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header = QWidget(self.main_body)
        self.header.setObjectName(u"header")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 5)
        self.title_txt = QLabel(self.header)
        self.title_txt.setObjectName(u"title_txt")

        self.horizontalLayout_7.addWidget(self.title_txt, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notification_btn = QPushButton(self.frame_3)
        self.notification_btn.setObjectName(u"notification_btn")
        icon9 = QIcon()
        icon9.addFile(u":/font_awesome_regular/icons/font_awesome/regular/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notification_btn.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notification_btn)

        self.more_btn = QPushButton(self.frame_3)
        self.more_btn.setObjectName(u"more_btn")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.more_btn.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.more_btn)

        self.profile_btn = QPushButton(self.frame_3)
        self.profile_btn.setObjectName(u"profile_btn")
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_btn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.profile_btn)


        self.horizontalLayout_7.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.search_frame = QFrame(self.header)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMaximumSize(QSize(251, 16777215))
        self.search_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.search_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(16, 16))
        self.label_9.setMaximumSize(QSize(16, 16))
        self.label_9.setPixmap(QPixmap(u":/feather/icons/feather/search.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.search_line = QLineEdit(self.search_frame)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_8.addWidget(self.search_line)

        self.search_btn = QPushButton(self.search_frame)
        self.search_btn.setObjectName(u"search_btn")

        self.horizontalLayout_8.addWidget(self.search_btn)


        self.horizontalLayout_7.addWidget(self.search_frame)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame_4)
        self.minimize_btn.setObjectName(u"minimize_btn")
        icon12 = QIcon()
        icon12.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon12)

        self.horizontalLayout_9.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_4)
        self.maximize_btn.setObjectName(u"maximize_btn")
        icon13 = QIcon()
        icon13.addFile(u":/material_design/icons/material_design/crop_square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_btn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_4)
        self.close_btn.setObjectName(u"close_btn")
        icon14 = QIcon()
        icon14.addFile(u":/material_design/icons/material_design/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.close_btn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.main_content = QWidget(self.main_body)
        self.main_content.setObjectName(u"main_content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10 = QHBoxLayout(self.main_content)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 5, 5, 5)
        self.main_page_content = QWidget(self.main_content)
        self.main_page_content.setObjectName(u"main_page_content")
        self.verticalLayout_11 = QVBoxLayout(self.main_page_content)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 5, 0, 5)
        self.main_pages = QCustomQStackedWidget(self.main_page_content)
        self.main_pages.setObjectName(u"main_pages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_12 = QVBoxLayout(self.home_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_8 = QLabel(self.home_page)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.main_pages.addWidget(self.home_page)
        self.create_json_page = QWidget()
        self.create_json_page.setObjectName(u"create_json_page")
        self.verticalLayout_13 = QVBoxLayout(self.create_json_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.create_json_page)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.main_pages.addWidget(self.create_json_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.verticalLayout_14 = QVBoxLayout(self.reports_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.reports_page)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.main_pages.addWidget(self.reports_page)
        self.graphs_page = QWidget()
        self.graphs_page.setObjectName(u"graphs_page")
        self.verticalLayout_15 = QVBoxLayout(self.graphs_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.graphs_page)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_15.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.main_pages.addWidget(self.graphs_page)

        self.verticalLayout_11.addWidget(self.main_pages)


        self.horizontalLayout_10.addWidget(self.main_page_content)

        self.right_menu = QCustomSlideMenu(self.main_content)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_16 = QVBoxLayout(self.right_menu)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(self.right_menu)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.right_menu_close_btn = QPushButton(self.widget_3)
        self.right_menu_close_btn.setObjectName(u"right_menu_close_btn")
        self.right_menu_close_btn.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.right_menu_close_btn)


        self.verticalLayout_16.addWidget(self.widget_3)

        self.right_menu_pages = QCustomQStackedWidget(self.right_menu)
        self.right_menu_pages.setObjectName(u"right_menu_pages")
        self.notification_page = QWidget()
        self.notification_page.setObjectName(u"notification_page")
        self.verticalLayout_17 = QVBoxLayout(self.notification_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.notification_page)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_17.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.right_menu_pages.addWidget(self.notification_page)
        self.more_page = QWidget()
        self.more_page.setObjectName(u"more_page")
        self.verticalLayout_18 = QVBoxLayout(self.more_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_15 = QLabel(self.more_page)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_18.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.right_menu_pages.addWidget(self.more_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_19 = QVBoxLayout(self.profile_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.profile_page)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_19.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.right_menu_pages.addWidget(self.profile_page)

        self.verticalLayout_16.addWidget(self.right_menu_pages)


        self.horizontalLayout_10.addWidget(self.right_menu)


        self.verticalLayout_10.addWidget(self.main_content)

        self.footer = QWidget(self.main_body)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 0)
        self.label_6 = QLabel(self.footer)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.footer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.horizontalLayout_4.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(15, 15))
        self.size_grip.setMaximumSize(QSize(15, 15))
        self.size_grip.setFrameShape(QFrame.Shape.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.size_grip, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_10.addWidget(self.footer, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.center_menu_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menu_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Side Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menu_btn.setText("")
#if QT_CONFIG(tooltip)
        self.home_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.create_json_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Create JSON File", None))
#endif // QT_CONFIG(tooltip)
        self.create_json_btn.setText(QCoreApplication.translate("MainWindow", u"Create JSON", None))
#if QT_CONFIG(tooltip)
        self.reports_btn.setToolTip(QCoreApplication.translate("MainWindow", u"View Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.graphs_btn.setToolTip(QCoreApplication.translate("MainWindow", u"View Graphs", None))
#endif // QT_CONFIG(tooltip)
        self.graphs_btn.setText(QCoreApplication.translate("MainWindow", u"Graphs", None))
#if QT_CONFIG(tooltip)
        self.settings_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.info_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Inforamtions", None))
#endif // QT_CONFIG(tooltip)
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.help_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
#if QT_CONFIG(tooltip)
        self.center_menu_close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.center_menu_close_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.title_txt.setText(QCoreApplication.translate("MainWindow", u"General template", None))
#if QT_CONFIG(tooltip)
        self.notification_btn.setToolTip(QCoreApplication.translate("MainWindow", u"View Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notification_btn.setText("")
#if QT_CONFIG(tooltip)
        self.more_btn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.more_btn.setText("")
#if QT_CONFIG(tooltip)
        self.profile_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Profiles", None))
#endif // QT_CONFIG(tooltip)
        self.profile_btn.setText("")
        self.label_9.setText("")
        self.search_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
#if QT_CONFIG(tooltip)
        self.search_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Ctrl+K", None))
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"restore", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Home page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Create JSON page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reports page", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Graphs page", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Right menu", None))
#if QT_CONFIG(tooltip)
        self.right_menu_close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.right_menu_close_btn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Copyright / Org. name / whatever", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Progress bar", None))
    # retranslateUi

