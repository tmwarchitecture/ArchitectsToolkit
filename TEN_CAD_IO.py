import rhinoscriptsyntax as rs
import Rhino


def exportTEN_CAD():
    a = rs.GetObjects("Select Objects", preselect = "True")
    b = rs.ScaleObjects(a, [0,0,0], [1000,1000,0], copy=True)
    rs.UnitSystem(2)
    
    savePath0 = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
    savePath1 = '"'+savePath0+'"'
    rs.SelectObjects(b)
    rs.Command('_-Export '+savePath1+' _Enter')
    rs.DeleteObjects(b)
    rs.UnitSystem(4)
    print "Exported"
    return None

def importTEN_CAD():
    savePath0 = rs.OpenFileName("Open", "Autocad (*.dwg)|*.dwg||")
    savePath1 = '"'+savePath0+'"'
    rs.Command('_-Import '+savePath1+' _Enter')
    print "Import not added yet"
    return None

if __name__=="__main__":
    type = rs.GetInteger("", number = 0)
    if (type == 0):
        exportTEN_CAD()
    elif (type == 1):
        importTEN_CAD()