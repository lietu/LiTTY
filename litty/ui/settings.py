# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'litty\ui\settings.ui'
#
# Created: Sun Jan 26 10:39:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(391, 557)
        self.centralwidget = QtGui.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.connection_tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connection_tab.sizePolicy().hasHeightForWidth())
        self.connection_tab.setSizePolicy(sizePolicy)
        self.connection_tab.setObjectName("connection_tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.connection_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.connection_group = QtGui.QGroupBox(self.connection_tab)
        self.connection_group.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connection_group.sizePolicy().hasHeightForWidth())
        self.connection_group.setSizePolicy(sizePolicy)
        self.connection_group.setMaximumSize(QtCore.QSize(16777215, 200))
        self.connection_group.setObjectName("connection_group")
        self.formLayout = QtGui.QFormLayout(self.connection_group)
        self.formLayout.setObjectName("formLayout")
        self.connection_port_label = QtGui.QLabel(self.connection_group)
        self.connection_port_label.setObjectName("connection_port_label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole,
                                  self.connection_port_label)
        self.connection_port = QtGui.QLineEdit(self.connection_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connection_port.sizePolicy().hasHeightForWidth())
        self.connection_port.setSizePolicy(sizePolicy)
        self.connection_port.setMaximumSize(QtCore.QSize(100, 16777215))
        self.connection_port.setInputMask("")
        self.connection_port.setMaxLength(5)
        self.connection_port.setObjectName("connection_port")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole,
                                  self.connection_port)
        self.connection_hostname_label = QtGui.QLabel(self.connection_group)
        self.connection_hostname_label.setObjectName(
            "connection_hostname_label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole,
                                  self.connection_hostname_label)
        self.connection_hostname = QtGui.QLineEdit(self.connection_group)
        self.connection_hostname.setMinimumSize(QtCore.QSize(200, 0))
        self.connection_hostname.setObjectName("connection_hostname")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole,
                                  self.connection_hostname)
        self.connection_protocol_label = QtGui.QLabel(self.connection_group)
        self.connection_protocol_label.setLayoutDirection(
            QtCore.Qt.LeftToRight)
        self.connection_protocol_label.setObjectName(
            "connection_protocol_label")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole,
                                  self.connection_protocol_label)
        self.connection_protocol = QtGui.QComboBox(self.connection_group)
        self.connection_protocol.setMaximumSize(QtCore.QSize(100, 16777215))
        self.connection_protocol.setObjectName("connection_protocol")
        self.connection_protocol.addItem("")
        self.connection_protocol.addItem("")
        self.connection_protocol.addItem("")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole,
                                  self.connection_protocol)
        self.connection_connect_button = QtGui.QPushButton(
            self.connection_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connection_connect_button.sizePolicy().hasHeightForWidth())
        self.connection_connect_button.setSizePolicy(sizePolicy)
        self.connection_connect_button.setMinimumSize(QtCore.QSize(100, 50))
        self.connection_connect_button.setDefault(True)
        self.connection_connect_button.setObjectName(
            "connection_connect_button")
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole,
                                  self.connection_connect_button)
        self.verticalLayout_2.addWidget(self.connection_group)
        self.session_group = QtGui.QGroupBox(self.connection_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.session_group.sizePolicy().hasHeightForWidth())
        self.session_group.setSizePolicy(sizePolicy)
        self.session_group.setMinimumSize(QtCore.QSize(0, 288))
        self.session_group.setBaseSize(QtCore.QSize(0, 198))
        self.session_group.setObjectName("session_group")
        self.horizontalLayout = QtGui.QHBoxLayout(self.session_group)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.session_list_widget = QtGui.QWidget(self.session_group)
        self.session_list_widget.setMinimumSize(QtCore.QSize(200, 0))
        self.session_list_widget.setObjectName("session_list_widget")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.session_list_widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.session_search = QtGui.QLineEdit(self.session_list_widget)
        self.session_search.setText("")
        self.session_search.setObjectName("session_search")
        self.verticalLayout_6.addWidget(self.session_search)
        self.session_list = QtGui.QListWidget(self.session_list_widget)
        self.session_list.setResizeMode(QtGui.QListView.Fixed)
        self.session_list.setObjectName("session_list")
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        QtGui.QListWidgetItem(self.session_list)
        self.verticalLayout_6.addWidget(self.session_list)
        self.horizontalLayout.addWidget(self.session_list_widget)
        self.session_buttons_group = QtGui.QWidget(self.session_group)
        self.session_buttons_group.setMinimumSize(QtCore.QSize(100, 0))
        self.session_buttons_group.setObjectName("session_buttons_group")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.session_buttons_group)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.session_save_as = QtGui.QPushButton(self.session_buttons_group)
        self.session_save_as.setObjectName("session_save_as")
        self.verticalLayout_5.addWidget(self.session_save_as)
        self.session_buttons_widget = QtGui.QWidget(self.session_buttons_group)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
                                       QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.session_buttons_widget.sizePolicy().hasHeightForWidth())
        self.session_buttons_widget.setSizePolicy(sizePolicy)
        self.session_buttons_widget.setMinimumSize(QtCore.QSize(100, 0))
        self.session_buttons_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.session_buttons_widget.setObjectName("session_buttons_widget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.session_buttons_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.session_load = QtGui.QPushButton(self.session_buttons_widget)
        self.session_load.setObjectName("session_load")
        self.verticalLayout_4.addWidget(self.session_load)
        self.session_save = QtGui.QPushButton(self.session_buttons_widget)
        self.session_save.setObjectName("session_save")
        self.verticalLayout_4.addWidget(self.session_save)
        self.session_delete = QtGui.QPushButton(self.session_buttons_widget)
        self.session_delete.setObjectName("session_delete")
        self.verticalLayout_4.addWidget(self.session_delete)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.session_buttons_widget)
        self.horizontalLayout.addWidget(self.session_buttons_group)
        self.verticalLayout_2.addWidget(self.session_group)
        self.tabs.addTab(self.connection_tab, "")
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.settings_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.settings_label = QtGui.QLabel(self.settings_tab)
        self.settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_label.setObjectName("settings_label")
        self.verticalLayout_3.addWidget(self.settings_label)
        self.tabs.addTab(self.settings_tab, "")
        self.verticalLayout.addWidget(self.tabs)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(
            QtGui.QApplication.translate("SettingsWindow", "MainWindow", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_group.setTitle(
            QtGui.QApplication.translate("SettingsWindow",
                                         "Connection information", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_port_label.setText(
            QtGui.QApplication.translate("SettingsWindow", "Port", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_port.setText(
            QtGui.QApplication.translate("SettingsWindow", "22", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_port.setPlaceholderText(
            QtGui.QApplication.translate("SettingsWindow", "1-65535", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_hostname_label.setText(
            QtGui.QApplication.translate("SettingsWindow",
                                         "Address (hostname or IP)", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_hostname.setPlaceholderText(
            QtGui.QApplication.translate("SettingsWindow",
                                         "fqdn.domain.com or 1.2.3.4", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_protocol_label.setText(
            QtGui.QApplication.translate("SettingsWindow", "Protocol", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.connection_protocol.setItemText(0, QtGui.QApplication.translate(
            "SettingsWindow", "SSH", None, QtGui.QApplication.UnicodeUTF8))
        self.connection_protocol.setItemText(1, QtGui.QApplication.translate(
            "SettingsWindow", "Telnet", None, QtGui.QApplication.UnicodeUTF8))
        self.connection_protocol.setItemText(2, QtGui.QApplication.translate(
            "SettingsWindow", "Raw", None, QtGui.QApplication.UnicodeUTF8))
        self.connection_connect_button.setText(
            QtGui.QApplication.translate("SettingsWindow", "Connect", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_group.setTitle(
            QtGui.QApplication.translate("SettingsWindow", "Session manager",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.session_search.setPlaceholderText(
            QtGui.QApplication.translate("SettingsWindow", "Search", None,
                                         QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.session_list.isSortingEnabled()
        self.session_list.setSortingEnabled(False)
        self.session_list.item(0).setText(
            QtGui.QApplication.translate("SettingsWindow", "Default Session",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(1).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(2).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(3).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(4).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(5).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(6).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(7).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(8).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(9).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(10).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(11).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(12).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(13).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(14).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(15).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(16).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(17).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(18).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(19).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.item(20).setText(
            QtGui.QApplication.translate("SettingsWindow", "New Item", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_list.setSortingEnabled(__sortingEnabled)
        self.session_save_as.setText(
            QtGui.QApplication.translate("SettingsWindow", "Save As...", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_load.setText(
            QtGui.QApplication.translate("SettingsWindow", "Load", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_save.setText(
            QtGui.QApplication.translate("SettingsWindow", "Save", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.session_delete.setText(
            QtGui.QApplication.translate("SettingsWindow", "Delete", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.connection_tab),
                             QtGui.QApplication.translate("SettingsWindow",
                                                          "Connection", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.settings_label.setText(
            QtGui.QApplication.translate("SettingsWindow", "Maybe later", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.settings_tab),
                             QtGui.QApplication.translate("SettingsWindow",
                                                          "Settings", None,
                                                          QtGui.QApplication.UnicodeUTF8))

