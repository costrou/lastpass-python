from distutils.core import setup
import os

long_description = """ lastpass-python is a python interface to the LastPass CLI"""

packages = []
for dirname, diranmes, filenames in os.walk('lastpass'):
    if '__init__.py' in filenames:
        packages.append(dirname.replace('/', '.'))

package_dir = {'lastpass': 'lastpass'}

setup(name='lastpass',
      version="0.0.1",
      description='Lastpass CLI Python Wrapper',
      url='https://github.com/costrou/newt-python',
      maintainer='Christopher Ostrouchov',
      maintainer_email='chris.ostrouchov+lastpass@gmail.com',
      license='LGPLv2.1+',
      platforms=['linux'],
      packages=packages,
      package_dir=package_dir,
      long_description=long_description)
