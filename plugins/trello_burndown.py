#!/usr/bin/env python

# Usage:
#
# Your board has lists that contain the words mentioned in
# count_lists_names_colours below in their titles. This script
# will count all cards in those lists and create a stacked
# area graph accordingly.

import urllib2
import os
import sys

count_lists_names_colours = [
    ('todo', 2),
    ('doing', 1),
    ('done', 0),
]

def config(out):
    print >> out, "graph_title Trello Burndown Chart"
    print >> out, "graph_vlabel cards"
    print >> out, "graph_category brainlab"
    print >> out, "graph_args --lower-limit 0"

    areaOrStack='AREA'
    for name, colour in count_lists_names_colours:
        print >> out, "%s.label %s" % (name, name.capitalize())
        print >> out, "%s.draw %s" % (name, areaOrStack)
        print >> out, "%s.colour COLOUR%d" % (name, colour)
        areaOrStack = 'STACK'
        continue
    return

def get_board_url():
    return urllib2.urlopen(
        '%(url)s?cards=open&lists=open&key=%(key)s&token=%(token)s'
        % get_dict_extract(_get_env_prefix(),
                           os.environ))

def _get_env_prefix():
    # e.g. if the script is called as 'foobar.py', we will later
    # for 'foobar_url' in the environment.
    return os.path.basename(sys.argv[0]).split('.')[0] + '_'

def get_dict_extract(prefix, given_dict):
    return dict((key.split(prefix)[1], value)
                for key, value in given_dict.iteritems()
                if key.startswith(prefix))

def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'config':
        config(sys.stdout)
        sys.exit(0)
        pass
    return


# Todo:
# values
# add cooldown
