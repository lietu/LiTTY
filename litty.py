 #!/usr/bin/python

from litty.litty import LiTTY
import sys


__doc__ = "Handles launching LiTTY"


if __name__ == "__main__":
    litty = LiTTY()

    if not sys.stdin.isatty():
        litty.parse_ssh_config(sys.stdin.read())

    litty.parse_args(sys.argv)

    litty.start()
