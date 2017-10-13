import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def layerTag(obj):
    
    roomName = rs.LayerName(rs.ObjectLayer(obj), False)
    #add text tag
    try:
        text = str(roomName)
        pt0 = rs.BoundingBox(obj)[0]
        pt2 = rs.BoundingBox(obj)[2]
        pt = rs.AddPoint(rs.PointDivide(rs.PointAdd(pt0, pt2), 2))
        rs.MoveObject(pt, [0,1.5,0])
        areaTag = rs.AddText(text, pt, 1, justification = 131074)
    except:
        print "Object has no name"
        return
    rs.DeleteObject(pt)
    parentLayer = rs.ParentLayer(rs.ObjectLayer(obj))
    hostLayer = rs.AddLayer("ANNO_LAYER", (128,128,128), parent = parentLayer)
    rs.ObjectLayer(areaTag, hostLayer)
    
    #te = rs.coercerhinoobject(id, True, True)
    #te.Geometry.TextFormula = text
    #te.CommitChanges()
    #sc.doc.Views.Redraw()
    return None

def main():
    pline = rs.GetObjects("Select object to add layer tag to", preselect = True)
    if pline is None:
        return None
    rs.EnableRedraw(False)
    for i in range(0, len(pline)):
        layerTag(pline[i])
    rs.EnableRedraw(True)
if __name__=="__main__":
    main()
