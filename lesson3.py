

"""
Goals
- Visualise our data
- Plot simple graphs from data.
- Plot multiple graphs in a single figure.
"""


DATA_PATH = 'data/inflammation-01.csv'
DELIMITER = ','

import numpy
import matplotlib.pyplot as plt

data = numpy.loadtxt(fname=DATA_PATH, delimiter=DELIMITER)
image = plt.imshow(data)
plt.savefig('data.png')

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.amin(data, axis=0))

fig.tight_layout()

plt.savefig('inflammation.png')
