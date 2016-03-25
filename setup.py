from py2exe.build_exe import py2exe
from distutils.core import setup
import IPy
IPy.__version__
setup(windows=["GUI.py"],data_files=["data.json"])
#options={"py2exe":{"bundle_files":1}}