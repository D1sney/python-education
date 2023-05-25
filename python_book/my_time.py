import time
result=time.localtime(time.time())

def my_time():
    if result.tm_min<10:
        min=f'0{result.tm_min}'
    else:
        min=result.tm_min
    if result.tm_mon<10:
        mon=f'0{result.tm_mon}'
    else:
        mon=result.tm_mon
    if result.tm_hour<10:
        hour=f'0{result.tm_hour}'
    else:
        hour=result.tm_hour
    if result.tm_mday<10:
        day=f'0{result.tm_mday}'
    else:
        day=result.tm_mday
    
    return f'{hour}:{min} {day}.{mon}.{result.tm_year}'
print(my_time())
print(time.localtime(time.time()))