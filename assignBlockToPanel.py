import rhinoscriptsyntax as rs

def assignBlockToPanel(obj):
    """
    Assigns block containing a base surface to a surface with the matching name.
    Block, base surface, and target surface must all have the same name.
    
    input: target surface (with name)
    returns: None
    """
    allBlockNames = rs.BlockNames()
    for eachBlockName in allBlockNames:
        if rs.ObjectName(obj) == eachBlockName:
            blockName = eachBlockName
            print "Matching Block Found"
            
            objBasePt = rs.SurfaceEditPoints(obj)[0]
            objYPt = rs.SurfaceEditPoints(obj)[1]
            objXPt = rs.SurfaceEditPoints(obj)[2]
            objXVec = rs.VectorCreate(objXPt, objBasePt)
            objXLength = rs.VectorLength(objXVec)
            objYLength = rs.Distance(objBasePt, objYPt)
            
            
            blockObjs = rs.BlockObjects(blockName)
            for blockObj in blockObjs:
                if rs.ObjectName(blockObj) == blockName:
                    print "Contains base plane"
                    if rs.IsSurface(blockObj):
                        blockBasePt = rs.SurfaceEditPoints(blockObj)[0]
                        blockYPt = rs.SurfaceEditPoints(blockObj)[1]
                        blockXPt = rs.SurfaceEditPoints(blockObj)[2]
                        blockXVec = rs.VectorCreate(blockXPt, blockBasePt)
                        rotAngle = rs.VectorAngle(objXVec ,blockXVec)
                        blockXLength = rs.VectorLength(blockXVec)
                        blockYLength = rs.VectorLength(rs.VectorCreate(blockYPt, blockBasePt))
                        xScale = objXLength/blockXLength
                        yScale = objYLength/blockYLength
                        newScale = [yScale, xScale, 1]
                        rs.InsertBlock(blockName, objBasePt, scale = newScale, angle_degrees = rotAngle)
                        break
                    else:
                        print "Error: Base plane was not a surface"

def main():
    objs = rs.GetObjects("Select panels to add matching block to", 8, preselect = True)
    if objs is None: return
    for obj in objs:
       assignBlockToPanel(obj)

if __name__ == "__main__":
    main()