import pandas as pd
import numpy as np


def cleanup_tuple(tup):
    """
    cleanup_tuple(tup) -> str

    This function is designed to cleanup the text output from the fuzzywuzzy
    extract functions. It takes a tuple as input and returns a str with the
    title and the score. It handles None and np.nan, as well as the case where
    the tuple is wrapped inside a list. It also ensures that the extracted item
    is a tuple. If the input is not a tuple, it returns np.nan.

    Parameters
    ----------
    tup : tuple
        A tuple containing the title and the score

    Returns
    -------
    str
        A string containing the title and the score with a comma and a space
        separating them

    workaround difficulty cleaning extract tuple + format match scoring result
    fix 1 -- instead of checking if tup is None or np.nan separately, us pd.isnull(tup) which handles both cases
    performance
    """

    # Handle None and np.nan directly
    if pd.isnull(tup):
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
