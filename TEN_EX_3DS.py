import rhinoscriptsyntax as rs

def ex3DS(objs):
    rs.MessageBox("Remember to check backfaces!")
    if objs is None:
        return
    rs.SelectObjects(objs)
    savePath = rs.SaveFileName("Save", "Autocad (*.dwg)|*.dwg||")
    rs.Command('! _-Export ' + str(savePath) + ' _Scheme _to3DSMax _Enter _Enter')
    print "Exported to {}".format(str(savePath))

objs = rs.GetObjects("Select Objects")
ex3DS(objs)