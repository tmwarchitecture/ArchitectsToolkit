import setLevels
import rhinoscriptsyntax as rs
def midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, 0]
def addLevelMarks():
    currentLevels = setLevels.getFloorLevels()
    size = 10
    i = 0
    stPts = []
    for level in currentLevels:
        vec1 = [size*.2,size*.1,0]
        ptA = [0, level, 0]
        ptB = [size, level, 0]
        stPts.append(ptA)
        rs.AddLine(ptA, ptB)
        rs.AddText("Level " + str(i+1) + ": +" + str(level), rs.VectorAdd(ptA, vec1), size*.1)
        triPts = [[0,0,0], [size*.05, size*.1,0], [-size*.05, size*.1,0], [0,0,0]]
        newPts = []
        for j in range(0, 4):
            newPts.append(rs.VectorAdd(ptA, triPts[j]))
        tri = rs.AddPolyline(newPts)
        rs.CloseCurve(tri)
        i=i+1
    return
if __name__=="__main__":
    addLevelMarks()
