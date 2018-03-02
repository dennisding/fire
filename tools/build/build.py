# -*- coding:utf-8 -*-

import argparse

from utils import builder

def parse_args():
	parser = argparse.ArgumentParser(description = 'gen CMake file')

	parser.add_argument('source', metavar = 'source', type = str)
	parser.add_argument('target', metavar = 'target', type = str)
	parser.add_argument('--config', type = str, default = 'configs')

	return parser.parse_args()

def build():
	args = parse_args()

	builder = builder.builder(args)

	builder.build()

if __name__ == '__main__':
	build()