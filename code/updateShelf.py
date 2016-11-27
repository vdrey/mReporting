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
cells['equity_val'] = {'worksheet':'All','cell':'E15'}
cells['fixed_val'] = {'worksheet':'All','cell':'E25'}
cells['cash_val'] = {'worksheet':'All','cell':'E32'}

# Account Values
cells['wfa_val'] = {'worksheet':'WFA','cell':'E8'}
cells['acorns_val'] = {'worksheet':'Acorns','cell':'E9'}
cells['robinhood_val'] = {'worksheet':'Robinhood','cell':'E8'}

# Category Percent
cells['equity_percent'] = {'worksheet':'All','cell':'E4'}
cells['fixed_percent'] = {'worksheet':'All','cell':'E18'}
cells['cash_percent'] = {'worksheet':'All','cell':'E28'}

# Asset Values
cells['LGMAX_val'] = {'worksheet':'WFA','cell':'E3'}
cells['LGRRX_val'] = {'worksheet':'WFA','cell':'E4'}
cells['VOO_val'] = {'worksheet':'Acorns','cell':'E4'}
cells['VB_val'] = {'worksheet':'Acorns','cell':'E5'}
cells['VWO_val'] = {'worksheet':'Acorns','cell':'E6'}
cells['VNQ_val'] = {'worksheet':'Acorns','cell':'E7'}
cells['IRDM_val'] = {'worksheet':'Robinhood','cell':'E2'}
cells['MSTX_val'] = {'worksheet':'Robinhood','cell':'E4'}
cells['SHY_val'] = {'worksheet':'Acorns','cell':'E2'}
cells['LQD_val'] = {'worksheet':'Acorns','cell':'E3'}
cells['DDF_val'] = {'worksheet':'Robinhood','cell':'E3'}
cells['CHKR_val'] = {'worksheet':'Robinhood','cell':'E5'}

# Number of shares
cells['LGMAX_shares'] = {'worksheet':'WFA','cell':'C3'}
cells['LGRRX_shares'] = {'worksheet':'WFA','cell':'C4'}
cells['VOO_shares'] = {'worksheet':'Acorns','cell':'C4'}
cells['VB_shares'] = {'worksheet':'Acorns','cell':'C5'}
cells['VWO_shares'] = {'worksheet':'Acorns','cell':'C6'}
cells['VNQ_shares'] = {'worksheet':'Acorns','cell':'C7'}
cells['IRDM_shares'] = {'worksheet':'Robinhood','cell':'C2'}
cells['MSTX_shares'] = {'worksheet':'Robinhood','cell':'C4'}
cells['SHY_shares'] = {'worksheet':'Acorns','cell':'C2'}
cells['LQD_shares'] = {'worksheet':'Acorns','cell':'C3'}
cells['DDF_shares'] = {'worksheet':'Robinhood','cell':'C3'}
cells['CHKR_shares'] = {'worksheet':'Robinhood','cell':'C5'}

# Morning Values
cells['morning_total_val'] = {'worksheet':'storage-morning','cell':'B2'}
cells['morning_equity_val'] = {'worksheet':'storage-morning','cell':'B6'}
cells['morning_fixed_val'] = {'worksheet':'storage-morning','cell':'B7'}
cells['morning_cash_val'] = {'worksheet':'storage-morning','cell':'B8'}
cells['morning_wfa_val'] = {'worksheet':'storage-morning','cell':'B3'}
cells['morning_acorns_val'] = {'worksheet':'storage-morning','cell':'B4'}
cells['morning_robinhood_val'] = {'worksheet':'storage-morning','cell':'B5'}
cells['morning_LGMAX_val'] = {'worksheet':'storage-morning','cell':'B10'}
cells['morning_LGRRX_val'] = {'worksheet':'storage-morning','cell':'B11'}
cells['morning_VOO_val'] = {'worksheet':'storage-morning','cell':'B12'}
cells['morning_VB_val'] = {'worksheet':'storage-morning','cell':'B13'}
cells['morning_VWO_val'] = {'worksheet':'storage-morning','cell':'B14'}
cells['morning_VNQ_val'] = {'worksheet':'storage-morning','cell':'B15'}
cells['morning_IRDM_val'] = {'worksheet':'storage-morning','cell':'B16'}
cells['morning_MSTX_val'] = {'worksheet':'storage-morning','cell':'B17'}
cells['morning_SHY_val'] = {'worksheet':'storage-morning','cell':'B18'}
cells['morning_LQD_val'] = {'worksheet':'storage-morning','cell':'B19'}
cells['morning_DDF_val'] = {'worksheet':'storage-morning','cell':'B20'}
cells['morning_CHKR_val'] = {'worksheet':'storage-morning','cell':'B21'}

# Morning Shares
cells['morning_LGMAX_shares'] = {'worksheet':'storage-morning','cell':'C10'}
cells['morning_LGRRX_shares'] = {'worksheet':'storage-morning','cell':'C11'}
cells['morning_VOO_shares'] = {'worksheet':'storage-morning','cell':'C12'}
cells['morning_VB_shares'] = {'worksheet':'storage-morning','cell':'C13'}
cells['morning_VWO_shares'] = {'worksheet':'storage-morning','cell':'C14'}
cells['morning_VNQ_shares'] = {'worksheet':'storage-morning','cell':'C15'}
cells['morning_IRDM_shares'] = {'worksheet':'storage-morning','cell':'C16'}
cells['morning_MSTX_shares'] = {'worksheet':'storage-morning','cell':'C17'}
cells['morning_SHY_shares'] = {'worksheet':'storage-morning','cell':'C18'}
cells['morning_LQD_shares'] = {'worksheet':'storage-morning','cell':'C19'}
cells['morning_DDF_shares'] = {'worksheet':'storage-morning','cell':'C20'}
cells['morning_CHKR_shares'] = {'worksheet':'storage-morning','cell':'C21'}

# Close shelf
cells.close()
