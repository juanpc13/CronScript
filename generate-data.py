# THIS IS TRIGGER BY A CRON TIMMER BY FOLLOWING EXPRESSION
# m h  dom mon dow   command
# * * * * * /usr/bin/python3 /home/jcpleitez/CronScript/generate-data.py

import datetime

datetime_object = datetime.datetime.now()

# Open a file with access mode 'a'
file_object = open('/home/jcpleitez/CronScript/sample.txt', 'a')
# Append 'hello' at the end of file
file_object.write('hello using cron at ' + str(datetime_object) + '\n')
# Close the file
file_object.close()
