from setuptools import setup

setup(name='RayTracing',
      version='0.1',
      description='Implementing a Ray Tracer',
      url='https://github.com/SBK78MC/raytrashing',
      author='raytrashing',
      packages=['RayTracing', 'RayTracing.Classes', 'RayTracing.Classes.Models'],
      zip_safe=False,
      setup_requires['numpy', 'matplotlib'])