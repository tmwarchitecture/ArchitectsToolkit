"""Duplicates a layer and all its sublayers incuding objects
Script by Mitch Heynick 20 April 2014"""

import rhinoscriptsyntax as rs
import scriptcontext as sc

def CopyObjectsToLayer(objs,layer):
    copies=rs.CopyObjects(objs)
    rs.ObjectLayer(copies,layer)

def UniqueLayerCopyName(layer,top):
    #Extract main level name; add - Copy to top level layer name only
    layers=rs.LayerNames()
    nameList=layer.split("::")
    newName=nameList[-1]
    
    rawName = rs.LayerName(layer, False)
    try:
        newNum = int(rawName.split("_")[-1]) + 1
    except:
        newNum = rawName
    if newNum <10:
        newNum = "0" + str(newNum)
    layerName = rawName.split("_")[0] + "_" + str(newNum)
    
    if top: newName = layerName
    if newName in layers:
        i=0
        while True:
            i+=1
            testName=newName+"({})".format(i)
            if not testName in layers: return testName
    return newName
    
def DupAllSubLayers(layer,layerCopy):
    subs=rs.LayerChildren(layer)
    if subs:
        for sub in subs:
            color=rs.LayerColor(sub)
            objs=rs.ObjectsByLayer(sub)
            name=UniqueLayerCopyName(sub,False)
            addLayer=rs.AddLayer(name,color,parent=layerCopy)
            CopyObjectsToLayer(objs,addLayer)
            rs.ExpandLayer(addLayer,rs.IsLayerExpanded(sub))
            DupAllSubLayers(sub,addLayer)

def DupLayersSublayersAndObjs():
    layer=rs.GetLayer()
    if layer==None: return
    #do initial run with selected layer
    color=rs.LayerColor(layer)
    objs=rs.ObjectsByLayer(layer)
    parentLayer=rs.ParentLayer(layer)
    
    
    copyName=UniqueLayerCopyName(layer,True)
    layerCopy=rs.AddLayer(copyName,color,parent=parentLayer)    
    CopyObjectsToLayer(objs,layerCopy)
    rs.ExpandLayer(layerCopy,rs.IsLayerExpanded(layer))
    DupAllSubLayers(layer,layerCopy)
    rs.CurrentLayer(layerCopy)

DupLayersSublayersAndObjs()