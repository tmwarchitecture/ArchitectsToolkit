import rhinoscriptsyntax as rs
import os

def getComponent():
    libPath = 'C:\\Users\\Tim\\Desktop\\temp\\library'
    items = os.listdir(libPath)
    choice = rs.ComboListBox(items)
    if choice is None:
        return
    rs.Command('_-Import '+libPath+"\\"+choice+' Objects Enter')
    rs.GetObjects()

getComponent()