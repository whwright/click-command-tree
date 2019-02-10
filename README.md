click-command-tree
==================

`click-command-tree` is a [click](https://github.com/pallets/click) plugin to show the command tree of your CLI

Installation
------------

```
pip install click-command-tree
```

Tested against Python 3.4, 3.5, and 3.6 and click >= 5.0

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
└── tree

```
