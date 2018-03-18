# -*- coding:utf-8 -*-

import re
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
		if source_root:
			self.source_root = self.root.join(source_root)
		if include_root:
			self.include_root = self.root.join(include_root)

	def gen_name(self):
		return self.root.split()[-1]

	def add_source_dir(self, dir, excludes = ()):
		files = self.scan_dir(dir, ('.cpp', '.cxx', '.c'), excludes)
		self.current_config.sources.update(files)

	def add_include_dir(self, dir, excludes =()):
		files = self.scan_dir(dir, ('.h', '.hpp'), excludes)
		self.current_config.includes.update(files)

	def scan_dir(self, name, suffix, excludes):
		if name == '.':
			name = str(self.root)
		else:
			name = self.root.join(name)

		root = path.path(name)
		excludes = self.format_excludes(name, excludes)

		result = {}

		def _filter(path):
			return os.path.splitext(path)[-1] in suffix

		def _exclude(path):
			for exclude in excludes:
				if exclude(path):
					return True
			return False

		for file_name in root.iter_file(_filter):
			if not _exclude(file_name):
				result[file_name] = file_name

		return result

	def format_excludes(self, root, excludes):
		result = []
		for exclude in excludes:
			if isinstance(exclude, str):
				result.append(self.gen_string_exclude(root, exclude))

		return result

	def gen_string_exclude(self, root, exclude):
		patten_str = root + '/' + exclude
		patten_str = patten_str.replace('\\', '/')
		patten = re.compile(patten_str)

		def _filter(path):
			p = path.root.replace('\\', '/')
			print 'patten', patten_str
			print 'pppp', p
			return patten.match(p)

		return _filter

	def add_macros(self, *args, **kwds):
		pass

	def add_depends(self, *depends):
		self.current_config.depends.update(depends)

	def iter_map(self, config_name, name):
		for sub_config_name in ('normal', config_name):
			config = self.configs.get(sub_config_name, {})
			if not config:
				continue

			for key, value in getattr(config, name).iteritems():
				yield key, value

class lib(project):
	def __init__(self, name = None):
		super(lib, self).__init__(name)

class exe(project):
	def __init__(self, name = None):
		super(exe, self).__init__(name)

