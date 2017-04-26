import rhinoscriptsyntax as rs
import scriptcontext
from scriptcontext import doc
import setLevels


def cutAtPlan(level):
    planPlane = rs.AddPlaneSurface([-1000,-1000,level], 3000, 3000)
    baseLayer = rs.AddLayer("71_PLANS")
    newParent = rs.AddLayer("PLAN_"+str(level), parent = baseLayer)
    origLayer = rs.CurrentLayer()
    shortName = rs.LayerName(origLayer, fullpath = False)
    
    #newChildsParent = rs.AddLayer( , parent = newParent)
    newChild = rs.AddLayer(shortName, parent = newParent, color = rs.LayerColor(origLayer))
    rs.CurrentLayer(newChild)
    
    objs = rs.ObjectsByLayer(origLayer)
    #if len(objs)<1:
    #    skip = True
    intersectCrvs = []
    tempCrv = None
    for obj in objs:
        if rs.IsBrep(obj):
            
            tempCrv = rs.IntersectBreps(obj, planPlane)
        if tempCrv != None:
            intersectCrvs.append(tempCrv)
    
    for crv in intersectCrvs:
        if not None:
            rs.ObjectLayer(crv, newChild)
    
    rs.DeleteObject(planPlane)
    rs.CurrentLayer(origLayer)

def main():
    levelsElev = setLevels.getFloorLevels()
    #levelsElev = [0.0,6.0,11.50,17.00,22.50,28.00]
    heights = []
    for leveli in levelsElev:
        heights.append(leveli+1)
    #heights = [12.50]
    layersToCut = rs.GetLayers()
    rs.EnableRedraw(False)
    for height in heights:
        for layer in layersToCut:
            rs.CurrentLayer(layer)
            cutAtPlan(height)
    rs.EnableRedraw(True)
    return None

main()