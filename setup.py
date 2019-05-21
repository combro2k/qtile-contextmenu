import setuptools

from distutils.core import setup

setup(
    name='qtile-contextmenu',
    version='0.1dev',
    packages=['qtilecontextmenu',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    entry_points = {
        'console_scripts': ['qtile-contextmenu=qtilecontextmenu.contextmenu:main'],
    },
    install_requires=[
        'qtile'
    ],
)
