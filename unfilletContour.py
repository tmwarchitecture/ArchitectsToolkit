import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
import scriptcontext as sc


def unfilletContour(obj, pt):
    rs.EnableRedraw(False)
    cir = rs.AddCircle(pt, 10000)
    cirSrf = rs.AddPlanarSrf(cir)
    
    curLay = rs.CurrentLayer()
    childrenLay = rs.LayerChildren(curLay)
    cutCrvs = []
    contours = []
    finalLines = []
    finalLineSegs = []
    #for lay in childrenLay:
    #    objs = rs.ObjectsByLayer(lay)
    #for obj in objs:
    tempCrv = rs.IntersectBreps(obj, cirSrf)
    if tempCrv is not None:
        cutCrvs.append(tempCrv)
    
    for crv in cutCrvs:
        contours.append(ghcomp.Explode(crv, True)[0])
    
    for contour in contours:
        for i in range(0, len(contour)):
            if rs.IsLine(contour[i]):
                finalLines.append(sc.doc.Objects.AddCurve(contour[i]))
                #print "A line!"
    finalPts = []
    for line in finalLines:
        rs.ExtendCurveLength(line, 0, 2, 30)
    for i in range(0,len(finalLines)-1):
        tempPt = rs.CurveCurveIntersection(finalLines[i], finalLines[i+1])
        finalPts.append(rs.AddPoint(rs.coerce3dpoint(tempPt[0][1])))
    tempPt = rs.CurveCurveIntersection(finalLines[-1], finalLines[0])
    finalPts.append(rs.AddPoint(rs.coerce3dpoint(tempPt[0][1])))
    for i in range(0, len(finalPts)-1):
        finalLineSegs.append(rs.AddLine(finalPts[i], finalPts[i+1]))
    finalLineSegs.append(rs.AddLine(finalPts[-1], finalPts[0]))
    lastCrv = rs.JoinCurves(finalLineSegs, True)
    newSrf = rs.AddPlanarSrf(lastCrv)
    sc.doc.Views.Redraw()
    
    rs.DeleteObjects(finalPts)
    rs.DeleteObjects(finalLines)
    rs.DeleteObject(tempCrv)
    rs.DeleteObject(lastCrv)
    rs.DeleteObjects(cutCrvs)
    rs.DeleteObject(cir)
    rs.DeleteObject(cirSrf)
    rs.EnableRedraw(True)
    
    rs.SelectObject(newSrf)

obj = rs.GetObject("Select objects")
pt = rs.GetPoint()
unfilletContour(obj, pt)
