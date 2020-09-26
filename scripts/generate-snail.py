import numpy as np
import pandas as pd
import pylab as plt
from os.path import join
from time import gmtime, strftime

# please use the join functon to avoid os path separator issue
DATA_SRC = join('data', 'csv', 'snail_data.csv')
RESULT_PATH = join('results')
LATEST_PATH = join(RESULT_PATH,'latest')
ARCHIVES_PATH = join(RESULT_PATH,'archives')
# if you're not french, change this
SEP = ";"


# Read the datas
# we supose french user so day is first in most of case
# change this if you work with US data
df = pd.read_csv(DATA_SRC, sep=SEP, index_col="date",
                 parse_dates=True, infer_datetime_format=True, dayfirst=True)

# add the day of week number
# Note that "lundi" is 0
df['dow'] = df.index.dayofweek
df['dow_angle'] = df['dow'] * (2 * np.pi / 7)


ax = plt.subplot(111, polar=True)
ax.plot(df['dow_angle'], df['value'], linewidth=1, linestyle='solid')

ax.set_xticks(2*np.pi*np.linspace(0, 6, 7)/7)
ax.set_xticklabels(['Lundi', 'Mardi', 'Mercredi', 'Jeudi',
                    'Vendredi', 'Samedi', 'Dimanche'])


# save as "latest"
plt.savefig(join(LATEST_PATH, 'latest.png'))
# save with timestamp
timestamp = "snail_at_{}.png".format(strftime("%Y%m%d", gmtime()))
plt.savefig(join(ARCHIVES_PATH, timestamp))
# Save as latest
plt.show()
