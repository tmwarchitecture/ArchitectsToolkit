import rhinoscriptsyntax as rs
import joinCrvsByLayer as jc

def make2dByLayer(layer):
    objs = rs.ObjectsByLayer(layer)
    if objs is None: 
        return
    #Make2d
    
    rs.SelectObjects(objs)
    rs.Command("-_make2d _D _U _Enter")
    projLines = rs.GetObjects("Press escape", preselect = True)
    finalCrvs = rs.JoinCurves(projLines)
    rs.DeleteObjects(projLines)
    rs.MatchObjectAttributes(finalCrvs, objs[0])
    return finalCrvs

def main():
    layers = rs.GetLayers()
    for layer in layers:
        make2dByLayer(layer)

if __name__ ==  "__main__":
    main()