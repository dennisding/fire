# -*- coding:utf-8 -*-

import os
import path
import template
import file_utils
import cmake_builder

class builder(object):
	def __init__(self, args):
		self.args = args

		self.prepare_args()

	def prepare_args(self):
		self.source = path.path(self.args.source)
		self.target = path.path(self.args.target)

	def build(self):
		self.scan_builders()
		self.prepare_builders()
		#self.gen_cmake_files()
		self.gen_targets()

		print 'builders', self.builders
		print 'files', self.builders['fire'].configs

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

		for platform in ('win', 'ios', 'android'):
			builder.build_config(platform)

		return builder

	def prepare_builders(self):
		pass

	def gen_targets(self):
		#self.builder.gen_targets()
		builder = cmake_builder.cmake_builder(self)
		builder.gen_target()

	def iter_project(self):
		return self.builders.itervalues()

#	def gen_cmake_files(self):
#		for name, builder in self.builders.iteritems():
#			self.gen_builder_cmake_file(name, builder)
#
#		self.gen_solution()

#	def gen_builder_cmake_file(self, name, builder):
#		args = {}
#
#	def gen_solution(self):
#		args = {}
#		args['sln_name'] = self.args.sln_name
#
#		target = self.target.join('CMakeLists.txt')
#		file_utils.gen_file('cmake_sln.txt', target, args)
