from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='IntelliType',
    version='0.3.3',
    packages=['IntelliType'],
    url='https://github.com/pmqtt/IntelliType',
    license='Apache 2',
    author='michael burzan',
    author_email='',
    description='The goal of IntelliType is to help you automate text-based processes',
    install_requires = ['keyboard'],
    entry_points={
        'console_scripts': [
            'itt=IntelliType:run',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown'
)
