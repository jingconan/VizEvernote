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
    # import ipdb;ipdb.set_trace()
    ve = EvernoteAnalyzer(notes)
    ve.count('created', 'week')
    ve.count('created', 'year')
    ve.count('created', 'month')
    ve.count('updated', 'week')
    ve.count('updated', 'year')
    ve.count('updated', 'month')
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

    plt.figure(figsize=(14, 8))
    ve.plot_count('created', 'week', width=0.5, tick_num=30, rotation=90)
    plt.savefig('../figures/created_week.png')

    plt.figure(figsize=(14,8))
    ve.plot_count('created', 'month', width=0.5, tick_num=None, rotation=90)
    plt.savefig('../figures/created_month.png')

    plt.figure(figsize=(14,8))
    ve.plot_count('created', 'year', width=0.5, tick_num=None, rotation=20)
    plt.savefig('../figures/created_year.png')

    plt.figure(figsize=(14,8))
    ve.plot_count('updated', 'week', width=0.5, tick_num=30, rotation=70)
    plt.savefig('../figures/updated_week.png')

    plt.figure(figsize=(14,8))
    ve.plot_count('updated', 'month', width=0.5, tick_num=None, rotation=70)
    plt.savefig('../figures/updated_month.png')

    plt.figure(figsize=(14,8))
    ve.plot_count('updated', 'year', width=0.5, tick_num=None, rotation=20)
    plt.savefig('../figures/updated_year.png')

    plt.figure(figsize=(14,8))
    ve.plot_tags_t('created', 'month', 70)
    plt.savefig('../figures/tags_created_month.png')

    # plt.figure(figsize=(14,8))
    # ve.plot_tags_t('created', 'week', 90)
    # plt.savefig('../figures/tags_created_week.png')

    plt.show()


def test_notebooks_created_month():
    # na = NotebooksAnalyzer('/home/wangjing/Public/EvernoteJSON/')
    # print(na)
    # na.count('created', 'month')
    # na.count('created', 'week')
    # na.count('updated', 'month')
    # na.count('updated', 'week')
    # na.dump(open('./Evernote-notebooks-ana.json', 'w'))

    nv = NotebooksVisualizer()
    nv.load(open('./Evernote-notebooks-ana.json', 'r'))
    plt.figure(figsize=(14,8))
    nv.area_plot('created', 'month', rotation=30)
    plt.savefig('../figures/area_created_month.png')

    plt.figure(figsize=(14,8))
    nv.area_plot('created', 'week', rotation=90, xtick_num=20)
    ylim = plt.gca().get_ylim()
    plt.ylim([0, ylim[1]])
    plt.savefig('../figures/area_created_week.png')

    plt.figure(figsize=(14,8))
    nv.area_plot('updated', 'month', rotation=30)
    ylim = plt.gca().get_ylim()
    plt.ylim([0, ylim[1]])
    plt.savefig('../figures/area_updated_month.png')

    plt.figure(figsize=(14,8))
    nv.area_plot('updated', 'week', rotation=90, xtick_num=20)
    ylim = plt.gca().get_ylim()
    plt.ylim([0, ylim[1]])
    plt.savefig('../figures/area_updated_week.png')

    plt.show()



if __name__ == "__main__":
    # count()
    # viz()
    test_notebooks_created_month()
