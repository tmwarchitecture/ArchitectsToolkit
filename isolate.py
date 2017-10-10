import rhinoscriptsyntax as rs

def isolateLayerObjects():
    """
    Isolate a layers objects 
    input: None
    return: None
    """
    obj = rs.GetObject("Select object on layer to isolate")
    if obj is None: return
    
    rs.EnableRedraw(False)
    layer = rs.ObjectLayer(obj)
    
    objects = rs.ObjectsByLayer(layer)
    
    rs.SelectObjects(objects)
    
    objs2keep = rs.InvertSelectedObjects()
    if objs2keep is None: return
    
    rs.HideObjects(objs2keep)
    rs.EnableRedraw(True)

def main():
    isolateLayerObjects()

if __name__ == "__main__":
    main()