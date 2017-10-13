import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def areaTag(pline):
    #get area
    area = rs.CurveArea(pline)[0]
    area = str((int(area*100))/100) + "m2"
    print area
    
    
    #move area tag below name tag location
    offset = [0,-2.5,0]
    
    
    
    #add text tag
    objID = pline
    text = '%<area("'+ str(objID) +'")>%m2'
    
    pt = rs.AddPoint(rs.CurveAreaCentroid(pline)[0])
    rs.MoveObject(pt, offset)
    areaTag = rs.AddText(text, pt, 1, justification = 131074)
    rs.DeleteObject(pt)
    
    parentLayer = rs.ParentLayer(rs.ObjectLayer(pline))
    hostLayer = rs.AddLayer("ANNO_AREA", (128,128,128), parent = parentLayer)
    rs.ObjectLayer(areaTag, hostLayer)
    
    
    te = rs.coercerhinoobject(areaTag, True, True)
    te.Geometry.TextFormula = text
    te.CommitChanges()
    sc.doc.Views.Redraw()
    return None

def main():
    pline = rs.GetObjects("Select curves to add area tag", preselect = True)
    if pline is None:
        return None
    #rs.EnableRedraw(False)
    for i in range(0, len(pline)):
        areaTag(pline[i])
    #rs.EnableRedraw(True)
if __name__=="__main__":
    main()
