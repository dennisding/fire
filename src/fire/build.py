# -*- coding:utf-8 -*-

from utils import template

class build(template.exe):
	def __init__(self):
		super(build, self).__init__('fire')

		self.add_source_dir('.', excludes = ('platform',))
		self.add_include_dir('.')

		self.add_macros('TEST')

	def setup_ios(self):
		self.add_source_dir('platform/ios')

	def setup_win(self):
		self.add_source_dir('platform/window')

	def setup_android(self):
		self.add_source_dir('platform/android')
