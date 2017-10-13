import rhinoscriptsyntax as rs

def main():
    items = ["Project Name", "Project Number", "Project Location", "Plot Ratio", "Min Green Coverage", "Max Site Coverage", "CAD coordinate (X,Y,Z)"]
    values = []
    if rs.GetDocumentData("Project Info", items[0]) is not None:
        for i in range(0,len(items)):
            values.append(rs.GetDocumentData("Project Info", items[i]))
    else:
            values = [None, None]
    values = rs.PropertyListBox(items, values, "Project Info", "Project Info")
    
    
    #if rs.ObjectsByLayer("SITE::BNDY") is not None:
    #    siteArea = rs.Area(rs.ObjectsByLayer("SITE::BNDY"))
    #else:
    #    siteArea = "No Site Boundary Layer"
    for i in range(0,len(items)):
        rs.SetDocumentData("Project Info", items[i], values[i])
    rs.Command("_Show ")

if( __name__ == "__main__" ):
    main()