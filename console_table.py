import re


class ConsoleTable(object):
    def __init__(self, row_format="|{:^}|{:^}|", column_widths=20, subcell_delimiter="|"):
        """
        :type row_format: string
        :param row_format: The format of the table row. Cell values are populated in "{}"s
        :type column_widths: int | tuple[int]
        :param column_widths: The width of the columns. If a tuple is provided, each integer shall be used as the width of each column.
                              If the length of this tuple is less than the number of "{}"s in the row_format string, it is padded using
                              the last number. For example, (20, 10) is padded to (20, 10, 10, 10) for row format string "{}|{}|{}|{}".
        :type subcell_delimiter: string
        """
        if not isinstance(column_widths, tuple):
            column_widths = (column_widths,)

        self._number_of_cells = len(re.findall(r"{.*?}", row_format))
        self.column_widths = self._right_pad_to_number(column_widths, self._number_of_cells)
        self.row_format = re.sub(r"{:?([<>^]?).*?}", r"{{:\1{}}}", row_format).format(*self.column_widths)
        self.subcell_delimiter = subcell_delimiter

    def _right_pad_to_number(self, l, number_to_reach):
        """
        :type l: list | tuple
        :type number_to_reach: int
        :rtype: list[any]
        """
        return l + type(l)([l[-1]]) * (number_to_reach - len(l))

    def print_entry(self, *cells):
        """
        :type cells: string | tuple[string]
        :param cells: The values used to populate the row. If one of the values is a tuple, the cell shall be broken up into subcells and
                      each value inputted. For example:
                          table = ConsoleTable(row_format="|{}|{}|", column_widths=23, subcell_delimiter="|")
                          table.print_entry("Cell 1", "Cell 2")
                          table.print_entry("Cell 1", ("Subcell 1", "Subcell 2"))

                      yields:
                          |        Cell 1         |        Cell 2         |
                          |        Cell 1         | Subcell 1 | Subcell 2 |
        """
        if len(cells) != self._number_of_cells:
            raise ValueError("Can not fit {} cells into table of width {}".format(len(cells), self._number_of_cells))

        cell_strings = []

        for column_number, entry in enumerate(cells):
            if isinstance(entry, tuple):
                entry = self._fit_into_cell(self.column_widths[column_number], entry)

            cell_strings.append(str(entry))

        print self.row_format.format(*cell_strings)

    def _fit_into_cell(self, cell_width, tuple_to_fit):
        """
        :type cell_width: int
        :type tuple_to_fit: tuple
        :rtype: string
        """
        subcell_width = (cell_width - len(tuple_to_fit) + 1) / len(tuple_to_fit)
        subcell = "{{:^{subcell_width}}}".format(subcell_width=subcell_width)
        return self.subcell_delimiter.join(subcell.format(cell) for cell in tuple_to_fit)

    def print_row_separator(self, repeating_character="-"):
        """
        :type repeating_character: string
        """
        print repeating_character * len(self.row_format.format(*self.column_widths))
