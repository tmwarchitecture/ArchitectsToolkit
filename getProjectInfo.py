import rhinoscriptsyntax as rs
import Rhino
import scriptcontext
scriptcontext.doc = Rhino.RhinoDoc.ActiveDoc

NAME = rs.GetDocumentData("SITE INFO", "NAME")
GFA = rs.GetDocumentData("SITE INFO", "GFA")
GREEN = rs.GetDocumentData("SITE INFO", "GREEN%")
AREA = str(rs.Area(rs.ObjectsByLayer("SITE::BNDY")))