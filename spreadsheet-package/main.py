from spreadsheet.core import Spreadsheet

spreadsheet = Spreadsheet()
spreadsheet.set_cell_value("A1", 13)
spreadsheet.set_cell_value("A2", 14)
# print(spreadsheet.get_cell_value("A1"))
spreadsheet.set_cell_value("A3", "=A1+A2")
print(spreadsheet.get_cell_value("A3"))
# spreadsheet.set_cell_value("A5", "=A1+A6")
spreadsheet.set_cell_value("A7", "=A1*A2") 