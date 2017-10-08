import rhinoscriptsyntax as rs
import scriptcontext as sc

def docText2Text(pt, section, entry):
    string = section + "\\" + entry
    text = entry + ': %<documenttext("'+ str(string) +'")>%'
    tag = rs.AddText(text, pt, 1, justification = 1)
    
    te = rs.coercerhinoobject(tag, True, True)
    te.Geometry.TextFormula = text
    te.CommitChanges()
    sc.doc.Views.Redraw()

section = "Tim"
entry = "Key2a"
pt = rs.GetPoint()
docText2Text(pt, section, entry)