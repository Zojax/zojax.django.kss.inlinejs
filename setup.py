from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='zojax.django.socialauthentication.ui',
      version=version,
      description="Rich UI for zojax.django.socialauthentication.",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Andrey Fedoseev',
      author_email='andrey.fedoseev@zojax.com',
      url='',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'':'src'},
      namespace_packages=['zojax', 'zojax.django', 'zojax.django.socialauthentication'],
      include_package_data=True,
      zip_safe=False,
      extras_require = dict(
        test = []
        ),
      install_requires=[
          'setuptools',
          'zojax.django.socialauthentication',
          'zojax.django.blueprint',
          'zojax.django.jquery',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      dependency_links = [],
      )
