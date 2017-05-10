"""
Sets or Gets current option number to document data

input: route(pline), width (num), height(num)
returns: 1 Solid Brep
"""

__author__ = 'Tim Williams'


import rhinoscriptsyntax as rs

#Updated
def getCurOp():
   #curOption 0 means not currently in an option layer structure.
    curLayer = rs.CurrentLayer()
    root = str(curLayer.split("::")[0])
    if len(curLayer.split("::"))>1:
        if (root == "30_AR" or root == "20_MASS" or root == "40_LANDSCAPE"):
            print "in the {} root".format(root)
            opName = str(curLayer.split("::")[1])
            try:
                opNum = int(opName.split("_")[1])
                if str(opName.split("_")[0]) == "OP": 
                    print "and OP number {}".format(opNum)
                    curOption = opNum
                else:
                    print ",but NOT under an OP layer."
                    curOption = 0
            except:
                print ",but NOT under an OP layer."
                curOption = 0
        else: 
            print "Not in ROOT"
    else:
        curOption = 0
    return curOption

def setCurOp(newOpNum):
    #sets current option integer to document data from user input
    OpInt = newOpNum
    rs.SetDocumentData("10_DATA", "OpNum", str(OpInt))
    return None

#updating
def iterateOp():
    curLayer = rs.CurrentLayer()
    root = str(curLayer.split("::")[0])
    if getCurOp() == 0: #if not in Cur Op
        newOpNum = 1
        items = ["20_MASS", "30_AR", "40_LANDSCAPE"]
        newParent = rs.ComboListBox(items, "Select layer to add new option to:", "Add Option")
        root = rs.AddLayer(newParent)
    else:
        rootKids = rs.LayerChildren(root)
        allOpts = []
        for lay in rootKids:
            allOpts.append(lay.split("::")[1])
        integers = []
        for name in allOpts:
            nameList = name.split("_")
            if len(nameList)>1:
                integers.append(int(nameList[1]))
        integers.sort()
        newOpNum = integers[-1]+1
    if (len(str(newOpNum))>1):
        newOptName = "OP_"+str(newOpNum)
    else:
        newOptName = "OP_0"+str(newOpNum)
    newLayer = rs.AddLayer(newOptName, parent = root)
    rs.CurrentLayer(newLayer)
    return newOpNum

def getLayerOpNum (layer):
    """
    Get a layers parent option number
    
    input: full name string of layer
    return: int of the option number
    """
    if layer is None:   return None
    
    a = layer.split("::")
    if len(a)>1:
        b = a[1].split("_")
        if b[0] == "OP":
            opNum = b[1]
            return int(opNum)
        else:
            print "Layer not a child of an option."
            return None
    else: 
        print "This is the root layer"
        return None

def getCurrentLayerOpNum ():
    """
    Get a layers parent option number
    
    input: full name string of layer
    return: int of the option number
    """
    layer = rs.CurrentLayer()
    curOpNum = getLayerOpNum(layer)
    if curOpNum > 0:
        return curOpNum
    else:
        newOpNum = rs.RealBox("Add layers to option number:", default_number=1, title = "Option Number", minimum = 1, maximum = 99)
        #newOpNum = rs.GetInteger("Add layers to option number:", number = 1, minimum = 1)
        return newOpNum
def selObjByUserTextVal(objs, val):
    """
    get objects from a list that have a UserText matching the value specified(val)
    
    input: list of objs (objs), value to find (int)
    returns: list of matching objs
    """
    matchingObjs = []
    for obj in objs:
        if (int(rs.GetUserText(obj, "Number"))==val):
            matchingObjs.append(obj)
    return matchingObjs


if __name__=="__main__":
    #curveId = rs.GetObject("pick up your curve", 4)
    #settings = ["optionA", "DefaultSettingA", "customSettingA"], ["optionB", "DefaultSettingB", "customSettingB"], ["optionC", "DefaultSettingC", "customSettingC"], ["optionD", "DefaultSettingD", "customSettingD"]
    #pickedAttributes = rs.GetBoolean("choose curve's attributes", settings, [True, True, True, True])
    #for patt in pickedAttributes:
    #    print patt
    #setCurOp()
    print getCurOp()
    print iterateOp()