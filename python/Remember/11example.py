
from pyowm import OWM

owm = OWM('2636cec816be0e8a422569c17fe5da0a')
monitoring = owm.weather_manager()
weather = monitoring.weather_at_place('Kiev')
print(weather)

lst = [int(i) for i in input().split()]

print(*lst[0])

