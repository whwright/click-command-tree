import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='click-command-tree',
    version='1.1.0',
    description='click plugin to show the command tree of your CLI',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/whwright/click-command-tree',
    author='Harrison Wright',
    author_email='mail@harrisonwright.me',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    py_modules=['click_command_tree'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    setup_requires=[
        'flake8==3.7.5',
    ],
    entry_points='''
        [click_command_tree]
        tree=click_command_tree:tree
    ''',
)
