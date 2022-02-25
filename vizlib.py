from collections import defaultdict
import pandas as pd
import numpy as np

COLORS = ['steelblue', 'peru', 'red', 'limegreen', 'yellow', 'blue', 'darkgreen', 'orange', 'magenta']

def viz_schedule(avail, b, n):
    n_filter = n.X.astype(bool)
    b_filter = b.X.astype(bool)
    a_filter = ~avail.astype(bool)

    def color_col(df):
        c_dict = defaultdict(lambda:'brown', zip(avail.columns, COLORS))
        df2 = df.copy(deep=True)
        df2[a_filter] = 'background-color: gray'
        for i, (colname, series) in enumerate(df2.items()):
            color = f"background-color: {c_dict[colname]}"
            series[(n_filter+b_filter)[:,i]] = color
        return df2

    schedule = pd.DataFrame(np.zeros(avail.shape), columns=avail.columns)
    schedule.iloc[:,:] = ""
    schedule[n_filter] = "N"
    schedule[b_filter] = "B"
    schedule[a_filter] = "-"
    return schedule.style.apply(color_col, axis=None)