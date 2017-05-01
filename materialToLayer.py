import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

guids = rs.GetObjects('select objects')

for guid in guids:
    obj = rs.coercerhinoobject(guid)
    
    #This gets the layers material index
    objLay = rs.ObjectLayer(obj)
    a = rs.LayerMaterialIndex(objLay)
    
    #This gets the 'By Object' Material Index
    material_index = obj.Attributes.MaterialIndex
    
    #Get material name from index
    rhino_material = sc.doc.Materials[a] #<This is where you change the material to look up
    material_color = rhino_material.DiffuseColor
    material_name = rhino_material.Name
    
    print rhino_material.Name
    layer_index = sc.doc.Layers.Find(material_name, True)
    if layer_index >= 0:
        obj.Attributes.LayerIndex = layer_index
        obj.CommitChanges()
    else:
        new_layer_index = sc.doc.Layers.Add(material_name, material_color)
        obj.Attributes.LayerIndex = new_layer_index
        obj.CommitChanges()