from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class GuiFunctions:
    def __init__(self, main_window):
        self.main = main_window         # Store main window instance
        self.ui = main_window.ui        # Store the ui instance
        self.load_custom_font()         # Apply font
        self.initialize_app_theme()     # Init app theme
        self.ui.search_btn.clicked.connect(self.show_search_results)      # Add click event to search button
        self.connect_menu_buttons()     # Connect menu buttons

    def connect_menu_buttons(self):
        """
        Connect buttons to expand / collapse menu widgets
        :return: None
        """
        # Expand center menu widget #
        self.ui.settings_btn.clicked.connect(lambda: self.ui.center_menu.expandMenu())
        self.ui.info_btn.clicked.connect(lambda: self.ui.center_menu.expandMenu())
        self.ui.help_btn.clicked.connect(lambda: self.ui.center_menu.expandMenu())

        # Collapse center menu widget #
        self.ui.center_menu_close_btn.clicked.connect(lambda: self.ui.center_menu.collapseMenu())

        # Expand right menu widget #
        self.ui.notification_btn.clicked.connect(lambda: self.ui.right_menu.expandMenu())
        self.ui.more_btn.clicked.connect(lambda: self.ui.right_menu.expandMenu())
        self.ui.profile_btn.clicked.connect(lambda: self.ui.right_menu.expandMenu())

        # Collapse right menu widget #
        self.ui.right_menu_close_btn.clicked.connect(lambda: self.ui.right_menu.collapseMenu())

    def create_search_tip_overlay(self):
        """
        Create a search tip overlay under the search input
        :return: None
        """
        self.search_tool_tip = QCustomTipOverlay(
            title="Search results",
            description="Searching...",
            icon=self.main.theme.PATH_RESOURCES + "feather/search.png",  # Icon path from theme resources
            isClosable=True,
            target=self.ui.search_frame,  # Put tip overlay under search input
            parent=self.main,
            deleteOnClose=True,
            duration=-1,  # Set duration to -1 to prevent auto-close
            tailPosition="top-center",
            closeIcon=self.main.theme.PATH_RESOURCES + "material_design/close.png",  # Add a close icon
            toolFlag=True
        )

        # Create loader #
        loader = QCustom3CirclesLoader(
            parent=self.search_tool_tip,
            color=QColor(self.main.theme.COLOR_ACCENT_1),       # Color from the theme
            penWidth=20,
            animationDuration=400
        )

        self.search_tool_tip.addWidget(loader)      # Add loader to the tip overlay

    def show_search_results(self):
        """
        Show search container
        :return: None
        """
        search_phrase = self.ui.search_line.text()      # Get text from search bar
        # If search_phrase is empty #
        if not search_phrase:
            return

        try:
            self.search_tool_tip.show()

        # tool tip deleted #
        except:
            self.create_search_tip_overlay()        # re-init
            self.search_tool_tip.show()

        self.search_tool_tip.setDescription("Showing search results for: " + search_phrase)  # Update search description

    # Initialize app theme
    def initialize_app_theme(self):
        """
        Initialize app theme from settings
        :return: None
        """
        settings = QSettings()
        current_theme = settings.value("THEME")
        # print("Current theme is: ", current_theme)

        self.populate_theme_list(current_theme)  # Add them to the theme list
        # Connect theme change to change_app_theme #
        self.ui.theme_list.currentTextChanged.connect(self.change_app_theme)

    def populate_theme_list(self, current_theme):
        """
        Populate the list from available app themes
        :param current_theme: Currently applied app theme
        :return: None
        """
        theme_count = -1

        for theme in self.ui.themes:
            self.ui.theme_list.addItem(theme.name, theme.name)

            # check default / current theme #
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.theme_list.setCurrentIndex(theme_count)  # Select the theme

    def change_app_theme(self):
        """
        Change app theme based on user selection
        :return: None
        """
        settings = QSettings()
        selected_theme = self.ui.theme_list.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            # Apply new theme #
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    def load_custom_font(self):
        """
        Load and apply custom font
        :return: None
        """
        font_id = QFontDatabase.addApplicationFont("./fonts/google-sans-cufonfonts/ProductSans-Regular.ttf")

        # If font loaded #
        if font_id == -1:
            print("Failed to load the font")
            return

        # Apply font #
        font_family = QFontDatabase.applicationFontFamilies(font_id)

        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")

        self.main.setFont(product_sans)  # Apply to main window
