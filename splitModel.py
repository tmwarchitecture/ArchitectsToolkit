import rhinoscriptsyntax as rs
import Rhino

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

def main():
    objs = rs.VisibleObjects()
    cutLevel = 12
    rs.EnableRedraw(False)
    objsCopy = rs.CopyObjects(objs)
    splitModel(objsCopy, cutLevel)
    rs.EnableRedraw(True)

main()