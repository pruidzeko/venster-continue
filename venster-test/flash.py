# -*- python -*-
# Generated from c:\WORK\ctypes\win32\com\tools\Flash.ocx

###############################################################
# NOTE: This is a GENERATED file. Please do not make changes, #
# they will be overwritten next time it is regenerated.       #
###############################################################

from ctypes import *
from comtypes import IUnknown, GUID, STDMETHOD, HRESULT
from comtypes.automation import IDispatch, BSTR, VARIANT, dispinterface, DISPMETHOD, DISPPARAMS, EXCEPINFO


##############################################################################

# The Type Library
class ShockwaveFlashObjects:
    'Shockwave Flash'
    guid = GUID('{D27CDB6B-AE6D-11CF-96B8-444553540000}')
    version = (1, 0)
    flags = 0x8
    path = 'c:\\WORK\\ctypes\\win32\\com\\tools\\Flash.ocx'

##############################################################################

class IShockwaveFlash(IDispatch):
    """Shockwave Flash"""
    _iid_ = GUID('{D27CDB6C-AE6D-11CF-96B8-444553540000}')


class _IShockwaveFlashEvents(dispinterface):
    """Event interface for Shockwave Flash"""
    _iid_ = GUID('{D27CDB6D-AE6D-11CF-96B8-444553540000}')


class IFlashFactory(IUnknown):
    """IFlashFactory Interface"""
    _iid_ = GUID('{D27CDB70-AE6D-11CF-96B8-444553540000}')


class IDispatchEx(IDispatch):
    _iid_ = GUID('{A6EF9860-C720-11D0-9337-00A0C90DCAA9}')


class IFlashObjectInterface(IDispatchEx):
    """IFlashObjectInterface Interface"""
    _iid_ = GUID('{D27CDB72-AE6D-11CF-96B8-444553540000}')

class IServiceProvider(IUnknown):
    _iid_ = GUID('{6D5140C1-7436-11CE-8034-00AA006009FA}')


