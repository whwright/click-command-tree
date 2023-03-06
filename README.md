click-command-tree
==================

`click-command-tree` is a [click](https://github.com/pallets/click) plugin to show the command tree of your CLI

[![build and test](https://github.com/whwright/click-command-tree/actions/workflows/build.yaml/badge.svg)](https://github.com/whwright/click-command-tree/actions/workflows/build.yaml)

Installation
------------

```
pip install click-command-tree
```

This is tested against Python versions 3.7 - 3.11 and (latest major release) click versions
5.x, 6.x, 7.x, 7.1.x, 8.0.x, and 8.1.x.


Example
-------

```python
from pkg_resources import iter_entry_points

import click
from click_plugins import with_plugins


@with_plugins(iter_entry_points('click_command_tree'))
@click.group()
def root():
    pass


@root.group()
def command_group():
    pass


@command_group.command()
def nested_command():
    pass


@root.command()
def standard_command():
    pass


if __name__ == '__main__':
    root()

```

```
↪ python example.py --help
Usage: example.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  command-group
  standard-command
  tree              show the command tree of your CLI


↪ python example.py tree
root
├── command-group
│   └── nested-command
├── standard-command
└── tree - show the command tree of your CLI
```
