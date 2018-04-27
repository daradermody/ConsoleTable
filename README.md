# ConsoleTable
Python library for printing pretty tables with dynamic cells

# Usage
## Simple Table
Import and create a table object like this:

```python
from console_table import ConsoleTable

table = ConsoleTable()
table.print_entry("Heading 1", "Heading 2")
table.print_row_separator()
table.print_entry("Cell 1", ("Subcell 1", "Subcell 2"))

```

Which gives you this:

```commandline
|     Heading 1      |     Heading 2      |
-------------------------------------------
|       Cell 1       |Subcell 1|Subcell 2 |
```
As shown above, if one of the cell values provided is a tuple, the cell shall be broken up into subcells.

## Table Configuration
You can configure the table using the following parameters in the ConsoleTable constructor:

| Parameter         | Description   | Example  |
| ----------------- |:--------------|:--------:|
| row_format        | The format of the table row. Cell values are populated in "{}"s | <nobr>`"|{}|{}|"`</nobr> |
| column_widths     | The width of the columns. If a tuple is provided instead of an int, each integer shall be used as the width of each column.  If the length of this tuple is less than the number of "{}"s in the row_format string, the last number is used for the rest of the columns | <nobr>`(10, 5)`</nobr> |
| subcell_delimiter | The character(s) to separate subcells with | `":"` |

# How to Contribute
All you need to know is how to run the unit tests:

```
./unit_test_console_table.py
```