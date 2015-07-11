#!/usr/bin/env python

# Usage:
#
# Your board has lists that contain the words mentioned in
# names_colours below in their titles. This script will count all
# cards in those lists and create a stacked area graph accordingly.
#
# Add this to your munin-node configuration:
#
# [trello_burndown]
# env.category My Team Name
# env.trello_url https://api.trello.com/1/board/...
# env.trello_key ...
# env.trello_token ...
# env.http_proxy ...

import os
import sys
import urllib2
import json

names_colours = [
    ('cool', 3),
    ('todo', 2),
    ('doing', 1),
    ('done', 0),
]

def config(out):
    print >> out, "graph_title Trello Burndown Chart"
    print >> out, "graph_vlabel cards"
    print >> out, "graph_category", _get_category()
    print >> out, "graph_args --lower-limit 0"

    areaOrStack='AREA'
    for name, colour in names_colours:
        print >> out, "%s.label %s" % (name, name.capitalize())
        print >> out, "%s.draw %s" % (name, areaOrStack)
        print >> out, "%s.colour COLOUR%d" % (name, colour)
        areaOrStack = 'STACK'
        continue

    return

def _get_category():
    if 'category' in os.environ:
        return os.environ['category']
    return 'Trello'

def get_board_url():
    try:
        proxy = urllib2.ProxyHandler({'https': os.environ['http_proxy']})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
    except KeyError:
        pass
    return urllib2.urlopen(
        '%(url)s?cards=open&lists=open&key=%(key)s&token=%(token)s'
        % get_dict_extract('trello_', os.environ))

def get_dict_extract(prefix, given_dict):
    return dict((key.split(prefix)[1], value)
                for key, value in given_dict.iteritems()
                if key.startswith(prefix))

def get_list_id_dict(board):
    return dict( (l['id'], counter_name)
                 for l in board['lists']
                 for counter_name in dict(names_colours).keys()
                 if counter_name in l['name'].lower() and not l['closed'] )

def get_counts(ids, board):
    counts = dict(zip(dict(names_colours).keys(),
                      [0] * len(names_colours)))
    for c in board['cards']:
        if c['idList'] in ids and not c['closed']:
            counts[ids[c['idList']]] += 1
            pass
        continue

    return counts

def print_counts(counts, out):
    for name, colour in names_colours:
        print >> out, "%s.value %d" % (name, counts[name])
        continue

    return

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'config':
        config(sys.stdout)
    else:
        board = json.load(get_board_url())
        ids = get_list_id_dict(board)
        counts = get_counts(ids, board)
        print_counts(counts, sys.stdout)
        pass
    pass
