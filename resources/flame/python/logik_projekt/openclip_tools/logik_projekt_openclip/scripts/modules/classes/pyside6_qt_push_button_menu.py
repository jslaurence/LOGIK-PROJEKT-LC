#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        pyside6_qt_push_button_menu.py
# Version:          1.0.1
# Created:          2024-01-19
# Modified:         2024-11-16

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

# Standard library imports
import ast
import datetime
import functools
import importlib.util
import os
import re
import shutil
import subprocess
import typing
from typing import (
    Union,
    List,
    Dict,
    Optional,
    Callable
)
import xml
import xml.etree.ElementTree as ET

# Third Party library imports
from PySide6 import (
    QtWidgets,
    QtCore,
    QtGui
)

class pyside6_qt_push_button_menu(QtWidgets.QPushButton):
    '''
    Custom Qt Flame Menu Push Button Widget

    pyside6_qt_push_button_menu(button_name, menu_options[, menu_width=150, max_menu_width=2000, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_width: (optional) width of widget. default is 150. [int]
    max_menu_width: (optional) set maximum width of widget. default is 2000. [int]
    menu_action: (optional) execute when button is changed. [function]

    To update an existing button menu:

    pyside6_qt_push_button_menu.update_menu(button_name, menu_options[, menu_action=None])

    button_name: text displayed on button [str]
    menu_options: list of options show when button is pressed [list]
    menu_action: (optional) execute when button is changed. [function]

    Examples:

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = pyside6_qt_push_button_menu('push_button_name', push_button_menu_options)

        or

        push_button_menu_options = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        menu_push_button = pyside6_qt_push_button_menu(push_button_menu_options[0], push_button_menu_options)
    '''

    def __init__(self, button_name: str, menu_options: List[str], menu_width: Optional[int]=150, max_menu_width: Optional[int]=2000, menu_action: Optional[Callable[..., None]]=None):
        super(pyside6_qt_push_button_menu, self).__init__()
        from functools import partial

        # Check argument types

        if not isinstance(button_name, str):
            raise TypeError('pyside6_qt_push_button_menu: button_name must be string.')
        if not isinstance(menu_options, list):
            raise TypeError('pyside6_qt_push_button_menu: menu_options must be list.')
        if not isinstance(menu_width, int):
            raise TypeError('pyside6_qt_push_button_menu: menu_width must be integer.')
        if not isinstance(max_menu_width, int):
            raise TypeError('pyside6_qt_push_button_menu: max_menu_width must be integer.')

        # Build push button menu

        self.setText(button_name)
        self.setMinimumHeight(28)
        self.setMinimumWidth(menu_width)
        self.setMaximumWidth(max_menu_width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setStyleSheet('QPushButton {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                           'QPushButton:disabled {color: rgb(116, 116, 116); background-color: rgb(45, 55, 68); border: none}'
                           'QPushButton:hover {border: 1px solid rgb(90, 90, 90)}'
                           'QPushButton::menu-indicator {image: none}'
                           'QToolTip {color: rgb(170, 170, 170); background-color: rgb(71, 71, 71); border: 10px solid rgb(71, 71, 71)}')

        self.pushbutton_menu = QtWidgets.QMenu(self)
        self.pushbutton_menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushbutton_menu.setMinimumWidth(menu_width)
        self.pushbutton_menu.setStyleSheet('QMenu {color: rgb(154, 154, 154); background-color: rgb(45, 55, 68); border: none; font: 14px "Discreet"}'
                                           'QMenu::item:selected {color: rgb(217, 217, 217); background-color: rgb(58, 69, 81)}')
        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

        self.setMenu(self.pushbutton_menu)

    def create_menu(self, menu, menu_action):
        self.setText(menu)
        if menu_action:
            menu_action()

    def update_menu(self, button_name: str, menu_options: List[str], menu_action=None):
        from functools import partial

        self.setText(button_name)

        self.pushbutton_menu.clear()

        for menu in menu_options:
            self.pushbutton_menu.addAction(menu, partial(self.create_menu, menu, menu_action))

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# # If this script is executed as main:
# # Call functions for immediate execution
# if __name__ == "__main__":

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.1
# modified:              2024-05-07 - 21:48:20
# comments:              Refactored monolithic code to discreet modules
# -------------------------------------------------------------------------- #
# version:               0.0.2
# modified:              2024-05-07 - 21:49:31
# comments:              Added docstrings
# -------------------------------------------------------------------------- #
# version:               0.0.3
# modified:              2024-05-07 - 21:50:00
# comments:              Prep for initial production test
# -------------------------------------------------------------------------- #
# version:               0.0.4
# modified:              2024-05-09 - 13:18:47
# comments:              Refactored code works in flame 2025. Time to tidy up.
# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-17 - 13:36:42
# comments:              Replaced FlameButton with pyside6_qt_button
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-17 - 13:37:49
# comments:              Replaced FlameClickableLineEdit with pyside6_qt_clickable_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-17 - 13:38:19
# comments:              Replaced FlameLabel with pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-17 - 13:38:29
# comments:              Replaced FlameLineEdit with pyside6_qt_line_edit
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-17 - 13:39:27
# comments:              Replaced FlameListWidget with pyside6_qt_list_widget
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-17 - 13:39:47
# comments:              Replaced FlameMessageWindow with pyside6_qt_message_window
# -------------------------------------------------------------------------- #
# version:               0.1.1
# modified:              2024-05-17 - 13:40:01
# comments:              Replaced FlamePasswordWindow with pyside6_qt_password_window
# -------------------------------------------------------------------------- #
# version:               0.1.2
# modified:              2024-05-17 - 13:40:28
# comments:              Replaced FlamePresetWindow with pyside6_qt_preset_window
# -------------------------------------------------------------------------- #
# version:               0.1.3
# modified:              2024-05-17 - 13:40:37
# comments:              Replaced FlameProgressWindow with pyside6_qt_progress_window
# -------------------------------------------------------------------------- #
# version:               0.1.4
# modified:              2024-05-17 - 13:41:39
# comments:              Replaced FlamePushButton with pyside6_qt_push_button
# -------------------------------------------------------------------------- #
# version:               0.1.5
# modified:              2024-05-17 - 13:41:49
# comments:              Replaced FlamePushButtonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.1.6
# modified:              2024-05-17 - 13:42:30
# comments:              Replaced FlameQDialog with pyside6_qt_qdialog
# -------------------------------------------------------------------------- #
# version:               0.1.7
# modified:              2024-05-17 - 13:44:20
# comments:              Replaced FlameSlider with pyside6_qt_slider
# -------------------------------------------------------------------------- #
# version:               0.1.8
# modified:              2024-05-17 - 13:44:30
# comments:              Replaced FlameTextEdit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.1.9
# modified:              2024-05-17 - 13:44:39
# comments:              Replaced FlameTokenPushButton with pyside6_qt_token_push_button
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-17 - 13:45:12
# comments:              Replaced FlameTreeWidget with pyside6_qt_tree_widget
# -------------------------------------------------------------------------- #
# version:               0.2.1
# modified:              2024-05-17 - 13:45:29
# comments:              Replaced FlameWindow with pyside6_qt_window
# -------------------------------------------------------------------------- #
# version:               0.2.2
# modified:              2024-05-17 - 13:45:43
# comments:              Replaced pyflame_file_browser with pyside6_qt_file_browser
# -------------------------------------------------------------------------- #
# version:               0.2.3
# modified:              2024-05-17 - 13:47:07
# comments:              Replaced pyflame_get_flame_version with pyside6_qt_get_flame_version
# -------------------------------------------------------------------------- #
# version:               0.2.4
# modified:              2024-05-17 - 13:47:43
# comments:              Replaced pyflame_get_shot_name with pyside6_qt_get_shot_name
# -------------------------------------------------------------------------- #
# version:               0.2.5
# modified:              2024-05-17 - 13:47:56
# comments:              Replaced pyflame_load_config with pyside6_qt_load_config
# -------------------------------------------------------------------------- #
# version:               0.2.6
# modified:              2024-05-17 - 13:49:42
# comments:              Replaced pyflame_open_in_finder with pyside6_qt_open_in_finder
# -------------------------------------------------------------------------- #
# version:               0.2.7
# modified:              2024-05-17 - 13:49:51
# comments:              Replaced pyflame_print with pyside6_qt_print
# -------------------------------------------------------------------------- #
# version:               0.2.8
# modified:              2024-05-17 - 13:50:00
# comments:              Replaced pyflame_refresh_hooks with pyside6_qt_refresh_hooks
# -------------------------------------------------------------------------- #
# version:               0.2.9
# modified:              2024-05-17 - 13:50:10
# comments:              Replaced pyflame_resolve_path_tokens with pyside6_qt_resolve_path_tokens
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-17 - 13:50:21
# comments:              Replaced pyflame_resolve_shot_name with pyside6_qt_resolve_shot_name
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-17 - 13:50:32
# comments:              Replaced pyflame_save_config with pyside6_qt_save_config
# -------------------------------------------------------------------------- #
# version:               0.3.2
# modified:              2024-05-17 - 15:16:41
# comments:              Replaced pyside6_qt_textedit with pyside6_qt_text_edit
# -------------------------------------------------------------------------- #
# version:               0.3.3
# modified:              2024-05-17 - 15:48:00
# comments:              Replaced pyside6_qt_push_buttonMenu with pyside6_qt_push_button_menu
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-05-18 - 18:00:39
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-05-18 - 18:46:09
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-06-04 - 17:38:52
# comments:              Added 'Smart Replace' option for render and write nodes
# -------------------------------------------------------------------------- #
# version:               0.4.6
# modified:              2024-06-05 - 19:30:33
# comments:              Added a new script to create openclip multichannel
# -------------------------------------------------------------------------- #
# version:               0.4.7
# modified:              2024-06-05 - 21:08:34
# comments:              Modified note strings
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-06-26 - 22:31:48
# comments:              Fixed missing import statements for pyside6_qt_label
# -------------------------------------------------------------------------- #
# version:               0.4.8
# modified:              2024-07-11 - 08:39:06
# comments:              Added new schematic reels for batch groups
# -------------------------------------------------------------------------- #
# version:               0.4.9
# modified:              2024-07-11 - 08:41:36
# comments:              Fixed a version bug for the changelist updater script
# -------------------------------------------------------------------------- #
# version:               0.5.0
# modified:              2024-08-31 - 18:26:05
# comments:              prep for release.
# -------------------------------------------------------------------------- #
# version:               1.0.0
# modified:              2024-10-30 - 07:35:26
# comments:              Refactored PySide6 Output Node Config UI.
# -------------------------------------------------------------------------- #
# version:               1.0.1
# modified:              2024-11-16 - 16:52:06
# comments:              Fixed circular import statements
# -------------------------------------------------------------------------- #
