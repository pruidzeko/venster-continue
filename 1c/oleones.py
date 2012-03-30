# -*- coding: cp1251 -*-
# Copyright Maxim Kolosov 2012 pyirrlicht@gmail.com
# http://venster-continue.googlecode.com
# BSD license

import comtypes.client
from comtypes.automation import COMError

vbs_code = '''
Function object_pointer(name)
	Set object_pointer = app.CreateObject(name)
End Function
Function SelectItems
	SelectItems = pointer.SelectItems()
End Function
Function GetItem
	GetItem = pointer.GetItem()
End Function
Function Code
	Code = pointer.Code
End Function
Function Description
	Description = pointer.Description
End Function
Function Currentltem
	Currentltem = pointer.Currentltem()
End Function
Function FullCode
	FullCode = pointer.FullCode()
End Function
Function FullDescr
	FullDescr = pointer.FullDescr()
End Function
Function IsGroup
	IsGroup = Cbool(pointer.IsGroup())
End Function
Function Level
	Level = Cint(pointer.Level())
End Function
Function Locking
	Locking = Cbool(pointer.Locking())
End Function
Function DeleteMark
	DeleteMark = Cbool(pointer.DeleteMark())
End Function
Function object_count(name)
	Dim result
	result = 0
	Set object = app.CreateObject(name)
	If object.SelectItems() Then
		While object.GetItem()
			result = result + 1
		Wend
	End If
	object_count = result
End Function
'''

def com_error_to_file(err):
	f = open('error.txt', 'a')
	f.write(repr(err.args[0]))
	f.write('\n')
	try:
		f.write(err.args[1])
	except:
		f.write(repr(err.args[1]))
	f.write('\n')
	try:
		f.write(err.args[2][0].encode('cp1251'))#
	except:
		f.write(repr(err.args[2][0]))
	f.write('\n')
	try:
		f.write(err.args[2][1].encode('cp1251'))#
	except:
		f.write(repr(err.args[2][1]))
	f.write('\n')
	f.write(repr(err.args[2][2]))
	f.write('\n')
	f.write(repr(err.args[2][3]))
	f.write('\n')
	f.write(repr(err.args[2][4]))
	f.close()


class MSScriptControl:

	ScriptControl = None

	def __init__(self, *args, **kwargs):
		self.ole_id = kwargs.pop('ole_id', 'MSScriptControl.ScriptControl')
		self.ScriptLanguage = kwargs.pop('ScriptLanguage', 'VBScript')
		self.ScriptControl = comtypes.client.CreateObject(self.ole_id)
		self.ScriptControl.Language = self.ScriptLanguage
		code = kwargs.pop('code', None)
		if code:
			self.AddCode(code)

	def __del__(self):
		del self.ScriptControl

	def Reset(self):
		self.ScriptControl.Reset()

	def Run(self, proc):
		try:
			return self.ScriptControl.Run(proc)
		except COMError, err:
			print('Error Run %s' % proc)
			com_error_to_file(err)
			return None

	def AddCode(self, text):
		try:
			self.ScriptControl.AddCode(text)
		except COMError, err:
			print('Error AddCode %s' % text)
			com_error_to_file(err)

	def AddObject(self, name, obj):
		try:
			self.ScriptControl.AddObject(name, obj)
		except COMError, err:
			print('Error AddObject %s, %s' % (name, repr(obj)))
			com_error_to_file(err)

	def Eval(self, text):
		try:
			return self.ScriptControl.Eval(text)
		except COMError, err:
			print('Error Eval %s' % text)
			com_error_to_file(err)
			return None

	def ExecuteStatement(self, text):
		try:
			self.ScriptControl.ExecuteStatement(text)
		except COMError, err:
			print('Error ExecuteStatement %s' % text)
			com_error_to_file(err)

	def FastEval(self, text):
		return self.ScriptControl.Eval(text)


class OLE1C:

	app = None

	def __init__(self, *args, **kwargs):
		self.ole_id = kwargs.pop('ole_id', 'V1CEnterprise')
		if self.ole_id in ('V1CEnterprise', 'V77', 'V77S', 'V77L', 'V77M'):
			self.ole_id += '.Application'
		self.params = ''
		self.monopoly = kwargs.pop('monopoly', False)
		if self.monopoly:
			self.params += ' /m'
		self.db = kwargs.pop('db', '')
		if self.db:
			self.params += ' /d' + self.db
		self.user_directory = kwargs.pop('user_directory', '')
		if self.user_directory:
			self.params += ' /u' + self.user_directory
		self.user = kwargs.pop('user', '')
		if self.user:
			self.params += ' /n' + self.user
		self.pwd = kwargs.pop('pwd', '')
		if self.pwd:
			self.params += ' /p' + self.pwd
		self.flags = kwargs.pop('flags', '')
		self.auto_init = kwargs.pop('auto_init', True)
		try:
			self.app = comtypes.client.GetActiveObject(self.ole_id)
		except:
			self.app = comtypes.client.CreateObject(self.ole_id)#, dynamic=True)
		if not self.app:
			self.app = comtypes.client.CreateObject(self.ole_id)#, dynamic=True)
		if self.auto_init:
			if not self.Initialize():
				print('ERROR Initialize RMTrade with parameters %s' % self.params)

	def __del__(self):
		del self.app
		from gc import collect
		collect()

	def Initialize(self):
		return self.app.Initialize(self.app.RMTrade, self.params, self.flags)

	def CreateObject(self, *args):
		return self.app.CreateObject(*args)

	def EvalExpr(self, text):
		try:
			return self.app.EvalExpr(text)
		except COMError, err:
			print('Error EvalExpr %s' % text)
			com_error_to_file(err)

	def ExecuteBatch(self, text):
		try:
			return self.app.ExecuteBatch(text)
		except COMError, err:
			print('Error ExecuteBatch %s' % text)
			com_error_to_file(err)
