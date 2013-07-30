# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:52:28 2013

@author: kranzth
"""
from traits.api \
    import HasTraits, Instance, Str, on_trait_change

from traitsui.api \
    import View, VGroup, Item, ValueEditor, TextEditor

from copy import deepcopy

class DictEditor(HasTraits):
    SearchTerm = Str()
    Object = Instance( object )

    def __init__(self, obj, **traits):
        super(DictEditor, self).__init__(**traits)
        self._original_object = obj
        self.Object = self._filter(obj)

    def trait_view(self, name=None, view_elements=None):
        return View(
          VGroup(
            Item( 'SearchTerm',
                  label      = 'Search:',
                  id         = 'search',
                  editor     = TextEditor(),
                  #style      = 'custom',
                  dock       = 'horizontal',
                  show_label = True
            ),
            Item( 'Object',
                  label      = 'Debug',
                  id         = 'debug',
                  editor     = ValueEditor(),
                  style      = 'custom',
                  dock       = 'horizontal',
                  show_label = False
            ),
          ),
          title     = 'Dictionary Editor',
          width     = 800,
          height    = 600,
          resizable = True,
        )

    @on_trait_change("SearchTerm")
    def search(self):
        self.Object = self._filter(self._original_object, self.SearchTerm)

    def _filter(self, object_, search_term=None):
        def has_matching_leaf(obj):
            if isinstance(obj, list):
                return any(
                        map(has_matching_leaf, obj))
            if isinstance(obj, dict):
                return any(
                        map(has_matching_leaf, obj.values()))
            else:
                try:
                    if not str(obj) == search_term:
                        return False
                    return True
                except ValueError:
                    False

        obj = deepcopy(object_)
        if search_term is None:
            return obj

        if isinstance(obj, dict):
            for k in obj.keys():
                if not has_matching_leaf(obj[k]):
                    del obj[k]

            for k in obj.keys():
                if isinstance(obj, dict):
                    obj[k] = self._filter(obj[k], search_term)
                elif isinstance(obj, list):
                    filter(has_matching_leaf,obj[k])

        return obj

def viz_dict(data):
    b = DictEditor(my_data)
    b.configure_traits()

def build_sample_data():
    def make_one_level_dict():
        return dict(zip(range(100),
                        range(100,150) + map(str,range(150,200))))

    my_data = make_one_level_dict()
    my_data[11] = make_one_level_dict()
    my_data[11][11] = make_one_level_dict()
    return my_data

# Test
if __name__ == '__main__':
    my_data = build_sample_data()
    b = DictEditor(my_data)
 
 
 b.configure_traits()
