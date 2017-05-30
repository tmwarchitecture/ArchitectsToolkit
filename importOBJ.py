import rhinoscriptsyntax as rs
import os

libPath = 'C:\\Users\\Tim\\Desktop\\temp\\library'
items = os.listdir(libPath)

choice = rs.ComboListBox(items)

rs.Command('_-Import '+libPath+"\\"+choice+' Objects Enter 0,0,0 1 0')