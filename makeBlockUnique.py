import rhinoscriptsyntax as rs

def makeBlockUnique(obj):
    oldBase = rs.BlockInstanceInsertPoint(obj)
    if oldBase is None: return
    newName = rs.GetString("New Block Name")
    if newName is None: return
    newOrigin = rs.GetPoint("Select New Block Base point", base_point = oldBase)
    if newOrigin is None: return
    blockObjs = rs.ExplodeBlockInstance(obj)
    if blockObjs is None: return
    origObjs = []
    
    for a in blockObjs:
        origObjs.append(a)
    
    rs.AddBlock(origObjs, newOrigin, newName, True)
    
    rs.InsertBlock(newName, newOrigin)
    
    return

def main():
    obj = rs.GetObject("Select Block to Make unique", filter = 4096)
    makeBlockUnique(obj)

main()