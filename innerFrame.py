import rhinoscriptsyntax as rs

def innerFrame():
    objs = rs.GetObjects("Select objects to add frame to", filter = 24, group = True,preselect = True)
    if objs is None:
        return
    
    dist = rs.GetReal("Offset Distance")
    if dist is None:
        return
    rs.EnableRedraw(False)
    
    srfs = []
    
    for obj in objs:
        if rs.IsPolysurface(obj):
            srfs = srfs + rs.ExplodePolysurfaces(obj)
        else:
            srfs.append(rs.CopyObject(obj))
    
    for srf in srfs:
        if rs.IsSurfacePlanar(srf):
            edgeCrvs = rs.DuplicateEdgeCurves(srf)
            border = rs.JoinCurves(edgeCrvs, True)
            innerEdge = rs.OffsetCurveOnSurface(border, srf, dist)
            rs.AddPlanarSrf([border, innerEdge])
            rs.DeleteObject(innerEdge)
            rs.DeleteObject(border)
        else:
            print "Surface is not planar"
    rs.DeleteObjects(srfs)
    rs.EnableRedraw(True)

if __name__=="__main__":
    innerFrame()
