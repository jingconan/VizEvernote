from __future__ import print_function, division, absolute_import
import sys
from lxml.html import etree
from StringIO import StringIO
#http://www.hanxiaogang.com/writing/parsing-evernote-export-file-enex-using-python/
# p = etree.HTMLParser(remove_blank_text=True, resolve_entities=False)
p = etree.HTMLParser(remove_blank_text=True)

entities = [
    ('&nbsp;', u'\u00a0'),
    ('&acirc;', u'\u00e2'),
]


def to_valid_xml(x):
    for before, after in entities:
        x = x.replace(before, after.encode('utf8'))
    return x


def convert_xml(f_name, out_name):
    with open(f_name, 'r') as fid:
        with open(out_name, 'w') as out:
            for line in fid:
                out.write(to_valid_xml(line))


def parseNoteXML(note_name):
    convert_xml(note_name, note_name + '.xml')
    context = etree.iterparse(note_name + '.xml',
                              encoding='utf-8',
                              strip_cdata=False)
    note_dict = {}
    notes = []
    for ind, (action, elem) in enumerate(context):
        text = elem.text
        if elem.tag == 'content':
            # x = to_valid_xml(elem.text.encode('utf-8'))
            x = elem.text.encode('utf-8')
            r = etree.parse(StringIO(x), p)
            for e in r.iter():
                try:
                    text.append(e.text)
                except:
                    print('cannot print', file=sys.stderr)

        note_dict[elem.tag] = text
        # NixNote use "Note"; Evernote Windows & Mac Client use "note"
        # if elem.tag == "Note" or elem.tag == 'note':
        if elem.tag == "note":
            notes.append(note_dict)
            note_dict = {}
    return notes

if __name__ == "__main__":
    notes = parseNoteXML('../test.nnex')
