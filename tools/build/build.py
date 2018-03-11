# -*- coding:utf-8 -*-

import argparse

from utils import builder

def parse_args():
	parser = argparse.ArgumentParser(description = 'gen CMake file')

	parser.add_argument('source', nargs = '?', type = str, default = '../../src')
	parser.add_argument('target', nargs = '?', type = str, default = '../../temp/cmake')
	parser.add_argument('--config', type = str, default = 'configs')
	parser.add_argument('--platform', type = str, default = 'win')
	parser.add_argument('--sln_name', type = str, default = 'fire')

	return parser.parse_args()

def build():
	args = parse_args()

	b = builder.builder(args)

	b.build()

if __name__ == '__main__':
	build()