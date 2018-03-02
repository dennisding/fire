# -*- coding:utf-8 -*-

class build(template.exe):
	def __init__(self):
		super(build, self).__init__('fire')

		self.add_source_dir('.', exclude_dir = 'platform')
		self.add_include_dir('.')

		self.add_macros('TEST')

		self.add_depends()

	def setup_ios(self):
		self.add_source_dir('platform/ios')

	def setup_win(self):
		self.add_source_dir('platform/window')

	def setup_android(self):
		self.add_source_dir('platform/android')
