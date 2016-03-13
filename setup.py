from os import chdir,path
from sys import argv
from distutils.core import setup
import py2exe
chdir(path.dirname(argv[0]))
setup_file=argv.pop()
argv.append('py2exe')
setup(console=[setup_file])
