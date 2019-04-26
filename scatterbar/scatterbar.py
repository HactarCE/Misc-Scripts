#!/usr/bin/env python

# scatterbar.py (version 1)

# Copyright 2019 HactarCE (Andrew Farkas)
# This file is released under the MIT license.

# Data input is a CSV. Each row corresponds to one bar in the final chart. The
# bar consists of the linear average (mean) of the data points.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker


# This is the plot title. If you want to use double quotes in your title, put a
# backslash `\` before them. You can also leave these blank.
TITLE = ""
X_LABEL = "https://xkcd.com/833/"
Y_LABEL = "Quantity (cm)"

# Each file should have a title on the first line, and a single data point on
# all subsequent lines. The files must be in the same directory as the script.
# Put the names of the data files here:
DATA_FILES = r'''
infected.csv
uninfected.csv
'''

# For each color, you can use either a basic color name (such as 'blue') or a
# hexadecimal color, beginning with '#'. Google "hex color picker" to select hex
# colors.

# For each file, give a color for the rectangle. Specify only one color if you
# want to use the same color for all of them.
BAR_COLORS = r'''
red
blue
'''

# For each file, give a color for the dots. Specify only one color if you
# want to use the same color for all of them.
DOT_COLORS = r'''
darkred
darkblue
'''

# This is the Y coordinate of the bottom of the bar. You can leave it at `0`, or
# make it negative to give room for dots at Y=0.
BAR_BOTTOM = -0.4

# This determines how much to randomize X positions. Set it to `0` to keep them
# centered, or `0.9` to randomize them a lot.
X_VARIATION = 0.5

# This is the seed used to calculate dot X position. The same seed (and same
# data) will always produce the same dot positions, so you can change this to
# another integer to drastically change the dot X positions.
np.random.seed(0)

# This determines whether to draw "minor" tick marks. (`True` or `False`)
DO_MINOR_TICKS = False

# This determines whether to draw horizontal lines at each major and minor line
# respectively. Minor gridlines will only be shown if `DO_MINOR_TICKS` is
# `True`. (`True` or `False` each)
DO_MAJOR_GRID = True
DO_MINOR_GRID = True

# A pair (width, height) describing the size of the plot in centimeters.
FIGSIZE = (5, 5)


def get_bar_height(values):
    """Get the height of the bar, given a Numpy array of Y coordinates.

    By default, this is a simple mean, but feel free to modify it as needed.
    """
    return sum(values) / len(values)


# DO NOT MODIFY BELOW THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING


# Parse DATA_FILES into a list
if isinstance(DATA_FILES, str):
    DATA_FILES = list(filter(None, DATA_FILES.splitlines()))

# Parse BAR_COLORS into a list
if isinstance(BAR_COLORS, str):
    BAR_COLORS = list(filter(None, BAR_COLORS.splitlines()))
if len(BAR_COLORS) == 1:
    BAR_COLORS = np.full_like(DATA_FILES, BAR_COLORS[0])

# Parse DOT_COLORS into a list
if isinstance(DOT_COLORS, str):
    DOT_COLORS = list(filter(None, DOT_COLORS.splitlines()))
if len(DOT_COLORS) == 1:
    DOT_COLORS = np.full_like(DATA_FILES, DOT_COLORS[0])

fig, ax = plt.subplots(figsize=FIGSIZE)

headers = []
datasets = []

for filename in DATA_FILES:
    try:
        with open(filename) as f:
            lines = list(f)
            headers.append(lines[0])
            datasets.append(np.array(list(map(float, lines[1:]))))
    except Exception:
        print(f"Unable to load file {filename!r}. Make sure it exists and has the right format.")
        exit(1)

ax.bar(
    x=np.arange(len(datasets)),
    height=np.vectorize(get_bar_height)(datasets),
    bottom=BAR_BOTTOM,
    color=BAR_COLORS,
    zorder=2,
)

for i, dataset in enumerate(datasets):
    x = np.full_like(dataset, i)
    x += (np.random.rand(*dataset.shape) - 0.5) * X_VARIATION
    ax.scatter(
        x=x,
        y=dataset,
        color=DOT_COLORS[i],
        zorder=3,
    )


ax.set_title(TITLE)
ax.set_xticks(np.arange(len(headers)))
ax.set_xticklabels(headers)
ax.set_xlabel(X_LABEL)
ax.set_ylabel(Y_LABEL)
if DO_MINOR_TICKS:
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
if DO_MINOR_GRID or DO_MAJOR_GRID:
    if DO_MINOR_GRID:
        if DO_MAJOR_GRID:
            which = 'both'
        else:
            which = 'minor'
    else:
        which = 'major'
    ax.grid(
        b=True,
        which=which,
        axis='y',
        zorder=1,
    )

fig.savefig('out.png')
