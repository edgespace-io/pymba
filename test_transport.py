from pymba import *

with Vimba() as vimba:
    # get list of available interfaces
    interfaceIds = vimba.getInterfaceIds()
    for interfaceId in interfaceIds:
        print(interfaceId)
    
    # get interface object and open it
    interface0 = vimba.getInterface(interfaceIds[0])
    interface0.openInterface()
    
    # list interface features
    interfaceFeatureNames = interface0.getFeatureNames()
    for name in interfaceFeatureNames:
        print(name)
    
    # close interface
    interface0.closeInterface()

