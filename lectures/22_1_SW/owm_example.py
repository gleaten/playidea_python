import pickle 
import pyowm 

# save
# my_owm_key = "my_key here!!"
# with open('my_owm_key.pickle', 'wb') as f:
#     pickle.dump(my_owm_key, f, pickle.HIGHEST_PROTOCOL)

# load
with open('my_owm_key.pickle', 'rb') as f:
    my_key = pickle.load(f)
    
# print(my_key)

from pyowm import OWM
from pyowm.utils import config 
from pyowm.utils import timestamps

owm = OWM(my_key)
mgr = owm.weather_manager()

observation = mgr.weather_at_place("Seoul,KR")
w = observation.weather 
# print(dir(observation))
print(w.detailed_status)
print(w.wind())
print(w.temperature('celsius'))
print(w.rain)