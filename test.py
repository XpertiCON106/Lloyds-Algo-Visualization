import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(1974)

clabel = ["Cluster 1", "Cluster 2"]

print(clabel)
# Generate Data
num = 20
x, y = np.random.random((2, num))
print("x: " + str(x))
print("y: " + str(y))
labels = np.random.choice(clabel, num)
print("Labels: " + str(labels))
df = pd.DataFrame(dict(x=x, y=y, label=labels))

groups = df.groupby('label')

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, label=name)
ax.legend()

plt.show()
