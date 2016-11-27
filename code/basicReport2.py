#!/usr/bin/python3

# This script gets the end of day total value, as well as the morning total value.

# The script then calculates the day's $ & % change, and sends it in an email.
# 
# In addition, the percentage changes for equity and fixed income is recorded.
import cell
import gmail3
import datetime
import shelve
from email.mime.text import MIMEText

# Function for cleaning up dollar values, and converting into a number
def clean(val):
    # Split string
    val = list(val)
    # Remove $ and ,
    while '$' in val:
        val.remove('$')
    while ',' in val:
        val.remove(',')
    # Join string
    val = ''.join(val)
    # convert to float
    val = float(val)
    
    return val


## Get the evening total values, as well as equity, 
## fixed income, and cash values and percentages.
gSheet = "Other"
cells = shelve.open('cell_store')

# Total
morning_val_s = cell.getVal(gSheet, cells['morning_total_val']['worksheet'], cells['morning_total_val']['cell'])
evening_val_s = cell.getVal(gSheet, cells['total_val']['worksheet'], cells['total_val']['cell'])

# Category values & percents
equity_val_s = cell.getVal(gSheet, cells['equity_val']['worksheet'], cells['equity_val']['cell'])
equity_pct_s = cell.getVal(gSheet, cells['equity_percent']['worksheet'], cells['equity_percent']['cell'])

fixed_val_s = cell.getVal(gSheet, cells['fixed_val']['worksheet'], cells['fixed_val']['cell'])
fixed_pct_s = cell.getVal(gSheet, cells['fixed_percent']['worksheet'], cells['fixed_percent']['cell'])

cash_val_s = cell.getVal(gSheet, cells['cash_val']['worksheet'], cells['cash_val']['cell'])
cash_pct_s = cell.getVal(gSheet, cells['cash_percent']['worksheet'], cells['cash_percent']['cell'])

cells.close()

# Convert to number
morning_val = clean(morning_val_s)
evening_val = clean(evening_val_s)

## Calculate change in value

# Dollar change
dollar_change = evening_val - morning_val

# Percentage change
percent_change = 100*(evening_val - morning_val)/morning_val

## Category change


## Create email
now = datetime.datetime.now()
to = 'daniel7reynolds@gmail.com'
subj = 'Report for %s/%s/%s' % (str(now.month), str(now.day), str(now.year))
message = """\
<html>
  <head></head>
  <body>
    <p>The day started with a value across accounts of %s, and ended the day at %s.<br>
       <br>
       <br>
       Dollar Value Change: $%.2f<br>
       Percentage Change:    %.3f<br>
       <br>
       <br>
       <table border=".1">
         <tr>
           <th>Category</th>
           <th>Value</th>
           <th>Percent</th>
         </tr>
         <tr>  
           <td align="center">Equity</td>
           <td align="center">%s</td>
           <td align="center">%s</td>
         </tr>
         <tr>
           <td align="center">Fixed</td>
           <td align="center">%s</td>
           <td align="center">%s</td>
         </tr>
           <td align="center">Cash</td>
           <td align="center">%s</td>
           <td align="center">%s</td>
       </table>
    </p>
  </body>
</html>
""" % (morning_val_s, evening_val_s, dollar_change, percent_change, equity_val_s, equity_pct_s, fixed_val_s,
       fixed_pct_s, cash_val_s, cash_pct_s)


part1 = MIMEText(message, 'html')

parts = [part1]

## Send email
gmail3.sGmail(to, subj, parts)

