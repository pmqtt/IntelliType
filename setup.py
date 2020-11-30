from setuptools import setup

setup(
    name='IntelliType',
    version='0.1',
    packages=['IntelliType'],
    url='https://github.com/pmqtt/IntelliType',
    license='Apache 2',
    author='michael burzan',
    author_email='',
    description='',
    install_requires = ['keyboard'],
    entry_points={
        'console_scripts': [
            'itt=IntelliType:run',
        ],
    }
)
