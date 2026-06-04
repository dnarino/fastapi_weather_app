import datetime
from typing import Optional, Tuple

# In-memory database
__cache = {}
LIFETIME_IN_HOURS = 1.0
MAX_CACHE_SIZE = 1000  # Fail-safe: limits maximum memory usage

def get_weather(city: str, state: Optional[str], country: str, units: str) -> Optional[dict]:
    key = __create_key(city, state, country, units)
    data = __cache.get(key)
    if not data:
        return None

    # Lazy Deletion: Check expiration ONLY when we access the data
    dt = datetime.datetime.now() - data['time']
    if dt / datetime.timedelta(minutes=60) >= LIFETIME_IN_HOURS:
        del __cache[key]  # Clean it up immediately
        return None

    return data['value']

def set_weather(city: str, state: Optional[str], country: str, units: str, value: dict):
    key = __create_key(city, state, country, units)
    __cache[key] = {
        'time': datetime.datetime.now(),
        'value': value
    }

    # Bounded Cache: Evict the oldest key if we exceed the limit
    # Python 3.7+ dictionaries maintain insertion order, making this O(1)
    if len(__cache) > MAX_CACHE_SIZE:
        oldest_key = next(iter(__cache))
        del __cache[oldest_key]

def __create_key(city: str, state: Optional[str], country: str, units: str) -> Tuple[str, str, str, str]:
    if not city or not country or not units:
        raise ValueError('City, country, and units are required')  # Fail-fast with specific exception

    if not state:
        state = ''

    return city.strip().lower(), state.strip().lower(), country.strip().lower(), units.strip().lower()
