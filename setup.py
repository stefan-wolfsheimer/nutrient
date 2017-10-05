from setuptools import setup

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(name='nutrient',
      version='0.1',
      description='',
      long_description=long_description,

      url='http://github.com/TODO',
      author='Stefan Wolfsheimer',
      author_email='stefan.wolfsheimer@gmail.com',
      license='MIT',

      packages=['nutrient'],
      install_requires=[],
      zip_safe=False,

      entry_points={
        'console_scripts': [
            'nutrient = nutrient.main:main'
        ] })

