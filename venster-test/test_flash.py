## 	   Copyright (c) 2003 Henk Punt

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the
## "Software"), to deal in the Software without restriction, including
## without limitation the rights to use, copy, modify, merge, publish,
## distribute, sublicense, and/or sell copies of the Software, and to
## permit persons to whom the Software is furnished to do so, subject to
## the following conditions:

## The above copyright notice and this permission notice shall be
## included in all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
## NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
## LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
## OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
## WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE

from venster.windows import *
from venster.wtl import *
from venster import atl
from venster.lib import form


from ctypes import *
from comtypes.connectionpoints import dispinterface_EventReceiver

import flash

class FlashEventsImpl(dispinterface_EventReceiver):
    _com_interfaces_ = [flash._IShockwaveFlashEvents]

    # The base class will call all methods we implement here,
    # and simply print the method name with the arguments
    # for unimplemented methods:
    def OnReadyStateChange(self, this, state):
        print "OnReadyStateChange: ", state
        
class FlashWindow(atl.AxWindow):
    def __init__(self, *args, **kwargs):
        atl.AxWindow.__init__(self, flash.ShockwaveFlash._reg_clsid_, *args, **kwargs)

        self.pUnk = self.GetControl()
        #get the Flash interface of the control
        self.pFlash = POINTER(flash.IShockwaveFlash)()
        self.pUnk.QueryInterface(byref(flash.IShockwaveFlash._iid_),
                                 byref(self.pFlash))

        #events are received by FlashEventsImpl
        self.flashEvents = FlashEventsImpl()
        self.flashEvents.connect(self.pFlash)

        #start the flash movie
        import os
        self.pFlash.LoadMovie(0, os.getcwd() + os.sep + "cow.swf")
        self.pFlash.Play()


    def dispose(self):
        #TODO disconnect connectionpoint but crashes :-(
        atl.AxWindow.dispose(self)

        
class MyForm(form.Form):
    _window_icon_ = _window_icon_sm_ = Icon("COW.ICO")
    
    _window_title_ = "Venster Flash Player"
    
    def OnCreate(self, event):
        self.controls.Add(form.CTRL_VIEW, FlashWindow(parent = self))

if __name__ == '__main__':
    mainForm = MyForm()        

    application = Application()
    application.Run()

