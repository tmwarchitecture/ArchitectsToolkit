import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
def matIndexByMatName(matName):
    rs.EnableRedraw(False)
    circle = rs.AddCircle([0,0,0],5)
    srf = rs.AddPlanarSrf(circle)
    #rs.ObjectMaterialIndex(srf, material_index =8)
    rs.SelectObject(srf)
    rs.Command("-_visApplyMaterial "+matName)
    matIndex = rs.ObjectMaterialIndex(srf)
    rs.DeleteObject(circle)
    rs.DeleteObject(srf)
    #obj = rs.coercerhinoobject(srf)
    #obj.Attributes.MaterialIndex = 8
    #print obj.Attributes.MaterialIndex
    rs.EnableRedraw(True)
    return matInd

material_Name = "/Grey-128 "

print matIndexByMatName(material_Name)

