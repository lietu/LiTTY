# LiTTY

## About LiTTY

LiTTY is (going to be) a cross-platform SSH client similar to PuTTY (which is
Windows only) by Janne Enberg aka. Lietu. LiTTY is made with Python, and uses
PySide Qt (4.8 for now) bindings for UI components.


## Licensing

This project is currently published under the new BSD and MIT licenses.

If you decide to contribute you agree that I, Janne Enberg, can at any point in
time decide to change the license of the project without prior notice or anything
to some other license from that point on.

But really it's quite unlikely I would do this, I would consider it only to get
some REALLY nifty library in use in case they use a silly license such as AGPLv3.
And even then it would have to be pretty god-like.


## How to develop LiTTY

Want to help? Great! Here's some instructions on how to work on the code.


### Current status

Currently the software does NOT work for any purpose "as is", but it is possible
to get it in a "slightly working" state with little effort.

There is currently no component to handle the terminal processing, but if you
download the terminal code from GateOne and put it in git-clone/terminal/*.py
the code magically comes to life (a bit). Isn't that a lucky coincidence?

You can get the GateOne terminal code from:
https://github.com/liftoff/GateOne/tree/master/terminal

Make sure you do not try and commit that code to this project, their AGPLv3
license is not compatible with LiTTY licensing.


### Development environment

1. You will need Python installed, get it from http://www.python.org/getit/ or
    your operating system's repositories
   * Both 2.7 and 3.3 have been tested to work
1. You will need Qt tools installed download from the Qt homepage at
http://qt-project.org/
1. You will need PySide installed, get it too from the Qt homepage at
http://qt-project.org/wiki/PySide
   * Windows: http://qt-project.org/wiki/PySide_Binaries_Windows
1. At least Windows users will probably want to download PyCrypto as a binary
  from http://www.voidspace.org.uk/python/weblog/arch_d7_2010_07_03.shtml
1. Some sort of a Python-aware IDE/editor is generally nice to have, PyCharm and
 Sublime Text are both good for the job
1. Install the rest of the required python packages ```pip install --user -r
requirements.txt```

Installing PyCrypto on Windows is most easily done by downloading it from
http://www.voidspace.org.uk/python/modules.shtml#pycrypto


### Working on the UI

The terminal window is custom code, originally made with Qt Designer but heavily
modified since. Working on it means getting your hands dirty and digging in Python
code in the TerminalWindow class in litty/ui/windows.py.

The settings window is however some small custom code on top of a Qt Designer
managed design. To work on it open litty/ui/settings.ui in Qt Designer, make
changes, and compile them back into the Python class with:
```
pyside-uic litty/ui/settings.ui -o litty/ui/settings.py
```
.. then if you need additional code do that to SettingsWindow class in
litty/ui/windows.py.


### Building binaries

Install CX-Freeze from http://cx-freeze.sourceforge.net/
.. or you can install it using easy_install: easy_install cx_freeze


Then simply:

```
python setup.py build
```


On Windows you can also create an installer with:

```
python setup.py bdist_msi
```


### So what exactly DOES work, how do I test this?

Well, there IS a GUI that does pretty much absolutely nothing .. you can click
on things, etc., but nothing affects anything, and the settings are not saved.
You can write "example.com" to the host and click on connect. However, at this
point it will just freeze after that, because it can't read a password or use
any other means of authentication etc.

For non-GUI connections, you can pipe an SSH config to litty and it will connect
to the host defined in it as the "default".

The software currently only supports password authentication to servers, and only
if that password is defined in that SSH config piped to it, so to test the terminal
you will need to create a file similar to this:

```
Host default
  HostName www.example.com
  Port 22
  User example
  Password VerySecure1
```

Then run:
```
cat ssh_config | python litty.py
```

Or in Windows:
```
type ssh_config | python litty.py
```

What it then does is connect to the host and run in a loop the command "uptime"
this can be changed in litty/ui/windows.py .

At this moment there is NO shell for you to write stuff in.

### Troubleshooting

#### ValueError: Procedure probably called with too many arguments (12 bytes in excess)

If you get this error, try and close Pageant or other SSH agents. Dunno why it breaks, don't have time to investigate yet.

### Python 2, 3 or both?

My goal is both, but currently it seems to work only with 2.7. This is as I'm using
Paramiko (an SSH library) and I'm getting an error from it in Python 3. Could be
that it's just me, could be that it's been since fixed, I haven't really looked
into it that much yet.


# Financial support

This project has been made possible thanks to [Cocreators](https://cocreators.ee) and [Lietu](https://lietu.net). You can help us continue our open source work by supporting us on [Buy me a coffee](https://www.buymeacoffee.com/cocreators).

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cocreators)
