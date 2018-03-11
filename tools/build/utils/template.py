# -*- coding:utf-8 -*-

import path
import config
import inspect

import os.path

class project(object):
	root = None # set by builder!!!!
	def __init__(self, name = None):
		self.name = name or self.gen_name()

		self.source_root = None
		self.include_root = None

		self.configs = {} # {name : configs}
		self.prepare_config('normal')

	def build_config(self, name):
		configer = getattr(self, 'setup_%s'%(name), None)
		if not configer:
			return

		self.prepare_config(name)
		configer()

	def prepare_config(self, name):
		conf = config.config(self)
		self.current_config = conf

		self.configs[name] = conf

	def set_roots(self, source_root = None, include_root = None):
		self.source_root = self.root.join(source_root)
		self.include_root = self.root.join(include_root)

	def gen_name(self):
		return self.root.split()[-1]

	def add_source_dir(self, dir, excludes = ()):
		dir = self.root.join(dir)
		files = self.scan_dir(dir, ('.cpp', '.cxx', '.c'), excludes)
		self.current_config.sources.update(files)

	def add_include_dir(self, dir, excludes =()):
		dir = self.root.join(dir)
		files = self.scan_dir(dir, ('.h', '.hpp'), excludes)
		self.current_config.includes.update(files)

	def scan_dir(self, name, suffix, excludes):
		root = path.path(name)

		result = {}

		def _filter(path):
			return os.path.splitext(path)[-1] in suffix

		def _exclude(path):
			return False

		for file_name in root.iter_file(_filter):
			if not _exclude(file_name):
				result[file_name] = file_name

		return result

	def add_macros(self, *args, **kwds):
		pass

	def add_depends(self, *depends):
		self.current_config.depends.update(depends)

	def gen_args(self):
		args = {}
		args['name'] = self.name

		return 'invalid.txt', args

class lib(project):
	def __init__(self, name = None):
		super(lib, self).__init__(name)

	def gen_args(self):
		_, args = super(lib, self).gen_args()

		return 'lib.txt', args

class exe(project):
	def __init__(self, name = None):
		super(exe, self).__init__(name)

	def gen_args(self):
		_, args = super(exe, self).gen_args()
		# add exe args

		return 'exe.txt', args
