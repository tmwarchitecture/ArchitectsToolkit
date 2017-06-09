import rhinoscriptsyntax as rs
import scriptcontext
from scriptcontext import doc
import setLevels


def cutAtPlan(level, floorNum):
    planPlane = rs.AddPlaneSurface([-1000,-1000,level], 3000, 3000)
    baseLayer = rs.AddLayer("60_PLANS")
    newParent = rs.AddLayer("Level_"+floorNum, parent = baseLayer)
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
            #rs.SetUserText(crv, "PlanID", "PLAN")
    
    rs.DeleteObject(planPlane)
    rs.CurrentLayer(origLayer)
def deleteExistingPlans():
    if rs.IsLayer("60_PLANS"):
        #delete all sublayers
        levelLayers = rs.LayerChildren("60_PLANS")
        for levelLayer in levelLayers:
            childLayers = rs.LayerChildren(levelLayer)
            for childLayer in childLayers:
                objects = rs.ObjectsByLayer(childLayer)
                rs.DeleteObjects(objects)
                rs.DeleteLayer(childLayer)
            rs.DeleteLayer(levelLayer)
    else:
        return    
def main():
    heightRel2FFL = rs.GetReal("Cut level (relative to FFL):", number = 1)
    levelsElev = setLevels.getFloorLevels()
    rs.EnableRedraw(False)
    deleteExistingPlans()
    heights = []
    
    for leveli in levelsElev:
        heights.append(leveli+heightRel2FFL)
    layers = rs.GetLayers()
    if layers is None:
        return
    layersToCut = []
    for layer in layers:
        if rs.LayerVisible(layer):
            layersToCut.append(layer)
    for i in range(0,len(heights)):
        for layer in layersToCut:
            rs.CurrentLayer(layer)
            if i<9:
                levelNum = "0"+str(i+1)
            else:
                levelNum = str(i+1)
            cutAtPlan(heights[i], levelNum)
    rs.EnableRedraw(True)
    return None

main()
