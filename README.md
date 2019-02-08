click-command-tree
==================

**WARNING**: This has really only been tested with python3 and click 6 and 7. I plan to do better testing and integrate CI so find all
possible versions this can be used with.

`click-command-tree` is a [click](https://github.com/pallets/click) plugin to show the command tree of your CLI

example:

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
  tree

↪ python example.py tree
root
├── command-group
│   └── nested-command
├── standard-command
└── tree

```
