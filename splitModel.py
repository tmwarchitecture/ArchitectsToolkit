import rhinoscriptsyntax as rs
import Rhino



def splitModel(objs, cutLevel):
    rs.EnableRedraw(False)
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
            rs.AddObjectToGroup(obj, "Above")
            print "Object Above"
        elif ptTop[2]<cutLevel:
            intersecting = False
            rs.AddObjectToGroup(obj, "Below")
            print "Object Below"
        else:
            intersecting = True
        
        if intersecting:
            if rs.IsSurface(obj):
                try:
                    copy = rs.CopyObject(obj)
                    splitSrfs = rs.SplitBrep(obj, circleSrf, True)
                    print len(splitSrfs)
                    for splitSrf in splitSrfs:
                        print "looping"
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
            
    rs.DeleteObject(belowDir)
    rs.DeleteObject(aboveDir)
    rs.DeleteObject(circle)
    rs.DeleteObject(circleSrf)
    rs.EnableRedraw(True)

def main():
    objs = rs.VisibleObjects()
    cutLevel = 20
    splitModel(objs, cutLevel)

main()