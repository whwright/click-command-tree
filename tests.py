import unittest
import sys
from contextlib import contextmanager
from io import StringIO

import click

from click_command_tree import _build_command_tree, _print_tree


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class CommandTreeTestCase(unittest.TestCase):
    def test_single_command_group(self):
        @click.group()
        def root():
            pass

        @root.command()
        def command_one():
            pass

        @root.command()
        def command_two():
            pass

        expected_output = """
root
├── command-one
└── command-two
"""[1:]  # strip off the first newline

        self._assert_correct_output(root, expected_output)

    def test_nested_command_groups(self):
        @click.group()
        def root():
            pass

        @root.group()
        def group_one():
            pass

        @group_one.command()
        def command_one_a():
            pass

        @group_one.command()
        def command_one_b():
            pass

        @group_one.command()
        def command_one_c():
            pass

        @root.group()
        def group_two():
            pass

        @group_two.group()
        def group_two_a():
            pass

        @group_two.group()
        def group_two_b():
            pass

        expected_output = """
root
├── group-one
│   ├── command-one-a
│   ├── command-one-b
│   └── command-one-c
└── group-two
    ├── group-two-a
    └── group-two-b
"""[1:]

        self._assert_correct_output(root, expected_output)


    def test_last_is_command(self):
        @click.group()
        def root():
            pass

        @root.group()
        def group_a():
            pass

        @group_a.command()
        def command_a_a():
            pass

        @root.group()
        def group_b():
            pass

        @group_b.command()
        def command_b_a():
            pass

        @root.group()
        def group_c():
            pass
        expected_output = """
root
├── group-a
│   └── command-a-a
├── group-b
│   └── command-b-a
└── group-c
"""[1:]

        self._assert_correct_output(root, expected_output)

    def test_single_command(self):
        @click.command()
        def root():
            pass

        expected_output = 'root\n'

        self._assert_correct_output(root, expected_output)

    def test_using_name_argument(self):
        @click.group(name='root-command')
        def root():
            pass

        @root.command(name='name-of-command')
        def thing():
            pass

        expected_output = """
root-command
└── name-of-command
"""[1:]

        self._assert_correct_output(root, expected_output)

    def _assert_correct_output(self, root, expected_output):
        with captured_output() as (out, err):
            tree = _build_command_tree(root)
            _print_tree(tree)

            self.assertEqual(expected_output, out.getvalue())
