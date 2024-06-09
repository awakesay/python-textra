# Author: Yuji Omoto <awakesay@live.jp>
# Copyright (c) 2024-2024 Yuji Omoto
# License: BSD 3 clause

from setuptools import setup  # type: ignore
import textra

DESCRIPTION = "TexTra Web API"
NAME = 'textra'
AUTHOR = 'Yuji Omoto'
AUTHOR_EMAIL = 'awakesay@live.jp'
URL = 'https://github.com/awakesay/python-textra'
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/awakesay/python-textra'
VERSION = textra.__version__
PYTHON_REQUIRES = ">=3.10"

INSTALL_REQUIRES = [
    'requests=>2.32.0'
]

# EXTRAS_REQUIRE = {
#     'tutorial': [
#         'mlxtend>=0.18.0',
#         'xgboost>=1.4.2',
#     ]
# }

PACKAGES = [
    'textra'
]

CLASSIFIERS: list[str] = [
    # 'Intended Audience :: Science/Research',
    # 'License :: OSI Approved :: BSD License',
    # 'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3.7',
    # 'Programming Language :: Python :: 3.8',
    # 'Programming Language :: Python :: 3.9',
    # 'Programming Language :: Python :: 3 :: Only',
    # 'Topic :: Scientific/Engineering',
    # 'Topic :: Scientific/Engineering :: Visualization',
    # 'Topic :: Scientific/Engineering :: Artificial Intelligence',
    # 'Topic :: Multimedia :: Graphics',
    # 'Framework :: Matplotlib',
]

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
    #   extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
)
