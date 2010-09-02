from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='zojax.django.widgets.thumbnail',
      version=version,
      description="Widgets for images with thumbnails.",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Anatoly Bubenkov',
      author_email='bubenkoff@gmail.com',
      url='',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'':'src'},
      namespace_packages=['zojax', 'zojax.django', 'zojax.django.widgets'],
      include_package_data=True,
      zip_safe=False,
      extras_require = dict(
        test = []
        ),
      install_requires=[
          'setuptools',
          'sorl-thumbnail',
          'django-form_utils'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      dependency_links = [],
      )
