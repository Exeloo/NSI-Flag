import sys
import os
import json
from io import StringIO
from importlib import import_module
import Main

def getFlag (name) :
    try :
        m = __import__ ("Flags." + name, fromlist=[name])
        flag = getattr(m, name)
        return flag()
    except :
        print(sys.exc_info()[0])
        return False

def getFlagList() :
    contryList = os.listdir("Flags")
    contryList.remove('__pycache__')
    return json.dumps([ str(i).replace('.py', '').replace('Armenie', 'Arménie') for i in contryList])

def getDefaultFlag() : 
    return getFlag("France")
    # return Main.getDefaultFlag()

def getIcon() :
    return getFlag("France")
    # return Main.getDefaultFlag()