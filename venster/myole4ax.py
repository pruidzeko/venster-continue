# -*- coding: mbcs -*-
typelib_path = 'myole4ax.tlb'
_lcid = 0 # change this if required
from ctypes import *
import stdole2
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
StructPtr = c_int
WSTRING = c_wchar_p
from ctypes.wintypes import POINT
from ctypes.wintypes import MSG
from ctypes.wintypes import RECT
from ctypes.wintypes import SIZE
from comtypes.automation import IDispatch
BORDERWIDTHS = RECT


class __MIDL___MIDL_itf_myole4ax_0000_0006(Structure):
    pass
OLEINPLACEFRAMEINFO = __MIDL___MIDL_itf_myole4ax_0000_0006
class __MIDL___MIDL_itf_myole4ax_0000_0002(Structure):
    pass
__MIDL___MIDL_itf_myole4ax_0000_0002._fields_ = [
    ('x', c_int),
    ('y', c_int),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0002) == 8, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0002)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0002) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0002)
class IOleWindow(stdole2.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000114-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IOleInPlaceUIWindow(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{00000115-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IOleInPlaceFrame(IOleInPlaceUIWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{00000116-0000-0000-C000-000000000046}')
    _idlflags_ = []
IOleWindow._methods_ = [
    COMMETHOD([], HRESULT, 'GetWindow',
              ( ['retval', 'out'], POINTER(c_int), 'phwnd' )),
    COMMETHOD([], HRESULT, 'ContextSensitiveHelp',
              ( ['in'], c_int, 'fEnterMode' )),
]
################################################################
## code template for IOleWindow implementation
##class IOleWindow_Impl(object):
##    def GetWindow(self):
##        '-no docstring-'
##        #return phwnd
##
##    def ContextSensitiveHelp(self, fEnterMode):
##        '-no docstring-'
##        #return 
##

class IOleInPlaceActiveObject(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{00000117-0000-0000-C000-000000000046}')
    _idlflags_ = []
IOleInPlaceUIWindow._methods_ = [
    COMMETHOD([], HRESULT, 'GetBorder',
              ( ['in'], StructPtr, 'lprectBorder' )),
    COMMETHOD([], HRESULT, 'RequestBorderSpace',
              ( ['in'], StructPtr, 'pborderwidths' )),
    COMMETHOD([], HRESULT, 'SetBorderSpace',
              ( ['in'], StructPtr, 'pborderwidths' )),
    COMMETHOD([], HRESULT, 'SetActiveObject',
              ( ['in'], POINTER(IOleInPlaceActiveObject), 'pActiveObject' ),
              ( ['in'], WSTRING, 'pszObjName' )),
]
################################################################
## code template for IOleInPlaceUIWindow implementation
##class IOleInPlaceUIWindow_Impl(object):
##    def RequestBorderSpace(self, pborderwidths):
##        '-no docstring-'
##        #return 
##
##    def SetActiveObject(self, pActiveObject, pszObjName):
##        '-no docstring-'
##        #return 
##
##    def SetBorderSpace(self, pborderwidths):
##        '-no docstring-'
##        #return 
##
##    def GetBorder(self, lprectBorder):
##        '-no docstring-'
##        #return 
##

IOleInPlaceFrame._methods_ = [
]
################################################################
## code template for IOleInPlaceFrame implementation
##class IOleInPlaceFrame_Impl(object):

class __MIDL___MIDL_itf_myole4ax_0000_0003(Structure):
    pass
__MIDL___MIDL_itf_myole4ax_0000_0003._fields_ = [
    ('x', c_float),
    ('y', c_float),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0003) == 8, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0003)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0003) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0003)
class __MIDL___MIDL_itf_myole4ax_0000_0004(Structure):
    pass
__MIDL___MIDL_itf_myole4ax_0000_0004._fields_ = [
    ('hWnd', c_int),
    ('message', c_int),
    ('wParam', c_int),
    ('lParam', c_int),
    ('time', c_int),
    ('pt', POINT),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0004) == 28, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0004)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0004) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0004)
POINTF = __MIDL___MIDL_itf_myole4ax_0000_0003
class __MIDL___MIDL_itf_myole4ax_0000_0005(Structure):
    pass
__MIDL___MIDL_itf_myole4ax_0000_0005._fields_ = [
    ('cx', c_int),
    ('cy', c_int),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0005) == 8, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0005)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0005) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0005)
class Library(object):
    u'My Ole Guid and interface definitions'
    name = u'myole4ax'
    _reg_typelib_ = ('{99AB80C4-5E19-4FD5-B3CA-5EF62FC3F765}', 1, 0)

