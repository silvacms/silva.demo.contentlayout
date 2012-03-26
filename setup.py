from setuptools import setup, find_packages
import os

version = '2.0dev'

tests_require = [
    'Products.Silva [test]',
    ]

setup(name='silva.demo.contentlayout',
      version=version,
      description="Silva Content Layout Demo templates",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Infrae',
      author_email='info@infrae.com',
      url='',
      license='GPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.demo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'silva.core.contentlayout',
      ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      )
