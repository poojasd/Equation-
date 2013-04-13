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
		label3= wx.StaticText(panel, -1, 'Time (hrs):')
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

		label11= wx.StaticText(panel, -1, 'Force(N):')
		label21= wx.StaticText(panel, -1, 'Mass (kg):')
		label31= wx.StaticText(panel, -1, 'Acce (m/s):')
	#	label41= wx.StaticText(panel, -1, 'Enter zero for the value you want to find1.')

		self.speed1= wx.TextCtrl(panel, -1, '0')
		self.distance1= wx.TextCtrl(panel, -1, '0')
		self.time1= wx.TextCtrl(panel, -1, '0')

		self.calcBtn1= wx.Button(panel, -1, 'Calculate1')
		self.calcBtn1.Bind(wx.EVT_BUTTON, self.onCalc1)

		# use gridbagsizer for layout of widgets
		sizer = wx.GridBagSizer(vgap=10, hgap=20)
	#	sizer.Add(label41, pos=(0, 0))
		sizer.Add(label11, pos=(7, 0))
		sizer.Add(self.speed1, pos=(7, 6)) # row 0, column 1
		sizer.Add(label21, pos=(8, 0))
		sizer.Add(self.distance1, pos=(8, 6))
		sizer.Add(label31, pos=(9, 0))
		sizer.Add(self.time1, pos=(9, 6))
		sizer.Add(self.calcBtn1, pos=(10, 0), span=(2, 3))
		# use boxsizer to add border around sizer
		border = wx.BoxSizer()
		border.Add(sizer, 0, wx.ALL, 20)
		panel.SetSizerAndFit(border)
		self.Fit()


	def onCalc(self, event):

		if (self.speed.GetValue())=='0': # find speed
			self.speed.SetValue(str(float(self.distance.GetValue())/float(self.time.GetValue())))# set speed
		elif (self.distance.GetValue())=='0': #find distance
			self.distance.SetValue(str(float(self.speed.GetValue())*float(self.time.GetValue()))) # set speed
		elif (self.time.GetValue())=='0': #find time
			self.time.SetValue(str(float(self.distance.GetValue())/float(self.speed.GetValue()))) # set time

	def onCalc1(self, event):

		if (self.speed1.GetValue())=='0': # find force
			self.speed1.SetValue(str(float(self.distance1.GetValue())*float(self.time1.GetValue()))) # set force
		elif (self.distance1.GetValue())=='0': #find mass
			self.distance1.SetValue(str(float(self.speed1.GetValue())/float(self.time1.GetValue()))) # set mass
		elif (self.time1.GetValue())=='0': #find acceleration
			self.time1.SetValue(str(float(self.speed1.GetValue())/float(self.distance1.GetValue()))) # set acceleration


app=wx.App()
frame= MyFrame(None, -1, 'Physics Problem Solver Extended Version')
frame.Show()
app.MainLoop()
