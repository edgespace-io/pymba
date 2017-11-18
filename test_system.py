from pymba import *

with Vimba() as vimba:
    # get system object
    system = vimba.getSystem()
    
    # list system features
    for featureName in system.getFeatureNames():
        print(featureName)


