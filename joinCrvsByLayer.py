import rhinoscriptsyntax as rs
import scriptcontext
from scriptcontext import doc

def joinLayCrvs():

    origLayer = rs.CurrentLayer()
    #shortName = rs.LayerName(origLayer, fullpath = False)
    fullname = rs.LayerName(origLayer)
    
    objs = rs.ObjectsByLayer(fullname)
    curves = []
    for obj in objs:
        if (rs.IsCurve(obj)):
            curves.append(obj)
    if (len(curves)>1):
        rs.JoinCurves(curves, True)

def main():
    layersToCut = rs.GetLayers()
    rs.EnableRedraw(False)
    for layer in layersToCut:
        rs.CurrentLayer(layer)
        joinLayCrvs()
    rs.EnableRedraw(True)
    return None

main()