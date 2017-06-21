import rhinoscriptsyntax as rs

def dimTENSimple():
    name = "TEN_Simple"
    rs.AddDimStyle(name)
    rs.DimStyleFont(name, "Calibri")
    rs.DimStyleLinearPrecision(name, 0)
    rs.DimStyleAnglePrecision(name, 1.00)
    
    
    rs.DimStyleArrowSize(name, 1.0)
    rs.DimStyleExtension(name, 1)
    
    rs.DimStyleLeaderArrowSize(name, 3.0)
    rs.DimStyleLengthFactor(name, 1000)
    
    rs.DimStyleNumberFormat(name, 0)
    rs.DimStyleOffset(name, 1)
    
    rs.DimStyleTextAlignment(name, 2)
    rs.DimStyleTextGap(name, 1)
    rs.DimStyleTextHeight(name, 1.5)
def dimTENPrecision():
    name = "TEN_Precision"
    rs.AddDimStyle(name)
    rs.DimStyleFont(name, "Calibri")
    rs.DimStyleLinearPrecision(name, 7)
    rs.DimStyleAnglePrecision(name, 1.00)
    
    
    rs.DimStyleArrowSize(name, 1.0)
    rs.DimStyleExtension(name, 1)
    
    rs.DimStyleLeaderArrowSize(name, 1.0)
    rs.DimStyleLengthFactor(name, 1000)
    
    rs.DimStyleNumberFormat(name, 0)
    rs.DimStyleOffset(name, 1)
    #rs.DimStylePrefix(name, None)
    rs.DimStyleTextAlignment(name, 2)
    rs.DimStyleTextGap(name, 1)
    rs.DimStyleTextHeight(name, 1.5)

if __name__ == "__main__":
    dimTENSimple()
    dimTENPrecision()