
from pyowm import OWM

owm = OWM('2636cec816be0e8a422569c17fe5da0a')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Kiev')

print(observation)