IShockwaveFlash._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "_get_ReadyState", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_TotalFrames", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_Playing", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_Playing", c_int),
    STDMETHOD(HRESULT, "_get_Quality", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_Quality", c_int),
    STDMETHOD(HRESULT, "_get_ScaleMode", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_ScaleMode", c_int),
    STDMETHOD(HRESULT, "_get_AlignMode", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_AlignMode", c_int),
    STDMETHOD(HRESULT, "_get_BackgroundColor", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_BackgroundColor", c_long),
    STDMETHOD(HRESULT, "_get_Loop", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_Loop", c_int),
    STDMETHOD(HRESULT, "_get_Movie", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_Movie", BSTR),
    STDMETHOD(HRESULT, "_get_FrameNum", POINTER(c_long)),
    STDMETHOD(HRESULT, "_put_FrameNum", c_long),
    STDMETHOD(HRESULT, "SetZoomRect", c_long, c_long, c_long, c_long),
    STDMETHOD(HRESULT, "Zoom", c_int),
    STDMETHOD(HRESULT, "Pan", c_long, c_long, c_int),
    STDMETHOD(HRESULT, "Play"),
    STDMETHOD(HRESULT, "Stop"),
    STDMETHOD(HRESULT, "Back"),
    STDMETHOD(HRESULT, "Forward"),
    STDMETHOD(HRESULT, "Rewind"),
    STDMETHOD(HRESULT, "StopPlay"),
    STDMETHOD(HRESULT, "GotoFrame", c_long),
    STDMETHOD(HRESULT, "CurrentFrame", POINTER(c_long)),
    STDMETHOD(HRESULT, "IsPlaying", POINTER(c_int)),
    STDMETHOD(HRESULT, "PercentLoaded", POINTER(c_long)),
    STDMETHOD(HRESULT, "FrameLoaded", c_long, POINTER(c_int)),
    STDMETHOD(HRESULT, "FlashVersion", POINTER(c_long)),
    STDMETHOD(HRESULT, "_get_WMode", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_WMode", BSTR),
    STDMETHOD(HRESULT, "_get_SAlign", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_SAlign", BSTR),
    STDMETHOD(HRESULT, "_get_Menu", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_Menu", c_int),
    STDMETHOD(HRESULT, "_get_Base", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_Base", BSTR),
    STDMETHOD(HRESULT, "_get_Scale", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_Scale", BSTR),
    STDMETHOD(HRESULT, "_get_DeviceFont", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_DeviceFont", c_int),
    STDMETHOD(HRESULT, "_get_EmbedMovie", POINTER(c_int)),
    STDMETHOD(HRESULT, "_put_EmbedMovie", c_int),
    STDMETHOD(HRESULT, "_get_BGColor", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_BGColor", BSTR),
    STDMETHOD(HRESULT, "_get_Quality2", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_Quality2", BSTR),
    STDMETHOD(HRESULT, "LoadMovie", c_int, BSTR),
    STDMETHOD(HRESULT, "TGotoFrame", BSTR, c_long),
    STDMETHOD(HRESULT, "TGotoLabel", BSTR, BSTR),
    STDMETHOD(HRESULT, "TCurrentFrame", BSTR, POINTER(c_long)),
    STDMETHOD(HRESULT, "TCurrentLabel", BSTR, POINTER(BSTR)),
    STDMETHOD(HRESULT, "TPlay", BSTR),
    STDMETHOD(HRESULT, "TStopPlay", BSTR),
    STDMETHOD(HRESULT, "SetVariable", BSTR, BSTR),
    STDMETHOD(HRESULT, "GetVariable", BSTR, POINTER(BSTR)),
    STDMETHOD(HRESULT, "TSetProperty", BSTR, c_int, BSTR),
    STDMETHOD(HRESULT, "TGetProperty", BSTR, c_int, POINTER(BSTR)),
    STDMETHOD(HRESULT, "TCallFrame", BSTR, c_int),
    STDMETHOD(HRESULT, "TCallLabel", BSTR, BSTR),
    STDMETHOD(HRESULT, "TSetPropertyNum", BSTR, c_int, c_double),
    STDMETHOD(HRESULT, "TGetPropertyNum", BSTR, c_int, POINTER(c_double)),
    STDMETHOD(HRESULT, "TGetPropertyAsNumber", BSTR, c_int, POINTER(c_double)),
    STDMETHOD(HRESULT, "_get_SWRemote", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_SWRemote", BSTR),
    STDMETHOD(HRESULT, "_get_FlashVars", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_FlashVars", BSTR),
    STDMETHOD(HRESULT, "_get_AllowScriptAccess", POINTER(BSTR)),
    STDMETHOD(HRESULT, "_put_AllowScriptAccess", BSTR),
]

_IShockwaveFlashEvents._dispmethods_ = [
    DISPMETHOD(0xfffffd9f, None, "OnReadyStateChange", c_long),
    DISPMETHOD(0x7a6, None, "OnProgress", c_long),
    DISPMETHOD(0x96, None, "FSCommand", BSTR, BSTR),
]

IFlashFactory._methods_ = IUnknown._methods_ + [
]

IFlashObjectInterface._methods_ = IDispatchEx._methods_ + [
]

IDispatchEx._methods_ = IDispatch._methods_ + [
    STDMETHOD(HRESULT, "GetDispID", BSTR, c_ulong, POINTER(c_long)),
    STDMETHOD(HRESULT, "RemoteInvokeEx", c_long, c_ulong, c_ulong, POINTER(DISPPARAMS), POINTER(VARIANT), POINTER(EXCEPINFO), POINTER(IServiceProvider), c_uint, POINTER(c_uint), POINTER(VARIANT)),
    STDMETHOD(HRESULT, "DeleteMemberByName", BSTR, c_ulong),
    STDMETHOD(HRESULT, "DeleteMemberByDispID", c_long),
    STDMETHOD(HRESULT, "GetMemberProperties", c_long, c_ulong, POINTER(c_ulong)),
    STDMETHOD(HRESULT, "GetMemberName", c_long, POINTER(BSTR)),
    STDMETHOD(HRESULT, "GetNextDispID", c_ulong, c_long, POINTER(c_long)),
    STDMETHOD(HRESULT, "GetNameSpaceParent", POINTER(POINTER(IUnknown))),
]

IServiceProvider._methods_ = IUnknown._methods_ + [
    STDMETHOD(HRESULT, "RemoteQueryService", POINTER(GUID), POINTER(GUID), POINTER(POINTER(IUnknown))),
]

##############################################################################

class ShockwaveFlash:
    """Shockwave Flash"""
    _reg_clsid_ = '{D27CDB6E-AE6D-11CF-96B8-444553540000}'
    _com_interfaces_ = [IShockwaveFlash]
    _outgoing_interfaces_ = [_IShockwaveFlashEvents]


class FlashProp:
    """Macromedia Flash Player Properties"""
    _reg_clsid_ = '{1171A62F-05D2-11D1-83FC-00A0C9089C5A}'
    _com_interfaces_ = [IUnknown]


class FlashObjectInterface:
    """IFlashObjectInterface Interface"""
    _reg_clsid_ = '{D27CDB71-AE6D-11CF-96B8-444553540000}'
    _com_interfaces_ = [IFlashObjectInterface]

