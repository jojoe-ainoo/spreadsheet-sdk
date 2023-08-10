# Spreadsheet Package

This package provides a spreadsheet backend supporting set and get operations on cells, along with formula evaluation.

## Installation

You can install this package using pip:

```bash
pip install ainoo-spreadsheet-sdk
```

## Usage

from spreadsheet.backend import Spreadsheet

# Create a new spreadsheet instance

spreadsheet = Spreadsheet()

# Set cell values

spreadsheet.setCellValue("A1", 13)
spreadsheet.setCellValue("A2", 14)
spreadsheet.setCellValue("A3", "=A1+A2")

# Get cell values

print(spreadsheet.getCellValue("A1")) # Output: 13
print(spreadsheet.getCellValue("A3")) # Output: 27
