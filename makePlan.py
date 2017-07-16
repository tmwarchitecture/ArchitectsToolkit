import rhinoscriptsyntax as rs
import Rhino

def flatten(crvs):
    planPlane = rs.AddPlaneSurface([-1000,-1000,0], 3000, 3000)
    
    #projectedCrvs = rs.ProjectCurveToSurface(crvs, planPlane, [0,0,-1])
    projectedCrvs = []
    
    for crv in crvs:
        explodedCrvs = rs.ExplodeCurves(crv)
        if explodedCrvs:
            for explodedCrv in explodedCrvs:
                tempCrv = rs.ProjectCurveToSurface(explodedCrv, planPlane, [0,0,-1])
                rs.DeleteObject(explodedCrv)
                rs.MatchObjectAttributes(tempCrv, crv)
                projectedCrvs.append(tempCrv)
            rs.DeleteObject(crv)
        else:
            tempCrv = rs.ProjectCurveToSurface(crv, planPlane, [0,0,-1])
            rs.MatchObjectAttributes(tempCrv, crv)
            rs.DeleteObjects(crv)
            projectedCrvs.append(tempCrv)
        
    rs.DeleteObject(planPlane)
    
    return projectedCrvs

def splitModel(objs, cutLevel):
    point = Rhino.Geometry.Point3d(0,0,cutLevel)
    
    belowDir = rs.AddLine(point, [0,0,-9999])
    aboveDir = rs.AddLine(point, [0,0,9999])
    circle = rs.AddCircle(point, 9999)
    circleSrf = rs.AddPlanarSrf(circle)
    
    aboveGroup = rs.AddGroup("Above")
    belowGroup = rs.AddGroup("Below")
    
    
    for obj in objs:
        ptBtm = rs.BoundingBox(obj)[0]
        ptTop = rs.BoundingBox(obj)[6]
        if ptBtm[2]>cutLevel:
            intersecting = False
            rs.AddObjectToGroup(obj, "Above")
            #print "Object Above"
        elif ptTop[2]<cutLevel:
            intersecting = False
            rs.AddObjectToGroup(obj, "Below")
            #print "Object Below"
        else:
            intersecting = True
        
        if intersecting:
            if rs.IsBrep(obj):
                closed = False
                if rs.IsPolysurfaceClosed(obj):
                    closed = True
                try:
                    copy = rs.CopyObject(obj)
                    splitSrfs = rs.SplitBrep(obj, circleSrf, True)
                    for splitSrf in splitSrfs:
                        #print "looping"
                        if closed:
                            rs.CapPlanarHoles(splitSrf)
                        rs.MatchObjectAttributes(splitSrf, copy)
                        ptBtm = rs.BoundingBox(splitSrf)[0]
                        ptTop = rs.BoundingBox(splitSrf)[6]
                        mdPtZ = (ptBtm[2] + ptTop[2]) / 2
                        if mdPtZ>cutLevel:
                            rs.AddObjectToGroup(splitSrf, "Above")
                        else:
                            rs.AddObjectToGroup(splitSrf, "Below")
                    rs.DeleteObject(copy)
                    rs.DeleteObject(obj)
                except:
                    None
            if rs.IsBlockInstance(obj):
                contents = rs.ExplodeBlockInstance(obj)
                for content in contents:
                    objs.append(content)
    rs.DeleteObject(belowDir)
    rs.DeleteObject(aboveDir)
    rs.DeleteObject(circle)
    rs.DeleteObject(circleSrf)

def makePlan():
    """
    make2d from above.
    input: list of layers to make2d
    returns: None
    """
    objs = rs.ObjectsByGroup("Below")
    
    #Make2d
    rs.SelectObjects(objs)
    rs.Command("-_make2d _D _U _Enter")
    projLines = rs.GetObjects("", preselect = True)
    
    #Get make2d root layer
    make2dRootRaw = rs.ObjectLayer(projLines[0])
    make2dRoot = make2dRootRaw.split("::")[0]
    
    #Rename make2d layers
    root  = rs.AddLayer("60_PLANS")
    roofLay = rs.AddLayer("Roof", parent = root)
    for projLine in projLines:
        linesLayer = rs.ObjectLayer(projLine)
        linesColor = rs.ObjectColor(projLine)
        linesLayerName = rs.LayerName(linesLayer, fullpath = False)
        newLayers = rs.AddLayer(linesLayerName, parent = roofLay, color = linesColor)
        rs.ObjectLayer(projLine,newLayers)
        rs.ObjectColor(projLine, (200,200,200))
    
    #Delete make2d Layers
    rs.DeleteLayer(make2dRoot)
    return

def cutAtPlan(level, join):
    cutPlane = rs.AddPlaneSurface([-1000,-1000,level], 3000, 3000)
    plane = rs.PlaneFromNormal([-1000,-1000,0], [0,0,1])
    planPlane = rs.AddPlaneSurface(plane, 3000, 3000)
    
    objs = rs.VisibleObjects()
    intersectCrvs = []
    tempCrv = None
    for obj in objs:
        if rs.IsBrep(obj):
            tempCrv = rs.IntersectBreps(obj, cutPlane)
        if tempCrv:
            rs.MatchObjectAttributes(tempCrv, obj)
            newCrvs = flatten(tempCrv)
    rs.DeleteObject(cutPlane)
    rs.DeleteObject(planPlane)

def main():
    objs = rs.VisibleObjects()
    cutLevel = 12
    rs.EnableRedraw(False)
    objsCopy = rs.CopyObjects(objs)
    splitModel(objsCopy, cutLevel)
    makePlan()
    rs.DeleteObjects(rs.ObjectsByGroup("Above"))
    rs.DeleteObjects(rs.ObjectsByGroup("Below"))
    cutAtPlan(cutLevel, False)
    rs.Command('_SelDupAll _delete')
    cutAtPlan(cutLevel, True)
    rs.Command('_SelDup _delete')
    rs.EnableRedraw(True)

main()