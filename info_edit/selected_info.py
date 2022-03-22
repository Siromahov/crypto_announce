# mails
mails = []

# sleep
hours = []
minutes = []

int_h = [int(hour) for hour in hours]
int_m = [int(minute) for minute in minutes]

if len(int_h) > 0:
    sleep_all = [int_h[0] + (int_m[0] / 60)]

# currency
selected = []

commits = []
commit_time = []

all = [mails, int_h, int_m, selected]
