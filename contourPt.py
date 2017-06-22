import rhinoscriptsyntax as rs


def contourPt(obj, pt):
    """
    creates a contour according to xy plane at specified height
    obj: single object to contour
    pt: a point to contour at
    """
    planPlane = rs.AddPlaneSurface([-10000,-10000,pt[2]], 30000, 30000)
    intersectCrvs = []
    tempCrv = None
    
    if rs.IsBrep(obj):
        tempCrv = rs.IntersectBreps(obj, planPlane)
    if tempCrv != None:
        objName = rs.ObjectName(obj)
        rs.ObjectName(tempCrv, objName)
        intersectCrvs.append(tempCrv)
        rs.MatchObjectAttributes(tempCrv, obj)
    rs.DeleteObject(planPlane)
    return intersectCrvs

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