import paramiko
import terminal
import tempfile
from PySide import QtCore, QtGui
from PySide.QtGui import QMainWindow, QErrorMessage
from .settings import Ui_SettingsWindow
from ..utils import log
from ..exceptions import NotEnoughInformationError
from ..config import SessionConfig


class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    # Elements from Qt Designer layout
    centralwidget = None
    connection_connect_button = None
    connection_group = None
    connection_hostname = None
    connection_hostname_label = None
    connection_port = None
    connection_port_label = None
    connection_protocol = None
    connection_protocol_label = None
    connection_tab = None
    formLayout = None
    horizontalLayout = None
    session_buttons_group = None
    session_buttons_widget = None
    session_delete = None
    session_group = None
    session_list = None
    session_list_widget = None
    session_load = None
    session_save = None
    session_save_as = None
    session_search = None
    settings_label = None
    settings_tab = None
    tabs = None
    verticalLayout = None
    verticalLayout_2 = None
    verticalLayout_3 = None
    verticalLayout_4 = None
    verticalLayout_5 = None
    verticalLayout_6 = None

    error_message = None

    def __init__(self, litty, parent=None):
        log.debug("Creating SettingsWindow")
        super(SettingsWindow, self).__init__(parent)
        self.litty = litty

        # Use the Qt Designer made layout
        self.setupUi(self)
        self._setup_error_message()

        self._setup_event_listeners()

    def _setup_error_message(self):
        self.error_message = QErrorMessage(self)

    def _setup_event_listeners(self):
        self.connection_connect_button.clicked.connect(
            self._connect_button_clicked
        )

    def _connect_button_clicked(self):
        log.debug("Connect -button clicked")
        try:
            sc = self._get_session_config()
            self.litty.switch_to_terminal(sc)
        except NotEnoughInformationError:
            log.debug("Not enough information to connect")
            self.error_message.showMessage(
                "Not enough information to connect"
            )

    def _get_session_config(self):
        sc = SessionConfig()
        sc.HostName = self.connection_hostname.text()
        sc.Port = self.connection_port.text()

        if not sc.check_settings():
            raise NotEnoughInformationError(
                "Not enough information to connect"
            )

        return sc


class TerminalTab(QtGui.QWidget):
    tabWidget = None
    sessionConfig = None
    client = None
    stdin = None
    stdout = None
    stderr = None
    edit = None

    def __init__(self, tabWidget, sessionConfig, parent=None):
        super(TerminalTab, self).__init__(parent)

        self.tabWidget = tabWidget
        self.sessionConfig = sessionConfig

        plainTextEdit = QtGui.QPlainTextEdit(self)
        gridLayout = QtGui.QGridLayout(self)
        gridLayout.addWidget(plainTextEdit, 0, 0, 1, 1)

        self.edit = plainTextEdit

    def rename(self, newName):
        """Rename this tab"""

        index = self.tabWidget.indexOf(self)
        self.name = newName
        self.tabWidget.setTabText(index, newName)

    def connect_ssh(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(
            paramiko.WarningPolicy()
        )
        self.client.connect(
            hostname=self.sessionConfig.HostName,
            port=int(self.sessionConfig.Port),
            username=self.sessionConfig.User,
            password=self.sessionConfig.Password
        )

        self.stdin, self.stdout, self.stderr = self.client.exec_command(
            'bash'
        )

        self.term = terminal.Terminal(24, 80, temppath=tempfile.gettempdir())

        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.update)
        self.timer.start(5)

    def update(self):
        ok = "is" if self.stdout.channel.in_buffer.read_ready() else "is not"
        log.debug("Update: Connection stdout " + ok + " ready for reading")

        if self.stdout.channel.in_buffer.read_ready():
            out = self.stdout.read(1)
            self.term.write(out)
        else:
            self.term.write("\n")
            self.stdin.write("uptime\n")

        screen = "\n".join(self.term.dump())
        self.edit.setPlainText(screen)


class TerminalWindow(QMainWindow):
    name = "LiTTY"
    size = (980, 760)
    tabs = []
    sessionConfig = None

    tabWidget = None

    def __init__(self, litty, sessionConfig, parent=None):
        super(TerminalWindow, self).__init__(parent)
        self.sessionConfig = sessionConfig
        self.litty = litty
        self._setup_ui()

    def _setup_window(self):
        self.setWindowTitle(self.name)
        self.resize(*self.size)

    def _setup_widgets(self):
        centralwidget = QtGui.QWidget(self)
        gridLayout = QtGui.QGridLayout(centralwidget)
        verticalLayout = QtGui.QVBoxLayout()
        self.tabWidget = QtGui.QTabWidget(centralwidget)

        verticalLayout.addWidget(self.tabWidget)
        gridLayout.addLayout(verticalLayout, 0, 0, 1, 1)
        self.setCentralWidget(centralwidget)

        self.create_tab()

    def create_tab(self):
        tab = TerminalTab(self.tabWidget, self.sessionConfig)

        self.tabWidget.addTab(tab, "")
        self.tabs.append(tab)

        self.tabs[0].rename(self.sessionConfig.get_connection_name())
        tab.connect_ssh()

    def _setup_ui(self):
        self._setup_window()
        self._setup_widgets()

        QtCore.QMetaObject.connectSlotsByName(self)
