import numpy as np
import pandas as pd

# ------------------------------------------------------------------------------

timestamps = pd.date_range("1970-01-01", "2019-08-15", freq='S')
df = pd.DataFrame({"timestamp": timestamps,
                   "normal": np.random.normal(size=len(timestamps)),
                   "log_normal": np.random.lognormal(size=len(timestamps)),
                   "exponential": np.random.exponential(size=len(timestamps)),
                   })
df.set_index("timestamp")

print("All memory allocations are done. Calculating means ...")

m1: float = df["normal"].mean()
m2: float = df["log_normal"].mean()
m3: float = df["exponential"].mean()
print(f"{m1}, {m2}, {m3}")

# ------------------------------------------------------------------------------

# Local Variables:
# mode:Python
# tab-width:4
# c-basic-offset:4
# End:
