import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

def distributeObjs():
    objs = rs.GetObjects()
    if objs is None:
        return
    rs.EnableRedraw(False)
    pts = []
    for obj in objs:
        pts.append(rs.BoundingBox(obj)[0])
    
    line = Rhino.Geometry.Line.TryFitLineToPoints(pts)[1]
    settingout = sc.doc.Objects.AddLine(line.From, line.To)
    sc.doc.Views.Redraw()
    t = []
    for i in range(0,len(pts)):
        t.append([i,(rs.CurveClosestPoint(settingout, pts[i]))])
    newItems = sorted(t, key=lambda tup: tup[1])
    sequence = []
    for newItem in newItems:
        sequence.append(newItem[0])
    
    rs.DeleteObject(settingout)
    
    #make distribute line
    for i in range(0,len(sequence)):
        if sequence[i] == 0:
            stPt = pts[i]
        if sequence[i] == len(sequence)-1:
            endPt = pts[i]
    divisionLine = rs.AddLine(stPt, endPt)
    
    #finalPts = list(reversed(rs.DivideCurve(divisionLine, len(objs)-1)))
    finalPts = rs.DivideCurve(divisionLine, len(objs)-1)
    
    for i in range(1, len(finalPts)-1):
        vec = rs.VectorCreate(finalPts[i], pts[sequence[i]])
        rs.MoveObject(objs[sequence[i]], vec)
    rs.DeleteObject(divisionLine)
    rs.EnableRedraw(True)

if __name__=="__main__":
    distributeObjs()    