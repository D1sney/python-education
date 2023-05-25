import time

days=0
hours=0
minutes=0
seconds=0

x=1970*365.25*86400+time.time()
# x=float(input('Введите количество секунд '))
days+=(x//86400)
hours+=((x%86400)//3600)
minutes+=(((x%86400)%3600)//60)
seconds+=(((x%86400)%3600)%60)

if days==0 and hours==0 and minutes==0:
    print(f'{seconds:.0f} seconds.')
if days==0 and hours==0:
    print(f'{minutes:.0f} minutes, {seconds:.0f} seconds.')
if days==0:
    print(f'{hours:.0f} hours, {minutes:.0f} minutes, {seconds:.0f} seconds.')
else:
    print(f'{days:.0f} days, {hours:.0f} hours, {minutes:.0f} minutes, {seconds:.0f} seconds.')

print(738981/365.25)
print(time.time()/(86400*365.25)+1970)
print(time.time())
print(time.gmtime(0))
print(time.localtime(0))
print(time.time_ns())