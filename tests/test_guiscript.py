#! /usr/bin/env py.test
try:
    import win32ui
except:
    win32ui = None

import os

import ccfreeze

if win32ui:
    def test_guiscript():
        f = ccfreeze.Freezer()
        f.addScript("ex-mbox.py", True)
        f()
        err = os.system("dist\\ex-mbox")
        assert err == 0


def test_guiscript2():
    f = ccfreeze.Freezer()
    f.addScript("hello-world.py", True)
    f()

    cmd = os.path.join("dist", "hello-world")
    err = os.system(cmd)

    assert err == 0
