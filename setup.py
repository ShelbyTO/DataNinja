# setup.py

from setuptools import setup, find_packages

setup(
    name='DataNinja',
    version='0.5',
    description='A comprehensive data analysis and visualization toolkit.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    author='Nicolas Prieur',
    author_email='pu-zle@live.fr',
    url='https://github.com/ShelbyTO/DataNinja',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'missingno',
        'ydata-profiling'
    ],
)
