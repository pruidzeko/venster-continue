# -*- coding: cp1251 -*-
# Copyright Maxim Kolosov 2012 pyirrlicht@gmail.com
# http://venster-continue.googlecode.com
# BSD license

def main():
	from oleones import OLE1C, MSScriptControl, vbs_code
	ones = OLE1C(
		ole_id = 'V77S',
		monopoly = True,
		db = '"C:\\Program Files\\1Cv77\\1SBDemo"',
		user_directory = '',
		user = 'admin',
		pwd = '',
		flags = '',# flags can be 'NO_SPLASH_SHOW'
		auto_init = False
	)
	if not ones.Initialize():
		print('ERROR Initialize RMTrade with parameters %s' % ones.params)
	else:
		print('class V1CEnterprise')
		print(ones)
		print('database parameters')
		print(ones.params)
		print('COM object Application')
		print(dir(ones.app))
		n = ones.ExecuteBatch('v1="";InputString(v1,"Справочник.Номенклатура",100);')
		n = ones.CreateObject('Справочник.Номенклатура')
		print('Reference')
		print(dir(n))
		print('Choose result')
		print(n.Choose('Select item', ''))
		n.Currentltem()
		n.SelectItems()
		f = open('test_productions.txt', 'w')
		while n.GetItem():
			f.write('item | ' + repr(n.FullCode()) + ' | ' + n.FullDescr())
		f.close()
		# extended functional
		script = MSScriptControl()
		script.AddObject('app', ones.app._comobj)
		script.AddCode(vbs_code)
		rp = script.Eval('object_pointer("Reference.Номенклатура")')
		script.AddObject('pointer', rp._comobj)
		if script.Eval('SelectItems'):
			print('count productions %d' % script.Eval('object_count("Reference.Номенклатура")'))
			while script.FastEval('GetItem'):
				print('code production %s' % repr(script.FastEval('Code')))
				print('full code production %s' % repr(script.FastEval('FullCode')))
				print('level production %d' % script.FastEval('Level'))
				print('is group production %d' % script.FastEval('IsGroup'))
				print('description production %s' % script.FastEval('Description'))
				print('description production %s' % script.FastEval('Description'.encode('cp1251'))
		script.ExecuteStatement('app.ExitSystem 0')
		script.Reset()
		del script

if __name__ == '__main__':
	main()
