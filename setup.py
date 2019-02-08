from setuptools import setup

setup(
    name='click-command-tree',
    version='0.1.0',
    py_modules=['click_command_tree'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [click_command_tree]
        tree=click_command_tree:tree
    ''',
)
