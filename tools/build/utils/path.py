# -*- coding:utf-8 -*-

import os.path

class path(object):
	def __init__(self, root = '', virtual = False):
		root = str(root)
		if not virtual and os.path.isdir(root):
			root = os.path.abspath(root)

		self.root = root

		self.tokens = self.split_path(root)

	def split_path(self, root):
		root = str(root)
		tokens = []

		base, name = os.path.split(root)
		while name:
			tokens.append(name)
			base, name = os.path.split(base)
		tokens.reverse()
		return tokens

	def split(self):
		return self.split_path(self.root)

	def __hash__(self):
		return hash(self.root)

	def __str__(self):
		return self.root

	def dir_name(self):
		return os.path.dirname(self.root)

	def join(self, name):
		return os.path.join(self.root, name)

	def relative_to(self, root):
		if isinstance(root, str):
			root = path(root)

		common = 0
		for first, second in zip(self.tokens, root.tokens):
			if first != second:
				break
			common += 1

		tokens = self.tokens[common:]
		for i in xrange(len(root.tokens) - common):
			tokens.insert(0, '..')

		return '/'.join(tokens)

	def iter_file(self, filter = None):
		filter = filter or (lambda a: True)

		for root, dirs, files in os.walk(self.root):
			if '.svn' in dirs:
				dirs.remove('.svn')

			if '.git' in dirs:
				dirs.remove('.git')

			for name in files:
				file_name = os.path.join(self.root, root, name)
				if filter(file_name):
					yield path(file_name)

