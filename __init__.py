import ts3lib as ts3
from ts3plugin import ts3plugin, PluginHost
import ts3defines
from PythonQt.QtGui import *
from PythonQt.QtCore import *


class bannerHider(ts3plugin):
	"""docstring for bannerHidder"""
	name = "bannerHider"
	requestAutoload = False
	version = "1"
	apiVersion = 22
	author = "Scratch"
	description = "Hides the banner on connection"
	offersConfigure = False
	commandKeyword = ""
	infoTitle = ""
	hotkeys = []
	menuItems = []

	def getBanners(self):
		banners = []
		try:
			for widget in QApplication.instance().allWidgets():
				if widget.className() == 'Banner':
					banners.append(widget)
			return banners
		except: from traceback import format_exc; ts3.logMessage(format_exc(), ts3defines.LogLevel.LogLevel_ERROR, "PyTSon", 0)
	
	def hideBanner(self, banners):
		for banner in banners:
			banner.visible = False
	
	def onConnectStatusChangeEvent(self, serverConnectionHandlerID, newStatus, errorNumber):
		if newStatus == 2:
			self.hideBanner(self.getBanners())
