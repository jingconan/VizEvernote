from __future__ import print_function, division, absolute_import
from VizEvernote import EvernoteAnalyzer
from VizEvernote import EvernoteVisualizer
import os
import os.path
import json
import matplotlib.pyplot as plt
import numpy as np
from util import stackplot


class NotebooksAnalyzer(EvernoteAnalyzer):
    def __init__(self, folder):
        self.notebooks = []
        self.nb_data = dict()
        self.analyzers = dict()
        self.stat = dict()
        self._load_notes(folder)

    def _load_notes(self, folder):
        for f in os.listdir(folder):
            print('load [%s]' % (f))
            f_path = os.path.join(folder, f)
            if os.path.isfile(f_path) and f.endswith('.json'):
                with open(f_path, 'r') as note_f:
                    notes = json.load(note_f)
                    nb_name = os.path.basename(f).rsplit('.json')[0]
                    self.notebooks.append(nb_name)
                    self.nb_data[nb_name] = notes
                    self.analyzers[nb_name] = EvernoteAnalyzer(notes)
        self.stat['notebooks'] = self.notebooks

    def __str__(self):
        return 'Notebooks:\n%s' % ('\n'.join(self.notebooks))

    def precentage(self, t_type, resolution):
        p_data = []
        for nb in self.notebooks:
            gc = self.analyzers[nb].count(t_type, resolution)
            p_data.append(gc)

        # get all possible dates
        dates = set()
        for d in p_data:
            dates |= set(d.keys())

        stat_data = dict(zip(dates, [[] for k in dates]))
        for pd in p_data:
            for dt in dates:
                stat_data[dt].append(pd.get(dt, 0))

        self.stat['p_data_%s-%s' % (t_type, resolution)] = stat_data


class NotebooksVisualizer(EvernoteVisualizer):
    def plot_precentage(self, t_type, resolution):
        k = 'p_data_%s-%s' % (t_type, resolution)
        dates, precentages = self.sort_pair(self.stat[k])
        stackplot(plt.gca(), np.arange(len(precentages)), zip(*precentages),
                  self.stat['notebooks'], xtick_labels=dates, rotation=30)
