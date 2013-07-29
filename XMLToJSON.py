#!/usr/bin/env python
import argparse
from parseNoteXML import parseNoteXML
parser = argparse.ArgumentParser(description='parse Evernote XML to Json Format')
parser.add_argument(
    'xml_name', help='XML file name')

parser.add_argument(
    'json_name', help='json file name')
args = parser.parse_args()
# notes = parseNoteXML('/home/wangjing/Documents/Evernote-2013-07-24.enex')
notes = parseNoteXML(args.xml_name)
import json
with open(args.json_name, 'wb') as fp:
    json.dump(notes, fp)
