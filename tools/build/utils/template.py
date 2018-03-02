# -*- coding:utf-8 -*-

class project(object):
	def __init__(self, name = None):
		self.name = name or self.gen_name()

		self.sources = []
		self.includes = []
		self.macros = []

	def gen_name(self):
		pass

	def add_source_dir(self, dir, exclude_dir = ()):
		pass

	def add_include_dir(self, dir):
		pass

	def add_macros(self, *args, **kwds):
		pass

	def add_depends(self, *depends):
		pass

	def gen_cmake_file(self):
		pass

class lib(object):
	def __init__(self, name = None):
		super(lib, self).__init__(name)

class exe(object):
	def __init__(self, name = None):
		super(exe, self).__init__(name)
