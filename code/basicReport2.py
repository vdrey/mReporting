#!/usr/bin/python3

# This script gets the end of day total value, as well as the morning total value.

# The script then calculates the day's $ & % change, and sends it in an email.
# 
# In addition, the percentage changes for equity and fixed income is recorded.
import cell
import gmail3
import datetime
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


## Get the evening and morning total values
gSheet = "Other"
all_sheet = "All"
store_sheet = "storage-morning"
total_val_cell = "D2"
morning_total_cell = "B2"

morning_val_s = cell.getVal(gSheet, store_sheet, morning_total_cell)
evening_val_s = cell.getVal(gSheet, all_sheet, total_val_cell)

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
    </p>
  </body>
</html>
""" % (morning_val_s, evening_val_s, dollar_change, percent_change)


part1 = MIMEText(message, 'html')

parts = [part1]

## Send email
gmail3.sGmail(to, subj, parts)

