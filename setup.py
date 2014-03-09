from cx_Freeze import setup, Executable


build_exe_options = {}

setup(
    name="litty",
    version="0.1",
    description="LiTTY - Lietu's TTY",
    options={"build_exe": build_exe_options},
    executables=[Executable("litty.py")]
)
