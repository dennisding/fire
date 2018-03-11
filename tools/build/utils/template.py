# -*- coding:utf-8 -*-

import path
import inspect

import os.path

class project(object):
	root = None # set by builder!!!!
	def __init__(self, name = None):
		self.name = name or self.gen_name()

		self.sources = {}
		self.includes = {}
		self.macros = []
		self.depends = set()

		self.source_root = None
		self.include_root = None

	def set_roots(self, source_root = None, include_root = None):
		self.source_root = self.root.join(source_root)
		self.include_root = self.root.join(include_root)

	def gen_name(self):
		return self.root.split()[-1]

	def add_source_dir(self, dir, excludes = ()):
		dir = self.root.join(dir)
		files = self.scan_dir(dir, ('.cpp', '.cxx', '.c'), excludes)
		self.sources.update(files)

	def add_include_dir(self, dir, excludes =()):
		dir = self.root.join(dir)
		files = self.scan_dir(dir, ('.h', '.hpp'), excludes)
		self.includes.update(files)

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
		self.depends.update(depends)

	def gen_cmake_file(self):
		pass

class lib(project):
	def __init__(self, name = None):
		super(lib, self).__init__(name)

class exe(project):
	def __init__(self, name = None):
		super(exe, self).__init__(name)
