#!/usr/bin/env python
import argparse
import os
import os.path
import json

from parseNoteXML import parseNoteXML
parser = argparse.ArgumentParser(description='parse Evernote XML to Json Format')
parser.add_argument(
    'xml_name', help='XML file name or a path of folder with xml files')

parser.add_argument(
    'json_name', help='json file name or path of output folder')
args = parser.parse_args()
# notes = parseNoteXML('/home/wangjing/Documents/Evernote-2013-07-24.enex')


def parse_and_save(xml_name, json_name):
    notes = parseNoteXML(xml_name)
    with open(json_name, 'wb') as fp:
        json.dump(notes, fp)

if os.path.isfile(args.xml_name):
    parse_and_save(args.xml_name, args.json_name)
else:
    if not os.path.exists(args.json_name):
        os.makedirs(args.json_name)
    for f in os.listdir(args.xml_name):
        print 'write [%s]' % (f)
        f_path = os.path.join(args.xml_name,f)
        if os.path.isfile(f_path) and f.endswith('.enex'):
            parse_and_save(f_path, os.path.join(args.json_name,
                                                f.rsplit('.enex')[0] + '.json'))
