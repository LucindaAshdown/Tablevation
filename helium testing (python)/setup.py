from setuptools import setup

setup(
	name = 'helium',
	version = '1.9.6',
	author = 'BugFree Software',
	author_email = 'contact@heliumhq.com',
	description = 'Simple web automation based on Selenium.',
	keywords = 'selenium web automation',
	url = 'http://heliumhq.com',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: Other/Proprietary License',
		'Topic :: Software Development :: Testing',
		'Topic :: Software Development :: Libraries',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Operating System :: MacOS :: MacOS X'
	],
	packages = [
		'bfs',
		'helium',
		'bfs.bfs10063',
		'bfs.bfs10143',
		'helium.bfs10063',
		'helium.bfs10143',
		'helium.bfs10155'
	],
	package_dir = {'helium': 'heliumlib/helium', 'bfs': 'heliumlib/bfs'},
	install_requires = [
		'selenium==3.0.1', 'pkcs1>=0.9.6',
		'decorator>=3.4.0', 'psutil>=0.6.1'
	],
	package_data = {
		'helium.bfs10155': ['*.py3'],
		'bfs.bfs10063': ['*.py3'],
		'bfs.bfs10143': ['*.py3'],
		'bfs': ['*.py3'],
		'helium.bfs10143': ['*.py3'],
		'helium.bfs10063': ['*.py3'],
		'helium': ['*.py3', 'data/*.*', 'data/macosx/webdrivers/*']
	},
	zip_safe = False
)