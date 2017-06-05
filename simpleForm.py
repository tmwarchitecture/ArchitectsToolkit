import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import *
from System.Drawing import Size, Point
class iForm(Form):

    def __init__(self):
        #the window
        self.Text = 'Simple'
        self.Width = 250
        self.Height = 600
        self.CenterToScreen()
        
        #Button
        btn = Button()
        btn.Parent = self
        btn.Text = "Button"
        btn.Location = Point(0,500)
        btn.Click += self.OnClick
        btn.MouseEnter += self.OnEnter

        #Text
        txt = Label()
        txt.Parent = self
        txt.Text = "This is the text area"
        txt.Location = Point(0,10)
        
        #Group Box
        gb = GroupBox()
        gb.Text = "Group Box"
        gb.Size = Size(120, 210)
        gb.Location = Point(20, 200)
        gb.Parent = self
        
        #check box
        cb = CheckBox()
        cb.Parent = self
        cb.Location = Point(10, 60)
        cb.Text = "Show Title"
        cb.Checked = True
        cb.CheckedChanged += self.OnCBchanged
        
        #Text Box
        tbox = TextBox()
        tbox.Parent = self
        tbox.Location = Point(10, 300)
        tbox.KeyUp += self.OnKeyUp
        
        #Radio Button
        male = RadioButton()
        male.Text = "Male"
        male.Parent = gb
        male.Location = Point(10, 30)
        male.CheckedChanged += self.OnRadioChanged
        female = RadioButton()
        female.Text = "Female"
        female.Parent = gb
        female.Location = Point(10, 60)
        female.CheckedChanged += self.OnRadioChanged
        
        #Status Bar
        self.statusbar = StatusBar()
        self.statusbar.Parent = self
        
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
        #when hover
        self.Close()

    def OnEnter(self, sender, args):
        #When button clicked
        print "button entered"

if __name__ == "__main__":
    form = iForm()
    form.ShowDialog()