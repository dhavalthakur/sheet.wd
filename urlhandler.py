import urllib.request
import urllib.parse
import urllib.error
import os
from laminus2 import *
class urlhandler:
    address = ''
    data = ''
    def __init__(self, url):
        self.address = url
    def openURL(self):
        self.data =  urllib.request.urlopen(self.address)
    def getURLdata(self):
        return self.data.read()
    def closeURL(self):
        self.data.close()