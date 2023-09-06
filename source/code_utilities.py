import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import clean_00, clean_01, clean_02, clean_03, clean_04, clean_05, clean_06

test_tuple = ("Job Title", 90.0)
functions = [clean_00, clean_01, clean_02, clean_03, clean_04, clean_05, clean_06]

timers = {}
for idx in range(7):
    start_time = time.time()
    for idx_2 in range(0, 10_000_000):
        functions[idx].cleanup_tuple(test_tuple)
    duration = time.time() - start_time
    timers[idx] = round(duration, 2)

for key, value in timers.items():
    print(f"{key:>5}: {value:>20.2f}")
