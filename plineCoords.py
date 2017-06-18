import rhinoscriptsyntax as rs

def plineCoordinate(pline):
    ctrlPts = rs.CurvePoints(pline)
    offsetDist = 3
    offsetVec = [offsetDist,offsetDist,0]
    textVec = [offsetDist,0,0]
    for ctrlPt in ctrlPts:
        leaderList = []
        ptX = ctrlPt[0]
        ptY = ctrlPt[1]
        ptZ = ctrlPt[2]
        text = str(ptX) + ", " + str(ptY) + ", " + str(ptZ)
        leaderPt = rs.VectorAdd(ctrlPt, offsetVec)
        textPt = rs.VectorAdd(leaderPt, textVec)
        leaderList.append(ctrlPt)
        leaderList.append(leaderPt)
        leaderList.append(textPt)
        leader = rs.AddLeader(leaderList, text = text)
        root = rs.AddLayer("80_LAYOUT")
        dimsLayer = rs.AddLayer("LEADERS", parent = root, color = (200,200,200))
        rs.ObjectLayer(leader, dimsLayer)

obj = rs.GetObject("", preselect = True)
plineCoordinate(obj)