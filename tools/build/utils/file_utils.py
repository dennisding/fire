# -*- coding:utf-8 -*-

import string

import os.path

templates = {} # {name: template}

def create_file(name):
	return open(name, 'wb')

def gen_file(file_name, name, args):
	template = gen_template(file_name)

	content = template.safe_substitute(args)

	file = create_file(name)
	file.write(content)
	file.close()

def gen_template(name):
	template = templates.get(name)
	if template:
		return template

	path = os.path.join('files', name)

	template = string.Template(open(path).read())
	templates[name] = template
	return template
