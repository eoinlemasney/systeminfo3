'''
Created on 21 Feb 2018

@author: eoinlemasney
'''
from setuptools import setup

setup(name = "systeminfo",
      version= "0.1",
      description= "Basic system information for COMP30670",
      url = "",
      author = "Eoin Le Masney",
      author_email= "eoin.lemasney@ucdconnect.ie",
      licence = "GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )
