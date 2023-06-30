import datetime
dt = datetime.datetime.now()

time = int(dt.strftime('%I'))

def inserted_time(current_time, increase_by):
    current_time += increase_by
    if current_time > 12:
        current_time -= 12
    str(current_time)
    return current_time

print(inserted_time(time, ))