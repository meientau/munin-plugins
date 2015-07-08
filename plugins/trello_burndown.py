#!/usr/bin/env python


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

def main():
    if len(sys.argv) == 2 and sys.argv[1] == 'config':
        config(sys.stdout)
        sys.exit(0)
        pass
    return


# Todo:
# describe necessary structure in trello
# pick api key and board id from env
# values
# add cooldown
