import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

def applyVrayMatToLayer(layer, matName):
    """
    applies vray mat to a layer
    input: layer, single layer name - matName: Vray mat string e.g. /glass_architectural
    returns: None
    """
    srf = rs.AddSphere([0,0,0], 1)
    rs.SelectObject(srf)
    rs.Command("-_visApplyMaterial "+matName)
    matIndex = rs.ObjectMaterialIndex(srf)
    rs.LayerMaterialIndex(layer, matIndex)
    rs.DeleteObject(srf)
    return None

def getMatTable():
    matTable = []
    i = 0
    for i in range(0, sc.doc.Materials.Count):
        matTable.append( sc.doc.Materials[i].Name)
    return matTable

def test():
    a =  Rhino.DocObjects.Tables.MaterialTable
    b =  sc.doc.Materials.Count
    Rhino.Geometry.Plane(
    c = Rhino.Geometry.Arc(
    print "yes"

def main():
    #layer = rs.GetLayer()
    matName = "/glass_architectural"
    #applyVrayMatToLayer(layer, matName)
    #print getMatTable()
    test()

if __name__ == "__main__":
    main()