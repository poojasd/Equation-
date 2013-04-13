'''Physics problem Solver

Finds Distance, Time or Speed according to input
'''

import wx


class MyFrame(wx.Frame):
     def __init__(self, parent, id, title):
  wx.Frame.__init__(self, parent, id, title)
	panel=wx.Panel(self, -1)

	label1= wx.StaticText(panel, -1, 'Speed (kmph):')
	label2= wx.StaticText(panel, -1, 'Distance (km):')
	label3= wx.StaticText(panel, -1, 'Time (hours):')
	label4= wx.StaticText(panel, -1, 'Enter zero for the value you want to find.')

	self.speed= wx.TextCtrl(panel, -1, '0')
	self.distance= wx.TextCtrl(panel, -1, '0')
	self.time= wx.TextCtrl(panel, -1, '0')
	
	self.calcBtn= wx.Button(panel, -1, 'Calculate')
	self.calcBtn.Bind(wx.EVT_BUTTON, self.onCalc)

# use gridbagsizer for layout of widgets
	sizer = wx.GridBagSizer(vgap=5, hgap=10)
	sizer.Add(label4, pos=(0, 0))
	sizer.Add(label1, pos=(2, 0))
	sizer.Add(self.speed, pos=(2, 1)) # row 0, column 1
	sizer.Add(label2, pos=(3, 0))
	sizer.Add(self.distance, pos=(3, 1))
	sizer.Add(label3, pos=(4, 0))
	sizer.Add(self.time, pos=(4, 1))
	sizer.Add(self.calcBtn, pos=(5, 0), span=(1, 2))
# use boxsizer to add border around sizer
	border = wx.BoxSizer()
	border.Add(sizer, 0, wx.ALL, 20)
	panel.SetSizerAndFit(border)
	self.Fit()
     def onCalc(self, event):

	if (self.speed.GetValue())=='0': # find speed
		self.speed.SetValue(str(float(self.distance.GetValue())/float(self.time.GetValue()))) # set speed
	elif (self.distance.GetValue())=='0': #find distance
		self.distance.SetValue(str(float(self.speed.GetValue())*float(self.time.GetValue()))) # set speed
	elif (self.time.GetValue())=='0': #find time
		self.time.SetValue(str(float(self.distance.GetValue())/float(self.speed.GetValue()))) # set time


app=wx.App()
frame=MyFrame(None, -1, 'Physics Problem Solver')
frame.Show()
app.MainLoop()
