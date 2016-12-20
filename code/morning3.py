# This script updates all of the morning values
import shelve
import cell

# Create a list of values to update.
vals = ['total_val','equity_val','fixed_val','cash_val','wfa_val','acorns_val','robinhood_val','LGMAX_val','LGRRX_val',
        'VOO_val','VB_val','VWO_val','VNQ_val','IRDM_val','MSTX_val','SHY_val','LQD_val','DDF_val','LGMAX_shares','LGRRX_shares',
        'VOO_shares','VB_shares','VWO_shares','VNQ_shares','IRDM_shares','MSTX_shares','SHY_shares','LQD_shares','DDF_shares',
        'CHKR_val','CHKR_shares','equity_percent','fixed_percent','cash_percent','SO_val','SO_shares']

# Open the shelf
cells = shelve.open('cell_store')

# go value-by-value and update the morning value.
for item in vals:
    mItem = 'morning_' + item
    cell.setVal('Other', cells[mItem]['worksheet'], cells[mItem]['cell'], cell.getVal('Other', cells[item]['worksheet'],cells[item]['cell']))   
