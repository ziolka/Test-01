from setuptools import setup, find_packages

setup(
    name='clean-folder',
    version='01.00.02',
    description='Very useful file sorter',
    url='http://github.com/test',
    author='Kamzio',
    author_email='kamzio@example.com',
    license='MIT',
    packages=['clean_folder'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main',]}
)