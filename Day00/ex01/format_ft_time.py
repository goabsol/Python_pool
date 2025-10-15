import datetime as dt
import time

now = time.time()
print(f"Seconds since January 1, 1970: {now:,} or {now:.2e} \
9 in scientific notation$")

date_time = dt.datetime.now()
print(f"{date_time.strftime('%b %d %Y')}")