class IOleClientSite(stdole2.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000118-0000-0000-C000-000000000046}')
    _idlflags_ = []
IOleClientSite._methods_ = [
]
################################################################
## code template for IOleClientSite implementation
##class IOleClientSite_Impl(object):

class __MIDL___MIDL_itf_myole4ax_0000_0001(Structure):
    pass
__MIDL___MIDL_itf_myole4ax_0000_0001._fields_ = [
    ('Left', c_int),
    ('Top', c_int),
    ('Right', c_int),
    ('Bottom', c_int),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0001) == 16, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0001)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0001) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0001)
class IOleControlSite(stdole2.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B196B289-BAB4-101A-B69C-00AA00341D07}')
    _idlflags_ = []
IOleControlSite._methods_ = [
    COMMETHOD([], HRESULT, 'OnControlInfoChanged'),
    COMMETHOD([], HRESULT, 'LockInPlaceActive',
              ( ['in'], c_int, 'fLock' )),
    COMMETHOD([], HRESULT, 'GetExtendedControl',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppDisp' )),
    COMMETHOD([], HRESULT, 'TransformCoords',
              ( ['in'], StructPtr, 'pPtlHimetric' ),
              ( ['in'], StructPtr, 'pPtfContainer' ),
              ( ['in'], c_int, 'dwFlags' )),
    COMMETHOD([], c_int, 'TranslateAccelerator',
              ( ['in'], StructPtr, 'lpmsg' ),
              ( ['in'], c_int, 'grfModifiers' )),
    COMMETHOD([], HRESULT, 'OnFocus',
              ( ['in'], c_int, 'fGotFocus' )),
    COMMETHOD([], HRESULT, 'ShowPropertyFrame'),
]
################################################################
## code template for IOleControlSite implementation
##class IOleControlSite_Impl(object):
##    def TransformCoords(self, pPtlHimetric, pPtfContainer, dwFlags):
##        '-no docstring-'
##        #return 
##
##    def GetExtendedControl(self):
##        '-no docstring-'
##        #return ppDisp
##
##    def ShowPropertyFrame(self):
##        '-no docstring-'
##        #return 
##
##    def TranslateAccelerator(self, lpmsg, grfModifiers):
##        '-no docstring-'
##        #return 
##
##    def LockInPlaceActive(self, fLock):
##        '-no docstring-'
##        #return 
##
##    def OnFocus(self, fGotFocus):
##        '-no docstring-'
##        #return 
##
##    def OnControlInfoChanged(self):
##        '-no docstring-'
##        #return 
##

IOleInPlaceActiveObject._methods_ = [
    COMMETHOD([], c_int, 'TranslateAccelerator',
              ( ['in'], c_int, 'lpmsg' )),
    COMMETHOD([], c_int, 'OnFrameWindowActivate',
              ( ['in'], c_int, 'fActivate' )),
    COMMETHOD([], c_int, 'OnDocWindowActivate',
              ( ['in'], c_int, 'fActivate' )),
    COMMETHOD([], c_int, 'ResizeBorder',
              ( ['in'], StructPtr, 'prcBorder' ),
              ( ['in'], POINTER(IOleInPlaceUIWindow), 'pUIWindow' ),
              ( ['in'], c_int, 'fFrameWindow' )),
    COMMETHOD([], c_int, 'EnableModeless',
              ( ['in'], c_int, 'fEnable' )),
]
################################################################
## code template for IOleInPlaceActiveObject implementation
##class IOleInPlaceActiveObject_Impl(object):
##    def OnFrameWindowActivate(self, fActivate):
##        '-no docstring-'
##        #return 
##
##    def TranslateAccelerator(self, lpmsg):
##        '-no docstring-'
##        #return 
##
##    def EnableModeless(self, fEnable):
##        '-no docstring-'
##        #return 
##
##    def ResizeBorder(self, prcBorder, pUIWindow, fFrameWindow):
##        '-no docstring-'
##        #return 
##
##    def OnDocWindowActivate(self, fActivate):
##        '-no docstring-'
##        #return 
##

class IOleInPlaceSite(IOleWindow):
    _case_insensitive_ = True
    _iid_ = GUID('{00000119-0000-0000-C000-000000000046}')
    _idlflags_ = []
IOleInPlaceSite._methods_ = [
    COMMETHOD([], c_int, 'CanInPlaceActivate'),
    COMMETHOD([], HRESULT, 'OnInPlaceActivate'),
    COMMETHOD([], HRESULT, 'OnUIActivate'),
    COMMETHOD([], HRESULT, 'GetWindowContext',
              ( ['out'], POINTER(POINTER(IOleInPlaceFrame)), 'ppFrame' ),
              ( ['out'], POINTER(POINTER(IOleInPlaceUIWindow)), 'ppDoc' ),
              ( ['in'], StructPtr, 'lprcPosRect' ),
              ( ['in'], StructPtr, 'lprcClipRect' ),
              ( ['in'], StructPtr, 'lpFrameInfo' )),
    COMMETHOD([], HRESULT, 'Scroll',
              ( ['in'], c_longlong, 'scrollExtant' )),
    COMMETHOD([], HRESULT, 'OnUIDeactivate',
              ( ['in'], c_int, 'fUndoable' )),
    COMMETHOD([], HRESULT, 'OnInPlaceDeactivate'),
    COMMETHOD([], HRESULT, 'DiscardUndoState'),
    COMMETHOD([], HRESULT, 'DeactivateAndUndo'),
    COMMETHOD([], HRESULT, 'OnPosRectChange',
              ( ['in'], c_int, 'lprcPosRect' )),
]
################################################################
## code template for IOleInPlaceSite implementation
##class IOleInPlaceSite_Impl(object):
##    def OnInPlaceDeactivate(self):
##        '-no docstring-'
##        #return 
##
##    def CanInPlaceActivate(self):
##        '-no docstring-'
##        #return 
##
##    def OnPosRectChange(self, lprcPosRect):
##        '-no docstring-'
##        #return 
##
##    def GetWindowContext(self, lprcPosRect, lprcClipRect, lpFrameInfo):
##        '-no docstring-'
##        #return ppFrame, ppDoc
##
##    def DeactivateAndUndo(self):
##        '-no docstring-'
##        #return 
##
##    def OnInPlaceActivate(self):
##        '-no docstring-'
##        #return 
##
##    def OnUIDeactivate(self, fUndoable):
##        '-no docstring-'
##        #return 
##
##    def OnUIActivate(self):
##        '-no docstring-'
##        #return 
##
##    def Scroll(self, scrollExtant):
##        '-no docstring-'
##        #return 
##
##    def DiscardUndoState(self):
##        '-no docstring-'
##        #return 
##

class IOleObject(stdole2.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000112-0000-0000-C000-000000000046}')
    _idlflags_ = []
IOleObject._methods_ = [
    COMMETHOD([], HRESULT, 'SetClientSite',
              ( ['in'], POINTER(IOleClientSite), 'pClientSite' )),
    COMMETHOD([], HRESULT, 'GetClientSite',
              ( ['retval', 'out'], POINTER(POINTER(IOleClientSite)), 'ppClientSite' )),
]
################################################################
## code template for IOleObject implementation
##class IOleObject_Impl(object):
##    def SetClientSite(self, pClientSite):
##        '-no docstring-'
##        #return 
##
##    def GetClientSite(self):
##        '-no docstring-'
##        #return ppClientSite
##

__MIDL___MIDL_itf_myole4ax_0000_0006._fields_ = [
    ('cb', c_int),
    ('fMDIApp', c_int),
    ('hwndFrame', stdole2.OLE_HANDLE),
    ('haccel', stdole2.OLE_HANDLE),
    ('cAccelEntries', c_int),
]
assert sizeof(__MIDL___MIDL_itf_myole4ax_0000_0006) == 20, sizeof(__MIDL___MIDL_itf_myole4ax_0000_0006)
assert alignment(__MIDL___MIDL_itf_myole4ax_0000_0006) == 4, alignment(__MIDL___MIDL_itf_myole4ax_0000_0006)
__all__ = ['POINTF', 'StructPtr', 'IOleClientSite',
           'IOleInPlaceFrame', 'IOleInPlaceUIWindow', 'IOleObject',
           'OLEINPLACEFRAMEINFO',
           '__MIDL___MIDL_itf_myole4ax_0000_0005', 'IOleInPlaceSite',
           'BORDERWIDTHS', 'IOleControlSite',
           '__MIDL___MIDL_itf_myole4ax_0000_0002',
           '__MIDL___MIDL_itf_myole4ax_0000_0004',
           '__MIDL___MIDL_itf_myole4ax_0000_0006',
           '__MIDL___MIDL_itf_myole4ax_0000_0001',
           'IOleInPlaceActiveObject',
           '__MIDL___MIDL_itf_myole4ax_0000_0003', 'IOleWindow']
#~ from comtypes import _check_version; _check_version('482')
