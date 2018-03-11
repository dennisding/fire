# -*- coding:utf-8 -*-

import os
import path

import template

class builder(object):
	def __init__(self, args):
		self.args = args

		self.prepare_args()

	def prepare_args(self):
		self.source = path.path(self.args.source)
		self.make_file = path.path(self.args.target)

	def build(self):
		self.scan_builders()
		self.prepare_builders()
		self.gen_cmake_files()

		print 'builders', self.builders
		print 'files', self.builders['fire'].sources
		print 'includes', self.builders['fire'].includes

	def scan_builders(self):
		self.builders = {} # {name:builder}

		root = path.path(self.source)
		def _filter(path):
			return os.path.basename(path) == 'build.py'

		for name in root.iter_file(_filter):
			builder = self.gen_project_builder(name)

			self.builders[builder.name] = builder

	def gen_project_builder(self, file_name):
		env = {}
		env['template'] = template

		file = open(str(file_name))
		exec file in env

		builder_type = env['build']
		builder_type.root = path.path(file_name.dir_name())
		builder = builder_type()

		platform_builder = getattr(builder, 'setup_%s'%(self.args.platform), None)
		platform_builder and platform_builder()

		return builder

	def prepare_builders(self):
		pass

	def gen_cmake_files(self):
		pass