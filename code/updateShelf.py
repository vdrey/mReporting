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

# Asset Values
cells['LGMAX_val'] = {'worksheet':'All','cell':'E5'}
cells['LGRRX_val'] = {'worksheet':'All','cell':'E6'}
cells['V00_val'] = {'worksheet':'All','cell':'E7'}
cells['VB_val'] = {'worksheet':'All','cell':'E8'}
cells['VWO_val'] = {'worksheet':'All','cell':'E9'}
cells['VNQ_val'] = {'worksheet':'All','cell':'E10'}
cells['IRDM_val'] = {'worksheet':'All','cell':'E11'}
cells['MSTX_val'] = {'worksheet':'All','cell':'E12'}
cells['SHY_val'] = {'worksheet':'All','cell':'E18'}
cells['LQD_val'] = {'worksheet':'All','cell':'E19'}
cells['DDF_val'] = {'worksheet':'All','cell':'E20'}

# Number of shares
cells['LGMAX_shares'] = {'worksheet':'All','cell':'C5'}
cells['LGRRX_shares'] = {'worksheet':'All','cell':'C6'}
cells['V00_shares'] = {'worksheet':'All','cell':'C7'}
cells['VB_shares'] = {'worksheet':'All','cell':'C8'}
cells['VWO_shares'] = {'worksheet':'All','cell':'C9'}
cells['VNQ_shares'] = {'worksheet':'All','cell':'C10'}
cells['IRDM_shares'] = {'worksheet':'All','cell':'C11'}
cells['MSTX_shares'] = {'worksheet':'All','cell':'C12'}
cells['SHY_shares'] = {'worksheet':'All','cell':'C18'}
cells['LQD_shares'] = {'worksheet':'All','cell':'C19'}
cells['DDF_shares'] = {'worksheet':'All','cell':'C20'}



# Close shelf
cells.close()