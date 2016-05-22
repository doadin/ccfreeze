version = "1.1.5"

import sys
from ccfreeze import modulegraph
sys.modules['modulegraph'] = modulegraph

from ccfreeze.freezer import Freezer

version = "1.1.4"


def main():
    scripts = sys.argv[1:]
    if not scripts:
        print("Version: %s (Python %s)" % (version, ".".join([str(x) for x in sys.version_info])))
        print("Usage: ccfreeze SCRIPT1 [SCRIPT2...]")
        print("   creates standalone executables from python scripts SCRIPT1,...")
        print()

        sys.exit(0)

    f = Freezer()
    for x in scripts:
        f.addScript(x)
    f()
