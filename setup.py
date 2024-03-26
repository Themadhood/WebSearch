from setuptools import setup, find_packages

#from my_pip_package import __version__


setup(
    name='TPC_WebSearch',
    version="1.0.0",#__version__,

    url='https://github.com/Themadhood/WebSearch',
    author='Themadhood Pequot',
    author_email='themadhoodpequot@gmail.com',

    packages=find_packages(),

    install_requires=[
        "google",#alows google search
        "requests",#web reader
        "beautifulsoup4",],

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
