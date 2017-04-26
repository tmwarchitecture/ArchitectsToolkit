import rhinoscriptsyntax as rs
import scriptcontext
import Rhino

def getLevelFromPt(pt):
    """
    Returns the Z of a pt.
    input: point
    returns: float
    """
    level = pt[2]
    return level

def getPlanIntersection(layers, level):
    rs.EnableRedraw(False)
    
    #Initiate list
    interCrvs = []
    
    #store origlayer for end
    origLayer = rs.CurrentLayer()
    
    #create the intersection surface
    circle = rs.AddCircle([0,0,level],1000)
    plane = rs.AddPlanarSrf(circle)
    
    #layer to assign intersections to
    newLayer = rs.AddLayer("CRVS")
    
    for layer in layers:
        
        #get all objects on layer
        rs.CurrentLayer(layer)
        objs = rs.ObjectsByLayer(rs.CurrentLayer())
        
        #for each object, intersect with surface
        for obj in objs:
            if rs.IsBrep(obj):
                interCrvs.append(rs.IntersectBreps(obj, plane))
        
        #change intersection crvs layer
        for crv in interCrvs:
            if crv is not None:
                rs.ObjectLayer(crv, newLayer)
    
    #Cleanup
    rs.DeleteObject(circle)
    rs.DeleteObject(plane)
    rs.CurrentLayer(origLayer)
    
    rs.EnableRedraw(True)
    return "Success"

if __name__=="__main__":
    
    #Assign layers to intersect
    layers2Inter = rs.LayerNames()
    
    #get elevation of the cut
    pt = rs.GetPoint("Select Pt")
    z = getLevelFromPt(pt)
    print "Level cutting at +{}m".format(z)
    
    #cut layers
    print getPlanIntersection(layers2Inter, z)