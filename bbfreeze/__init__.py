version = "1.1.4"

import sys
from bbfreeze import modulegraph
sys.modules['modulegraph'] = modulegraph

from bbfreeze.freezer import Freezer

version = "1.1.4"


def main():
    scripts = sys.argv[1:]
    if not scripts:
        print "Version: %s (Python %s)" % (version)
        print "Usage: bbfreeze SCRIPT1 [SCRIPT2...]"
        print "   creates standalone executables from python scripts SCRIPT1,..."
        print

        sys.exit(0)

    f = Freezer()
    for x in scripts:
        f.addScript(x)
    f()
