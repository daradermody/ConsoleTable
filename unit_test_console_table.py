#!/usr/bin/env python
from StringIO import StringIO

import sys
import unittest2
from mock import patch

from console_table import ConsoleTable


class EnmUserUnitTests(unittest2.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_console_table(self, output_mock):
        expected_value = "\n".join([
            "|     Heading 1      |     Heading 2      |",
            "-------------------------------------------",
            "|       Cell 1       |Subcell 1|Subcell 2 |"
        ]) + "\n"

        table = ConsoleTable()
        table.print_entry("Heading 1", "Heading 2")
        table.print_row_separator()
        table.print_entry("Cell 1", ("Subcell 1", "Subcell 2"))

        self.assertEqual(output_mock.getvalue(), expected_value)

    @patch('sys.stdout', new_callable=StringIO)
    def test_console_table_with_config(self, output_mock):
        expected_value = "\n".join([
            "      1 x 4    = 40  ",
            "      5 x 4    = 20  ",
            "    foo x bar  = foobar"
        ]) + "\n"

        table = ConsoleTable(row_format="{:>} x {} = {}", column_widths=(7, 4), subcell_delimiter="x")
        table.print_entry("1", "4", "40")
        table.print_entry("5", "4", "20")
        table.print_entry("foo", "bar", "foobar")

        self.assertEqual(output_mock.getvalue(), expected_value)


if __name__ == "__main__":
    unittest2.main(verbosity=2)
