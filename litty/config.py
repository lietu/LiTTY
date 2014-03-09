import os
import json
import re


class SessionConfig(object):
    """Connection settings for a session"""

    _HostName = ""
    User = ""
    Port = 22
    Protocol = "ssh"
    UserKnownHostsFile = "/dev/null"
    StrictHostKeyChecking = False
    PasswordAuthentication = False
    IdentityFile = None
    IdentitiesOnly = False
    LogLevel = "FATAL"
    ForwardAgent = True

    def __init__(self, data=None):
        if data:
            for key in data:
                self.__dict__[key] = data[key]

    @property
    def HostName(self):
        """Getter for HostName"""

        return self._HostName

    @HostName.setter
    def HostName(self, value):
        pos = value.find('@')
        if pos >= 0:
            self.User, self._Hostname = value.split('@')
        else:
            self._HostName = value

    def check_settings(self):
        """Check if we have enough settings to connect somewhere"""

        print("Hostname", self.HostName)
        print("_Hostname", self._HostName)
        print("Port", self.Port)

        if len(self.HostName) == 0:
            print("HostName")
            return False

        if len(self.Port) == 0:
            print("Port")
            return False

        return True

    def get_connection_name(self):
        if self.User:
            return self.User + '@' + self.HostName + ':' + self.Port
        return self.HostName + ':' + self.Port


class Config(object):
    sessions = {}

    def load(self, filename):
        filename = os.path.expanduser(filename)
        data = {}
        try:
            with open(filename, 'r') as config:
                data = json.load(config)
        except IOError:
            pass
        except ValueError:
            pass

        if "sessions" in data:
            for item in data["sessions"]:
                self.sessions.append(SessionConfig(item))

    def save(self, filename):
        data = {
            "sessions": self.sessions
        }

        filename = os.path.expanduser(filename)
        with open(filename, 'w') as config:
            json.dump(
                data,
                config,
                sort_keys=True,
                indent=4,
                separators=(',', ': ')
            )

    def read_config(self, text):

        hostreg = re.compile("^Host +(.+)$")
        settingreg = re.compile("^ +([a-zA-Z0-9.-]+) +(.*)$")

        name = None
        session = None
        for line in text.split("\n"):
            match = hostreg.match(line)
            if match:
                if session:
                    self.sessions[name] = session

                session = SessionConfig()
                name = match.group(1)

            if session:
                match = settingreg.match(line)

                if match:
                    key = match.group(1)
                    value = match.group(2)

                    setattr(session, key, value)

        if session:
            self.sessions[name] = session
