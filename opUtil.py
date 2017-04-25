import rhinoscriptsyntax as rs

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
    #layer = rs.GetLayer()
    print getCurrentLayerOpNum()