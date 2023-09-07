import pandas as pd
import numpy as np


def cleanup_tuple(tup):
    """workaround difficulty cleaning extract tuple + format match scoring result
    fix 1 -- instead of checking if tup is None or np.nan separately, us pd.isnull(tup) which handles both cases
    fix 2 -- instead of using pd.isnull(tup), us typ is None or np.isnan(tup) which is faster
    fix 3 -- instead of using round(float(tup[1]), 0), use int(tup[1]) to convert score to integer which is faster
    fix 4 -- replace  if tup is None or np.isnan(tup) with if pd.isnull(tup) to handle both cases
    """

    # Handle None and np.nan directly
    if tup is None or tup == np.nan:  # np.isnan(tup) can't convert all
        return np.nan

    # Handle the case where the tuple is wrapped inside a list
    if isinstance(tup, list):
        if not tup:
            return np.nan
        tup = tup[0]

    # Ensure that the extracted item is a tuple
    if not isinstance(tup, tuple):
        return np.nan

    title = tup[0]
    score = str(int(tup[1]))
    return f"{title}, {score}%"
