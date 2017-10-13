import rhinoscriptsyntax as rs

def proximityPts(pts, initialIndex):
    ptsRemaining = pts
    ptsActivated = []
    initialIndex = initialIndex
    ptsActivated.append(pts[initialIndex])
    del ptsRemaining[initialIndex]
    
    for i in range(0, len(pts)):
        closestIndex = rs.PointArrayClosestPoint(ptsRemaining, ptsActivated[-1])
        ptsActivated.append(pts[closestIndex])
        del ptsRemaining[closestIndex]
    
    return ptsActivated

def addNumberTag(sortedPts, objs):
    for i, pt in enumerate(sortedPts):
        numTag = rs.AddText(str(i+1), pt, justification = 131074)
        objLay = rs.ObjectLayer(objs[i])
        parentLayer = rs.ParentLayer(objLay)
        hostLayer = rs.AddLayer("ANNO_NUM", (128,128,128), parent = parentLayer)
        rs.ObjectLayer(numTag, hostLayer)


def main():
    objs = rs.GetObjects("Select Objects to Number", preselect = True)
    if objs is None: return
    pts = []
    for obj in objs:
        pt0 = rs.BoundingBox(obj)[0]
        pt2 = rs.BoundingBox(obj)[2]
        centerPt = rs.PointDivide(rs.PointAdd(pt0, pt2), 2)
        pts.append(centerPt)
    sortedPts = proximityPts(pts,0)
    addNumberTag(sortedPts, objs)
    print len(sortedPts)

main()