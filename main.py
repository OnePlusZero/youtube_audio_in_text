from logic.logiclang import start
from logic.logictube import lunk
from shutil import rmtree as rm
from os import remove as rmf


def st(pew):
    try:
        lunk(pew)
    except AttributeError:    
        start()
        s = "temporary-files"
        rm(s)
        d = 'output.wav'
        rmf(d)
    
