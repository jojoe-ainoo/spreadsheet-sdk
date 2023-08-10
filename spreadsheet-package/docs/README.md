# Spreadsheet Package

This package provides a spreadsheet backend supporting set and get operations on cells, along with formula evaluation.

## Installation

You can install this package using pip:

```bash
pip install spreadsheet-package==0.1
```

## Usage

from spreadsheet.backend import Spreadsheet

# Create a new spreadsheet instance

spreadsheet = Spreadsheet()

# Set cell values

spreadsheet.set_cell_value("A1", 13)
spreadsheet.set_cell_value("A2", 14)
spreadsheet.set_cell_value("A3", "=A1+A2")

# Get cell values

print(spreadsheet.get_cell_value("A1")) # Output: 13
print(spreadsheet.get_cell_value("A3")) # Output: 27
