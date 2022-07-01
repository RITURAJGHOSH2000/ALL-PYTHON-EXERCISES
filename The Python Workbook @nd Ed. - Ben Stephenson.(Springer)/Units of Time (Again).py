secs = int(input('Enter the number of seconds: '))
days = int(secs / 86400)
secs = secs % 86400
hours = int(secs / 3600)
secs = secs % 3600
mins = int(secs / 60)
secs = int(secs % 60)
hours_format = str(hours).zfill(2)
mins_format = str(mins).zfill(2)
secs_format = str(secs).zfill(2)
print(
    f'The equivalent duration in D:HH:MM:SS format is {days}:{hours_format}:{mins_format}:{secs_format}')
