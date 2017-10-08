import rhinoscriptsyntax as rs

def distFromCamera(target):
    camPos = rs.ViewCamera(rs.CurrentView())
    dist = rs.Distance(camPos, target)
    print "Distance from camera is " + str(dist)

def main():
    target = rs.GetPoint("Set the target point")
    if target is None: return
    distFromCamera(target)

main()