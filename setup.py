from setuptools import setup, find_packages, Extension

setup(
	name    = 'fib',
	version = '0.1.1',
	packages = find_packages(),
	license = 'GPL-2',
	classifiers = [ 'Developer Status :: 3 - Alpha',
					'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
					'Natural Language :: English',
					'Programming Language :: Python :: 3 :: Only',
					'Programming Language :: Python :: Implementation :: CPython'],
	ext_modules = [Extension('fib.fib', ['fib/fib.cpp'])]
	)
