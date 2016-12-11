#!/usr/bin/python3

# This script gets the total value of a portfolio as of 4am and stores it in the appropriate cell in the google sheet
import cell

gSheet = "Other"
all_sheet = 'All'
total_val_cell = 'D2'

# Get the current value
total_val = cell.getVal(gSheet, all_sheet, total_val_cell)

store_sheet = 'storage-morning'
morning_total_cell = 'B2'

# Set the morning value
cell.setVal(gSheet, store_sheet, morning_total_cell, total_val)
