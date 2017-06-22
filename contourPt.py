import rhinoscriptsyntax as rs


def contourPt(obj, pt):
    planPlane = rs.AddPlaneSurface([-1000,-1000,pt[2]], 3000, 3000)
    intersectCrvs = []
    tempCrv = None
    
    if rs.IsBrep(obj):
        tempCrv = rs.IntersectBreps(obj, planPlane)
    if tempCrv != None:
        objName = rs.ObjectName(obj)
        rs.ObjectName(tempCrv, objName)
        intersectCrvs.append(tempCrv)
    rs.DeleteObject(planPlane)

def main():
    objs = rs.GetObjects("Select objects to contour", preselect = True)
    if objs is None: return
    pt = rs.GetPoint("Select point to contour at")
    if objs is None: return
    rs.EnableRedraw(False)
    for obj in objs:
        contourPt(obj, pt)
    rs.EnableRedraw(True)

if __name__ == "__main__":
    main()