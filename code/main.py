import numpy as np

# Temporary setup to view data
data = np.load('../data/reddit.npz')
for file in data.files:
    print(file, data[file])

data = np.load('../data/reddit_adj.npz')
for file in data.files:
    print(file, data[file])