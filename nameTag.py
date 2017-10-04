import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
def nameTag(pline):
    #get area
    #area = rs.CurveArea(pline)[0]
    #area = str((int(area*100))/100) + "/2 = " + str(((int(area*100))/100)/2)
    #area = str((int(area*100))/100) + "m2"
    #print area
    
    roomName = rs.ObjectName(pline)
    #add hatch
    #hatch = rs.AddHatch(pline)
    #rs.ObjectColor(hatch, color = [100,100,100])
    
    #add text tag
    #objID = pline
    try:
        text = str(roomName)
        pt = rs.AddPoint(rs.CurveAreaCentroid(pline)[0])
        areaTag = rs.AddText(text, pt, 1, justification = 131074)
    except:
        print "Object has no name"
    #areaTag = rs.AddTextDot(area, pt)
    rs.DeleteObject(pt)
    
    parentLayer = rs.ParentLayer(rs.ObjectLayer(pline))
    hostLayer = rs.AddLayer("ANNO_NAME", (128,128,128), parent = parentLayer)
    rs.ObjectLayer(areaTag, hostLayer)
    
    #te = rs.coercerhinoobject(id, True, True)
    #te.Geometry.TextFormula = text
    #te.CommitChanges()
    #sc.doc.Views.Redraw()
    return None

def main():
    pline = rs.GetObjects("Select Curve", preselect = True)
    if pline is None:
        return None
    rs.EnableRedraw(False)
    for i in range(0, len(pline)):
        nameTag(pline[i])
    rs.EnableRedraw(True)
if __name__=="__main__":
    main()
