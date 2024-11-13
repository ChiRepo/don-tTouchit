import platform as pf
import time
import datetime as dt
print(f'Completed on device: {pf.platform()}')
print(f'Process completed in {time.process_time()}(s)')

print(dt.datetime.now().strftime('%H:%M:%S'))