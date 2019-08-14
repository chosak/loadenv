from distutils.sysconfig import get_python_lib
from setuptools import setup


setup(
    name='python-loadenv',
    url='https://github.com/chosak/python-loadenv',
    author='CFPB',
    author_email='tech@cfpb.gov',
    description='Automatically load environment variables into Python',
    version='0.0.1',
    py_modules=['loadenv'],
    data_files = [(get_python_lib(prefix=''), ['loadenv-init.pth'])],
    license='CC0',
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
