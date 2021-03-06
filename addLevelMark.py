import setLevels
import rhinoscriptsyntax as rs
def midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, 0]
def addLevelMarks(func):
    rs.EnableRedraw(False)
    leftAlign = True
    geometry = []
    currentLevels = setLevels.getFloorLevels()
    for level in currentLevels:
        if level is None:
            print "Levels have not been set."
            return
    levelNames = rs.GetDocumentData("Levels")
    size = 10
    i = 0
    stPts = []
    for level in currentLevels:
        vec1 = [size*.2,size*.1,0]
        ptA = [0, level, 0]
        ptB = [size*.5, level, 0]
        stPts.append(ptA)
        geometry.append(rs.AddLine(ptA, ptB))
        geometry.append(rs.AddText(levelNames[i] + ": +" + str(level), rs.VectorAdd(ptA, vec1), size*.1))
                
        #Triangle Marking
        triPts = [[0,0,0], [size*.05, size*.07,0], [-size*.05, size*.07,0], [0,0,0]]
        newPts = []
        triPt = rs.VectorAdd(ptA, [size*.1, 0,0])
        for j in range(0, 4):
            newPts.append(rs.VectorAdd(triPt, triPts[j]))
        tri = rs.AddPolyline(newPts)
        geometry.append(rs.CloseCurve(tri))
        i=i+1
    
    #Dimensions
    for i in range(0, len(currentLevels)-1):
        pt1 = [0,currentLevels[i], 0]
        pt2 = [0,currentLevels[i+1], 0]
        pt3 = [size*-.15,currentLevels[i+1], 0]
        geometry.append(rs.AddAlignedDimension(pt1, pt2, pt3))
    firstPt = [0,currentLevels[0], 0]
    lastPt = [0,currentLevels[-1], 0]
    dimOffset = [size*-.3,currentLevels[-1], 0]
    geometry.append(rs.AddAlignedDimension(firstPt, lastPt, dimOffset))
    rs.AddLayer("80_LAYOUT", visible = True)
    annoLayer = rs.AddLayer("ANNO", parent = "80_LAYOUT")
    for geo in geometry:
        rs.ObjectLayer(geo, annoLayer)
    rs.AddBlock(geometry, [0,0,0], "Level Marks", True)
    if (func == 0):
        block = rs.InsertBlock("Level Marks", [0,0,0])
        rs.ObjectLayer(block, "ANNO")
    
    rs.EnableRedraw(True)
    return
if __name__=="__main__":
    func = rs.GetInteger("")
    addLevelMarks(func)
    
