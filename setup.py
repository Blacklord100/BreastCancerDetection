from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import BreastCancerDetection

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='BreastCancerDetection',
    version=BreastCancerDetection.__version__,
    url='https://github.com/Blacklord100/BreastCancerDetection',
    license='To be defined',
    author='Mithuran Gajendran',
    tests_require=['pytest'],
    #install_requires=['numpy==1.19.3',
    #                    'joblib>=1.0.0',
    #                    'pandas>=1.2.0',
    #                    'PyYAML>=5.3.1',
    #                    'scikit-learn>=0.24.0'
    #                    ],
    cmdclass={'test': PyTest},
    author_email='mithuran.gajendran@gmail.com',
    description='Breast Cancer Predicition',
    long_description=long_description,
    packages=find_packages(),
    #packages=['BreastCancerDetection'],
    include_package_data=True,
    platforms='any',
    test_suite='BreastCancerDetection.tests.test_BreastCancerDetection',
    # To be defined
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)