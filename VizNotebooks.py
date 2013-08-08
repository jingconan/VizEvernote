from __future__ import print_function, division, absolute_import
from VizEvernote import EvernoteAnalyzer
import os
import os.path
import json


class NotebooksAnalyzer(object):
    def __init__(self, folder):
        self.notebooks = dict()
        self.analyzers = dict()
        self._load_notes(folder)

    def _load_notes(self, folder):
        for f in os.listdir(folder):
            print('load [%s]' % (f))
            f_path = os.path.join(folder, f)
            if os.path.isfile(f_path) and f.endswith('.json'):
                with open(f_path, 'r') as note_f:
                    notes = json.load(note_f)
                    nb_name = os.path.basename(f)
                    self.notebooks[nb_name] = notes
                    self.analyzers[nb_name] = EvernoteAnalyzer(notes)
    def _print(self):
        for k, v in self.notebooks.iteritems():
            print('notebook: ', k)
