import rhinoscriptsyntax as rs
import os

def addComponent():
    libPath = 'C:\\Users\\Tim\\Desktop\\temp\\library'
    rhinoFiles = []
    
    items = os.listdir(libPath)
    
    if items is None:
        print "Library is empty or path is wrong"
        return
    
    for item in items:
        parts = item.split(".")
        if len(parts)==2:
            if parts[1]=="3dm":
                rhinoFiles.append(parts[0])
    
    choice = rs.ComboListBox(rhinoFiles, "Select Components to add", "add Component")
    if choice is None:
        return
    choiceFile = choice+".3dm"
    rs.EnableRedraw(False)
    rs.Command('-_NoEcho _-Import '+libPath+"\\"+choiceFile+' Objects Enter -_SelLast Enter')
    importedGeo = rs.GetObjects(preselect = True)
    rs.ObjectLayer(importedGeo, rs.CurrentLayer())
    rs.SelectObjects(importedGeo)
    rs.EnableRedraw(True)

if __name__=="__main__":
    addComponent()