# This script is used for updating a shelf file that is used to track worksheet & cell locations for various values.
import cell
import os
import shelve

# Check to see if a shelf already exists. If it does, delete it.
if os.path.exists('cell_store'):
    os.remove('cell_store')

# Create a shelf
cells = shelve.open('cell_store')

## Store the values
# The format for each value is {'worksheet':'something','cell':'cellthing'}

# Category Values
cells['total_val'] = {'worksheet':'All','cell':'D2'}
cells['equity_val'] = {'worksheet':'All','cell':'E14'}
cells['fixed_val'] = {'worksheet':'All','cell':'E22'}
cells['cash_val'] = {'worksheet':'All','cell':'E29'}

# Category Percent
cells['equity_percent'] = {'worksheet':'All','cell':'E4'}
cells['fixed_percent'] = {'worksheet':'All','cell':'E17'}
cells['cash_percent'] = {'worksheet':'All','cell':'E25'}








# Close shelf
cells.close()