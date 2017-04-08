# -*- coding: utf-8 -*-


import re


class my_app:


	header = []
	
	
	def __init__(self,url=(),fvars={}):
		self._urls = urls
		self._fvars = fvars
		
		
	def __call__(self,environ,start_response):
		self._status = '200 OK'
		del self.header[:]
		
		
		result = self_delegate(environ)
		start_response(self._status,self.headers)
		
		
		if isinstance(result,basestring):
			return iter([result])
		else:
			return iter(result)
	
	
	def _delegate(self,environ):
		path = environ['PATH_INFO']
		method = environ ['REQUEST_METHOD']
		
		
		for pattern ,name in self._urls:
			m = re.match ('^' +pattern +'$', path)
			if m :
				
				args = m.groups()
				funcname = method.upper()
				kclass = self._fvars.get(name)
				if hasattr(kclass,funcname):
					func = getattr(kclass,funcname)
					return func(klass(),*args)
		return self._notfound()
		
		
    def _notfound(self):
		self._status = '404 NOT FOUND'
		self.header("Content-type','text/plain')
		return "Not Found/n"
		
		
	@classmethod 
	def header(cls,name,value):
		cls.header.append((name,value))
				
				
				
