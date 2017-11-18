from pymba import *

try:
    with Vimba() as vimba:
except VimbaException as e:
    print(e.message)

