"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

N = 4
qt506 = (15.045, 7.907, 2.631, 4.507 )
#men_std = (2, 3, 4, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
rects1 = ax.bar(ind, qt506, width, color='r')

qt511 = (13.328, 6.669, 2.512, 4.147 )
#women_std = (3, 5, 2, 3)
#rects2 = ax.bar(ind + width, women_means, width, color='g', yerr=women_std)
rects2 = ax.bar(ind + width, qt511, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Second',fontsize=15)
ax.set_title('Swap by qtquick',fontsize=15)
ax.set_xticks(ind + width / 2)
ax.set_yticks(ind + 14)
ax.set_xticklabels(('total', 'text', 'svg', 'png'),fontsize=15)

ax.legend((rects1[0], rects2[0]), ('QT5.6', 'QT5.11'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.1f' % float(height),
                ha='center', va='bottom',fontsize=13)

autolabel(rects1)
autolabel(rects2)

plt.savefig("barChart.jpg")
plt.show()
