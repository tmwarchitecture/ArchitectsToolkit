import rhinoscriptsyntax as rs
from setLevels import getFFL

def getMassAreas():
    layer = rs.GetLayer()
    objs = rs.ObjectsByLayer(layer)
    levels = getFFL()
    for obj in objs:
        if rs.IsPolysurfaceClosed(obj):
            for level in levels:
                circ = rs.AddCircle([0,0,float(level)+1], 1000)
                srf = rs.AddPlanarSrf(circ)
                
                rs.IntersectBreps(obj, srf[0])
                rs.DeleteObject(srf)
                rs.DeleteObject(circ)
    
    print levels
    
    return


getMassAreas()