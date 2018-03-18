# -*- coding:utf-8 -*-

import template
import file_utils

class cmake_builder(object):
	def __init__(self, builder):
		self.builder = builder

	def gen_target(self):
		self.gen_projects()
		self.gen_solution()

	def gen_projects(self):
		for project in self.builder.iter_project():
			self.gen_project(project)

	def gen_project(self, project):
		args = {}
		args['project_name'] = project.name
		args['generator'] = self.gen_project_generator(project)
		args['source_files'] = self.gen_source_files(project)
		args['include_files'] = self.gen_include_files(project)


		file_name = self.builder.target.join('%s.cmake'%(project.name))
		file_utils.gen_file('project.txt', file_name, args)

	def gen_source_files(self, project):
		files = []
		for name, info in project.iter_map('win', 'sources'):
			files.append(name.relative_to(self.builder.target))

		return '\r\n\t'.join(files)

	def gen_include_files(self, project):
		return ''

	def gen_project_generator(self, project):
		if isinstance(project, template.lib):
			return 'add_library'
		elif isinstance(project, template.exe):
			return 'add_executable'

	def gen_solution(self):
		args = {}
		args['sln_name'] = self.builder.args.sln_name
		args['projects'] = self.gen_solution_project_include()

		target = self.builder.target.join('CMakeLists.txt')
		file_utils.gen_file('cmake_sln.txt', target, args)

	def gen_solution_project_include(self):
		result = []
		for builder in self.builder.iter_project():
			result.append('include(%s.cmake)'%(builder.name))

		return '\n'.join(result)