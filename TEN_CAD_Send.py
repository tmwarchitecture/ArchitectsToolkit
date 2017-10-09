import rhinoscriptsyntax as rs

def send2CAD(objs, newCoord, CADinMeters):
    transVec = rs.VectorScale(newCoord, .001)
    newObjs = rs.CopyObjects(objs, transVec)
    
    if CADinMeters:
        rs.ScaleObjects(newObjs, [0,0,0], [.001,.001,.001])
        print  "scaled"
    
    rs.SelectObjects(newObjs)
    
    loc = " D:\\temp.dwg"
    
    rs.Command('_-Export '+loc+' _Enter')
    
    rs.DeleteObjects(newObjs)
    print "Sent"
    return None

def main():
    objs = rs.GetObjects("Select Objects to Send to CAD", preselect = True)
    if objs is None:
        return
    items = [ ["Units", "Millimeters", "Meters"] ]
    defaults = [False]
    CADinMeters = rs.GetBoolean("Autocad DWG units", items, defaults)[0]
    if CADinMeters is None:
        return
    coordRaw = rs.GetDocumentData("Project Info", "CAD coordinate (mm)")
    if len(coordRaw) == 0:
        print "You have not specified a CAD Coordinate. Sending to 0,0,0."
        coord = [0,0,0]
    else:
        coord = coordRaw.split(',')
    send2CAD(objs, coord, CADinMeters)

main()