import rhinoscriptsyntax as rs
import datetime

def viewCaptureToFile():
    namedViews = rs.NamedViews()
    items = []
    for view in namedViews:
        items.append([view, False])
    returnedVals = rs.CheckListBox(items, "Select Views to Export", "Extract Views")
    if returnedVals is None: return
    
    chosenViews = []
    for val in returnedVals:
        if val[1]:
            chosenViews.append(val[0])
    if len(chosenViews) < 1: return
    
    path = rs.BrowseForFolder(message = "Choose Folder to export to")
    
    if path is None: return
    
    width = rs.GetInteger("Image Width in Pixels", number = 1920, minimum = 600, maximum = 10000)
    if width is None: return
    height = .625 * width
    
    rs.AddNamedView("temp")
    
    now = datetime.date.today()
    dateList = []
    if len(str(now.month))>1:
        month = str(now.month)
    else:
        month = "0"+str(now.month)
    if len(str(now.day))>1:
        day = str(now.day)
    else:
        day = "0"+str(now.day)
    time = str(now.year)+month+day
    
    for x in chosenViews:
        rs.RestoreNamedView(x)
        fileName = "\\" + str(time) + "_" + x + ".jpg"
        filePath = path + fileName
        rs.Command("_-ViewCaptureToFile  " + str(filePath) + " w " + str(width) + " h " + str(height) + " _Enter")
    rs.RestoreNamedView("temp")
    rs.DeleteNamedView("temp")

def main():
    rs.EnableRedraw(False)
    viewCaptureToFile()
    rs.EnableRedraw(True)

main()