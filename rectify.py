import rhinoscriptsyntax as rs
#import plineCoords
#import dimensionPline as dp
def roundedDist(numList, decPlaces):
    """
    :param numList: list of floats to round
    :param decPlaces: number of decimals to round to (-1 = 10, 2 = .01)
    :return: modified list of numbers
    """
    dlist = []
    for i in range(1, len(numList)):
        dlist.append(numList[i] - numList[i-1])
    for i in range(0, len(dlist)):
        dlist[i] = round(dlist[i], decPlaces)
    for i in range(1, len(numList)):
        numList[i]=numList[i-1] + dlist[i-1]
    return numList
def rectify(pline, decPlaces):
    """
    --Uses your current cplane as guides
    pline: one pline to rectify
    decPlace: number of decimals to round to (1 = 100mm, 2 = 10mm, 3 = 1mm)
    """
    rs.EnableRedraw(False)
    
    #Remove colinear points
    rs.SimplifyCurve(pline)
    
    #orient to world
    xPt = rs.VectorAdd(rs.ViewCPlane().Origin, rs.ViewCPlane().XAxis)
    yPt = rs.VectorAdd(rs.ViewCPlane().Origin, rs.ViewCPlane().YAxis)
    origCplane = [rs.ViewCPlane().Origin, xPt , yPt]
    world = [[0,0,0], [1,0,0], [0,1,0]] 
    rs.OrientObject(pline, origCplane, world)
    
    #get ctrl Pts
    ctrlPts = rs.CurvePoints(pline)
    
    #test if closed
    closedBool = rs.IsCurveClosed(pline)
    if closedBool:
        del ctrlPts[-1]
    
    #initial direction
    stPt = ctrlPts[0]
    nxtPt = ctrlPts[1]
    dX = abs(stPt[0]-nxtPt[0])
    dY = abs(stPt[1]-nxtPt[1])
    if dX>dY:
        xDir = True
    else:
        xDir = False
    
    #split into x and y vals
    xVals = []
    yVals = []
    xVals.append(ctrlPts[0][0])
    yVals.append(ctrlPts[0][1])
    if xDir:
        for i in range(1, len(ctrlPts)):
            if i%2==1:
                xVals.append(ctrlPts[i][0])
            else:
                yVals.append(ctrlPts[i][1])
    else:
        for i in range(1, len(ctrlPts)):
            if i%2==0:
                xVals.append(ctrlPts[i][0])
            else:
                yVals.append(ctrlPts[i][1])
    xVals = roundedDist(xVals, decPlaces)
    yVals = roundedDist(yVals, decPlaces)
    
    #Make points
    newPts = []
    for i in range(0, len(ctrlPts)):
        if xDir:
            if i%2==0:
                newPts.append(rs.coerce3dpoint([xVals[int(i/2)], yVals[int(i/2)], 0]))
            else:
                newPts.append(rs.coerce3dpoint([xVals[int(i/2+.5)], yVals[int(i/2-.5)], 0]))
        else:
            if i%2==0:
                newPts.append(rs.coerce3dpoint([xVals[int(i/2)], yVals[int(i/2)], 0]))
            else:
                newPts.append(rs.coerce3dpoint([xVals[int(i/2-.5)], yVals[int(i/2+.5)], 0]))
    
    #Close it
    if closedBool:
        if xDir:
            newPts[-1].X = newPts[0].X
        else:
            newPts[-1].Y = newPts[0].Y
        newPts.append(newPts[0])
    
    #make new Line
    newLine = rs.AddPolyline(newPts)
    
    #Cleanup
    objectsLay = rs.MatchObjectAttributes(newLine, pline)
    rs.DeleteObject(pline)
    
    #Move back to original cplane
    rs.OrientObject(newLine, world, origCplane)
    
    rs.EnableRedraw(True)
    return newLine
def main():
    objs = rs.GetObjects("Select Curves to Rectify", preselect = True, filter = 4)
    if objs is None:
        return
    for obj in objs:
        newLine = rectify(obj, 1)
        #dp.dimensionPline(newLine, 2)
        #plineCoords.plineCoordinate(newLine)
if __name__=="__main__":
    main()
