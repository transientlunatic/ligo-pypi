"""

This is a python-based installer for the lal, which is a
component of lalsuite.

Installer Maintainer: Daniel Williams <daniel.williams@ligo.org>

"""


try:
    from setuptools import setup
    from setuptools.command.install import install as SetuptoolsInstall
except ImportError:
    from distutils.core import setup

from subprocess import call
import os

from setuptools.command.install import install as SetuptoolsInstall


try:
    virtualenv =  os.environ['VIRTUAL_ENV']
    print("This installation is being completed within a virtual environment at {}".format(virtualenv))
except KeyError:
    virtualenv = None

def install_framelib():
    """
    Run the configure > make pipeline for the framelibrary
    """
    os.chdir("src")
    #print "Run the lal Bootstrap"
    #call(["autoreconf", "--install"])
    print "Run the lal Configuration"
    if virtualenv:
        call(["bash", "configure", "--silent", "--enable-silent-rules", "--prefix=/{}".format(virtualenv)])
    else:
        call(["bash", "configure", "--silent", "--enable-silent-rules"])
    print "Making lal"
    call(["make",  "-j", "--silent"])
    print "Installing lal"
    call(["make", "install", "--silent"])
    os.chdir("../../")

class MyInstall(SetuptoolsInstall):
    def run(self):
        SetuptoolsInstall.run(self)
        install_framelib()

#requirements = [
#    "numpy",
#    "healpy",
#    "h5py",
#]

requirements = []
        
setup(
    name='GWlal',
    version='0.0.1',
    description="A Pythonic installer for lal - part of lalsuite",
    # long_description=readme + '\n\n' + history,
    author="LIGO Collaboration / Daniel Williams",
    author_email='daniel.williams@ligo.org',
    url='https://git.ligo.org/daniel-williams/python-ligo',
    packages=[
         'lal',
    ],
    package_dir={'lal':
                 'src'},
    install_requires=requirements,
    cmdclass={'install': MyInstall},
    # license="GPLv3",
    zip_safe=True,
    keywords='ligo gravitational-waves',
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Science/Research',
    #     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    #     'Natural Language :: English',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.3',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    # ]
)
