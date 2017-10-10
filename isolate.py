import rhinoscriptsyntax as rs

def isolateLayerObjects():
    """
    Isolate a layers objects 
    input: None
    return: None
    """
    objs = rs.GetObjects("Select object on layer to isolate", preselect = True )
    if objs is None: return
    
    rs.EnableRedraw(False)
    layersToKeep = []
    for obj in objs:
        rs.SelectObjects(rs.ObjectsByLayer(rs.ObjectLayer(obj)))
    
    objs2keep = rs.InvertSelectedObjects()
    if objs2keep is None: return
    
    rs.HideObjects(objs2keep)
    rs.EnableRedraw(True)

def main():
    isolateLayerObjects()

if __name__ == "__main__":
    main()