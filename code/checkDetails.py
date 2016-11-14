# Sends a monthly reminder email
import datetime
import gmail2

to = 'daniel7reynolds@gmail.com'
subj = 'Monthly Reminder'
message = """
This is the montly reminder to check the equity/bond percent in the all part of the google sheet.

Take a look at:

LGMAX
"""

gmail2.sGmail(to,subj,message)
