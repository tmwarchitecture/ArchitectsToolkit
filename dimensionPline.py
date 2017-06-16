import rhinoscriptsyntax as rs
import Rhino

def dimensionPline(pline, offsetDist):
    segments = []
    segments = rs.ExplodeCurves(pline)
    for seg in segments:
        endPt = rs.CurveEndPoint(seg)
        stPt = rs.CurveStartPoint(seg)
        tanVec = rs.VectorCreate(stPt, endPt)
        offsetVec = rs.VectorRotate(tanVec, 90, [0,0,1])
        offsetVec = rs.VectorUnitize(offsetVec)
        offsetVec = rs.VectorScale(offsetVec, offsetDist)
        offsetPt = rs.VectorAdd(stPt, offsetVec)
        dim = rs.AddAlignedDimension(stPt, endPt, rs.coerce3dpoint(offsetPt))
        root = rs.AddLayer("80_LAYOUT")
        dimsLayer = rs.AddLayer("DIMS", parent = root)
        rs.ObjectLayer(dim, dimsLayer)
    rs.DeleteObjects(segments)
    return

def main():
    dist = 2
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