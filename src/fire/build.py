# -*- coding:utf-8 -*-

from utils import template

class build(template.solution):
	def __init__(self):
		super(build, self).__init__('fire')

		self.add_source_dir('.', exclude_dir = 'platform')
		self.add_include_dir('.')

	def setup_ios(self):
		pass

	def setup_win(self):
		self.add_source_dir('platform/window')

	def setup_android(self):
		pass