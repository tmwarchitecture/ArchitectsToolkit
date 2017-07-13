import rhinoscriptsyntax as rs
import Rhino
import System.Drawing.Color

def addConstructionLine(point_a):
    # Color to use when drawing dynamic lines
    line_color_1 = System.Drawing.Color.FromArgb(200,200,200)
    line_color_2 = System.Drawing.Color.FromArgb(255,0,0)

    # This is a function that is called whenever the GetPoint's
    # DynamicDraw event occurs
    def GetPointDynamicDrawFunc( sender, args ):
        point_b = args.CurrentPoint
        point_C = Rhino.Geometry.Point3d((point_a.X + point_b.X)/2, (point_a.Y + point_b.Y)/2, (point_a.Z + point_b.Z)/2)
        #Rhino.Geometry.Transform.Translation(
        vec = rs.VectorCreate(point_b, point_a)
        rs.VectorUnitize(vec)
        vec2 = rs.VectorScale(vec, 500)
        vec3 = rs.coerce3dpoint(rs.VectorAdd(point_b, vec2))
        rs.VectorReverse(vec2)
        vec4 = rs.coerce3dpoint(rs.VectorSubtract(point_b, vec2))
        
        args.Display.DrawLine(point_a, vec3, line_color_1, 1)
        args.Display.DrawLine(point_a, vec4, line_color_1, 1)
        args.Display.DrawPoint(point_a,Rhino.Display.PointStyle.ControlPoint,3,line_color_1)
        args.Display.DrawPoint(point_b,Rhino.Display.PointStyle.ControlPoint,3,line_color_2)

    # Create an instance of a GetPoint class and add a delegate
    # for the DynamicDraw event
    gp = Rhino.Input.Custom.GetPoint()
    gp.DynamicDraw += GetPointDynamicDrawFunc
    gp.Get()
    if( gp.CommandResult() == Rhino.Commands.Result.Success ):
        pt = gp.Point()
        line = rs.AddLine(point_a, pt)
        c = rs.CurveMidPoint(line)
        scaled = rs.ScaleObject(line, c, [500, 500, 500])
        rs.ObjectColor(scaled, [199,199,199])


if( __name__ == "__main__" ):
    #get the first point
    point_a = rs.GetPoint("Pick First Point")
    if point_a:
        addConstructionLine(point_a)