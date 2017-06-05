# coding: utf-8
import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
from System.Drawing import Size, Point, Icon, Color
import rhinoscriptsyntax as rs
import sys
import setLevels

class iForm(Form):
    def __init__(self, currentFFL):
        #the window
        self.Text = 'Set Levels'
        self.Width = 300
        self.Height = 600
        self.CenterToScreen()
        self.numLevels = setLevels.getNumFloors()
        self.tempLevels = currentFFL
        self.currentLevels = currentFFL
        self.FTF = []
        self.Autoscroll = True
        tooltip = ToolTip()
        panel = Panel()
        
        panel.ForeColor = Color.Blue
        panel.BackColor = Color.Beige
        panel.BorderStyle = BorderStyle.FixedSingle
        panel.Height = 400
        panel.Width = 300
        self.HScroll = True
        
        #Generate FTF
        for i in range(0, len(self.currentLevels)-1):
            try:
                self.FTF.append(float(self.currentLevels[i+1])-float(self.currentLevels[i]))
            except:
                self.FTF.append("")
        
        #Load Icon
        try:
            self.Icon = Icon("testIcon.ico")
        except Exception, e:
            print "Did not load Icon"
            print e.msg
            sys.exit(1)
        
        #Group Box
        gb = GroupBox()
        gb.Text = "Project Levels"
        gb.Size = Size(240, self.numLevels*40+30)
        gb.Location = Point(10, 10)
        gb.Parent = self
        
        #Button
        closeBtn = Button()
        closeBtn.Parent = self
        closeBtn.Text = "Close"
        closeBtn.Location = Point(200,500)
        closeBtn.Anchor = AnchorStyles.Right
        #btn.Dock = DockStyle.Right
        closeBtn.Click += self.OnClick
        closeBtn.MouseEnter += self.OnEnter
        applyBtn = Button()
        applyBtn.Parent = self
        applyBtn.Text = "Apply"
        applyBtn.Location = Point(100,500)
        applyBtn.Anchor = AnchorStyles.Right
        #btn.Dock = DockStyle.Right
        applyBtn.Click += self.OnApplyClick
        #applyBtn.MouseEnter += self.OnEnter
        
        for i in range(0,self.numLevels):
            #btn2 = Button()
            #btn2.Parent = gb
            #btn2.Text = "Add circle"
            #btn2.Location = Point(180,i*24+24)
            #btn2.Click += self.OnBtn2Enter
            tbox2 = TextBox()
            #tbox2.Align =HorizontalAlignment.Right
            tbox2.Text = str(currentFFL[i])
            tbox2.Name = str(i)
            tbox2.Parent = gb
            tbox2.Size = Size(60,20)
            tbox2.Location = Point(90,i*40+40)
            tbox2.KeyUp += self.OnKeyUp2
            
            #Header
            txtFTF = Label()
            txtFTF.Parent = gb
            txtFTF.Size = Size(36,12)
            txtFTF.Text = "FTF"
            txtFTF.Location = Point(152,10)
            
            txtSym = Label()
            txtSym.Parent = gb
            txtSym.Size = Size(12,12)
            txtSym.Text = "╣" + str(i)
            txtSym.Location = Point(152,i*40+40)
            
            #FTF text box
            if i < self.numLevels-1:
                tbox4 = TextBox()
                
                tbox4.Text = str(self.FTF[i])
                tbox4.Parent = gb
                tbox4.Size = Size(60,20)
                tbox4.Location = Point(152,i*40+58)
                tbox4.KeyUp += self.OnKeyUp2
            
            #Level Label
            txt1 = Label()
            txt1.Parent = gb
            txt1.Text = "Level " + str(i+1)
            txt1.Location = Point(10, i*40+40)
        
        self.statusbar = StatusBar()
        self.statusbar.Parent = self
        
        panel.Controls.Add(gb)
        self.Controls.Add(panel)
    def OnBtn2Enter(self, sender, event):
        rs.AddCircle([0,0,0], self.radius)
    def OnKeyUp2(self, sender, event): 
        self.tempLevels[int(sender.Name)]=sender.Text
        print sender.Name
    def OnKeyUp(self, sender, event): 
        self.Text = sender.Text
    def OnRadioChanged(self, sender, event):
        if sender.Checked:
            self.statusbar.Text = sender.Text
    def OnCBchanged(self, sender, event):
        if sender.Checked:
            self.Text = "CheckBox"
        else:
            self.Text = ""
    def OnClick(self, sender, args):
        self.Close()
    def OnApplyClick(self, sender, args):
        self.currentLevels = self.tempLevels
        print "Levels Updated"
        self.statusbar.Text = "Levels Updated"
    def OnEnter(self, sender, args):
        #When button clicked
        print "button entered"
    def updateFTF(ffl):
        tempFTF = []
        for i in range(0, len(ffl)-1):
            try:
                tempFTF.append(float(ffl[i+1])-float(ffl[i]))
            except:
                tempFTF.append("")
        return tempFTF

if __name__ == "__main__":
    levels = [0,6.0, 12.0, 15]
    form = iForm(setLevels.getFFL())
    form.ShowDialog()
    tempL = []
    tempL = form.currentLevels
    print form.tempLevels
    for i in range(0, len(form.currentLevels)):
        rs.SetDocumentData("Levels", str(i), str(tempL[i]))
