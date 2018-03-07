import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time


class PlotHist():

    def __init__(self, color):
        self.color = color

    def plot(self, tup_list):
        plt.cla()
        tup_list = sorted(tup_list, key=lambda x: x[1], reverse=True)
        x = range(len(tup_list))
        y = [i[1] for i in tup_list]
        plt.bar(x,y)
        plt.xticks(rotation=70)
        ax = plt.gca()
        ax.set_xticks(x)
        ax.set_xticklabels([i[0] for i in tup_list])
        fig = matplotlib.pyplot.gcf()
        #fig.set_size_inches(5.5, 4.5)
        fig.tight_layout()
        plt.pause(3)


if __name__ == '__main__':
    tup_list = [('hash', 10), ('test', 3), ('now', 6), ('now2', 6)]
    PlotHist().plot(tup_list)
    time.sleep(3)
    tup_list = [('hooot', 30), ('test', 3), ('now', 6)]
    PlotHist().plot(tup_list)
