click-command-tree
==================

`click-command-tree` is a [click](https://github.com/pallets/click) plugin to show the command tree of your CLI

Installation
------------

```
pip install click-command-tree
```

This is tested against Python versions 3.8 - 3.12 and (latest major release) click versions
5.x, 6.x, 7.x, 7.1.x, 8.0.x, and 8.1.x.


Example
-------

```python
import importlib.metadata

import click
from click_plugins import with_plugins


@with_plugins(importlib.metadata.entry_points(group="click_command_tree"))
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


Releasing:
1. update `__version__` variable, and in `setup.py`
1. git commit new version
1. git tag -a {version}
1. git push origin master --tags
1. make publish-dist
1. go to github UI and turn tag into a release
