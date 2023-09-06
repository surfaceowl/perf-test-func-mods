import numpy as np


def cleanup_tuple(tup):
    """workaround difficulty cleaning extract tuple + format match scoring result"""

    # Handle None and np.nan directly
    if tup is None or (isinstance(tup, float) and np.isnan(tup)):
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
    score = str(round(float(tup[1]), 0))
    return f"{title}, {score}%"
