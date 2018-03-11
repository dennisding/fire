# -*- coding:utf-8 -*-

class config(object):
	def __init__(self, project):
		self.project = project

		self.sources = {}
		self.includes = {}

		self.macros = {}
		self.depends = set()
