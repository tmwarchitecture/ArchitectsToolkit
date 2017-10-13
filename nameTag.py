import rhinoscriptsyntax as rs

def nameTag(obj):
    roomName = rs.ObjectName(obj)
    
    try:
        text = str(roomName)
        pt0 = rs.BoundingBox(obj)[0]
        pt2 = rs.BoundingBox(obj)[2]
        pt = rs.PointDivide(rs.PointAdd(pt0, pt2), 2)
        areaTag = rs.AddText(text, pt, 1, justification = 131074)
    except:
        print "Object has no name"
        return
    
    parentLayer = rs.ParentLayer(rs.ObjectLayer(obj))
    hostLayer = rs.AddLayer("ANNO_NAME", (128,128,128), parent = parentLayer)
    rs.ObjectLayer(areaTag, hostLayer)
    return None

def main():
    pline = rs.GetObjects("Select Objects to add name tag to", preselect = True)
    if pline is None:
        return None
    rs.EnableRedraw(False)
    for i in range(0, len(pline)):
        nameTag(pline[i])
    rs.EnableRedraw(True)
if __name__=="__main__":
    main()
