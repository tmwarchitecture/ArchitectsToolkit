import rhinoscriptsyntax as rs
import Rhino

objs = rs.VisibleObjects()

cutLevel = 3.5
point = Rhino.Geometry.Point3d(0,0,cutLevel)

belowDir = rs.AddLine(point, [0,0,-9999])
aboveDir = rs.AddLine(point, [0,0,9999])
circle = rs.AddCircle(point, 99)
circleSrf = rs.AddPlanarSrf(circle)

aboveGroup = rs.AddGroup("Above")
belowGroup = rs.AddGroup("Below")


for obj in objs:
    ptBtm = rs.BoundingBox(obj)[0]
    ptTop = rs.BoundingBox(obj)[6]
    if ptBtm[2]>cutLevel:
        intersecting = False
        rs.AddObjectToGroup(obj, aboveGroup)
        print "Object Above"
    elif ptTop[2]<cutLevel:
        intersecting = False
        rs.AddObjectToGroup(obj, belowGroup)
        print "Object Below"
    else:
        intersecting = True
    
    if intersecting:
        
        if rs.IsSurface(obj):
            try:
                splitSrfs = rs.SplitBrep(obj, circleSrf, True)
                for splitSrf in splitSrfs:
                    ptBtm = rs.BoundingBox(splitSrf)[0]
                    ptTop = rs.BoundingBox(splitSrf)[6]
                    mdPtZ = (ptBtm[2] + ptTop[2]) / 2
                    #if mdPtZ>cutLevel:
                        #rs.AddObjectToGroup(splitSrf, aboveGroup)
                    #else :
                        #rs.AddObjectToGroup(splitSrf, aboveGroup)
            except:
                None
        rs.DeleteObject(obj)
rs.DeleteObject(belowDir)
rs.DeleteObject(aboveDir)
rs.DeleteObject(circle)
rs.DeleteObject(circleSrf)
#        if rs.IsBrep(obj):
#            try:
#                cylinderAbove = rs.ExtrudeCurve(circle, aboveDir)
#                rs.CapPlanarHoles(cylinderAbove)
#                cylinderBelow = rs.ExtrudeCurve(circle, belowDir)
#                rs.CapPlanarHoles(cylinderBelow)
#                copy = rs.CopyObject(obj)
#                resultAbove = rs.BooleanDifference(obj , cylinderBelow, True)
#                resultBelow = rs.BooleanDifference(copy, cylinderAbove, True)
#                rs.DeleteObject(cylinderBelow)
#                rs.DeleteObject(cylinderAbove)
#                #rs.DeleteObject(obj)
#                print  "Object split"
#            except:
#                None