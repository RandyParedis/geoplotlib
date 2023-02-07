from setuptools import setup

setup(name='geoplotlib',
      use_2to3=True,
      packages=['geoplotlib'],
      version='0.3.3',
      description='python toolbox for geographic visualizations',
      author='Andrea Cuttone, Randy Paredis',
      author_email='andreacuttone@gmail.com, randy.paredis@uantwerpen.be',
      url='https://github.com/andrea-cuttone/geoplotlib',
      install_requires=['numpy>=1.12','pyglet>=1.2.4']
)
