#! /usr/bin/env python

import os
import sys

print sys.getfilesystemencoding(), os.environ.get("LANG", "<>")
