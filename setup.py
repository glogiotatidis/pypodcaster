from setuptools import setup, find_packages

setup(
    name='pypodcaster',
    version='0.7',
    packages=find_packages(),
    url='http://github.com/mantlepro/pypodcaster',
    license='MIT',
    author='mantlepro',
    author_email='mantlepro@gmail.com',
    description='Generate podcast feed from mp3 files',
    package_data={'pypodcaster': ['templates/*']},
    entry_points = {
        'console_scripts': ['pypodcaster = pypodcaster.__main__:main']
    }
)
