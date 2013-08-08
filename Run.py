#!/usr/bin/env python
import json
from VizEvernote import EvernoteAnalyzer, EvernoteVisualizer
from VizNotebooks import NotebooksAnalyzer
from VizNotebooks import NotebooksVisualizer
import matplotlib.pyplot as plt


def count():
    # notes = json.load(open('../data.json', 'r'))
    notes = json.load(open('/home/wangjing/Evernote-2013-07-24.json', 'r'))
    # notes = json.load(open('/home/wangjing/Public/Evernote-2013-July.json', 'r'))
    ve = EvernoteAnalyzer(notes)
    # ve.count('created', 'week')
    # ve.count('created', 'year')
    # ve.count('created', 'month')
    # ve.count('updated', 'week')
    # ve.count('updated', 'year')
    # ve.count('updated', 'month')
    ve.group_by_tags('created')
    ve.dump(open('./Evernote-2013-07-24-count.json', 'w'))
    # ve.dump(open('./Evernote-2013-July-count.json', 'w'))
    # ve.dump(open('./Evernote-2013-07-24-count2.json', 'w'))
    # import ipdb;ipdb.set_trace()
    # ve.monthly_count()
    # daily_evernotes(notes)


def viz():
    ve = EvernoteVisualizer()
    ve.load(open('./Evernote-2013-07-24-count.json', 'r'))
    # ve.load(open('./Evernote-2013-July-count.json', 'r'))
    # ve.plot()
    plt.figure()
    ve.plot_tags_t('created', 'month', 70)
    plt.show()


def test_notebooks():
    na = NotebooksAnalyzer('/home/wangjing/Public/EvernoteJSON/')
    print(na)
    na.precentage('created', 'month')
    na.dump(open('./Evernote-notebooks-ana.json', 'w'))

    nv = NotebooksVisualizer()
    nv.load(open('./Evernote-notebooks-ana.json', 'r'))
    nv.plot_precentage('created', 'month')


if __name__ == "__main__":
    # count()
    # viz()
    test_notebooks()
