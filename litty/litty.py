from .config import Config
from .ui.windows import TerminalWindow, SettingsWindow
from .utils import log
from PySide.QtGui import QApplication
import sys


defaultConfig = "~/.litty_config.json"


class LiTTY(object):
    def __init__(self):
        self.args = None
        self.config = Config()
        self.configFile = defaultConfig
        self.sessionConfig = None
        self.settingsWindow = None
        self.terminalWindows = []

    def start(self):
        self.config.load(self.configFile)

        # Create the application
        app = QApplication(self.args)

        # Pick which window to show
        if self.have_connection_info():
            log.debug(
                "Got connection info from CLI, launching terminal window"
            )
            self.create_terminal_window(self.sessionConfig)
        else:
            log.debug("Launching settings window")
            self.settingsWindow = SettingsWindow(self)
            self.settingsWindow.show()

        # Enter Qt application main loop
        app.exec_()
        self.config.save(self.configFile)
        sys.exit()

    def switch_to_terminal(self, sessionConfig):
        if self.settingsWindow:
            self.settingsWindow.hide()

        self.create_terminal_window(sessionConfig)

    def create_terminal_window(self, sessionConfig):
        tw = TerminalWindow(self, sessionConfig)
        tw.show()
        self.terminalWindows.append(tw)

    def have_connection_info(self):
        if self.sessionConfig:
            ok = self.sessionConfig.check_settings()
            print(self.sessionConfig.__dict__)
            okStr = "ok" if ok else "not ok"
            log.debug("Got session config, it is " + okStr)
            if ok:
                return True

        return False

    def parse_ssh_config(self, text):
        self.config.read_config(text)
        if "default" in self.config.sessions.keys():
            log.debug("Found a default connection in config")
            self.sessionConfig = self.config.sessions["default"]

    def parse_args(self, args):
        self.args = args
