import rhinoscriptsyntax as rs

def dimensionPline(pline, offsetDist):
    segments = []
    objLayer = rs.ObjectLayer(pline)
    objParent = rs.ParentLayer(objLayer)
    dimGroup = rs.AddGroup("Pline Dims")
    dimsLayer = rs.AddLayer("DIMS", parent = objParent, color = (100,100,100))
    segments = rs.ExplodeCurves(pline)
    for seg in segments:
        if rs.IsArc(seg):
            pass
        else:
            endPt = rs.CurveEndPoint(seg)
            stPt = rs.CurveStartPoint(seg)
            tanVec = rs.VectorCreate(stPt, endPt)
            offsetVec = rs.VectorRotate(tanVec, 90, [0,0,1])
            offsetVec = rs.VectorUnitize(offsetVec)
            offsetVec = rs.VectorScale(offsetVec, offsetDist)
            offsetPt = rs.VectorAdd(stPt, offsetVec)
            dim = rs.AddAlignedDimension(stPt, endPt, rs.coerce3dpoint(offsetPt))
            rs.ObjectLayer(dim, dimsLayer)
            rs.AddObjectToGroup(dim, dimGroup)
    rs.DeleteObjects(segments)
    return

def main():
    dist = 3
    objects = rs.GetObjects("Select Curves to Dimension", filter = 4, preselect = True)
    rs.EnableRedraw(False)
    if objects is None:
        return
    
    rs.CurrentDimStyle("10_Precision")
    
    for obj in objects:
        if rs.IsCurve(obj):
            dimensionPline(obj, dist)
        else:
            print "Not a polyline"
    rs.EnableRedraw(True)

main()    
