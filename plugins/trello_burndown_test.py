import unittest
import cStringIO

import trello_burndown

class TrelloBurndownTest(unittest.TestCase):
    def test_config_has_title(self):
        out = cStringIO.StringIO()
        trello_burndown.config(out)
        self.assertIn("graph_title", out.getvalue())
        pass

    def test_config_has_labels(self):
        out = cStringIO.StringIO()
        trello_burndown.config(out)
        for area in "todo", "doing", "done":
            self.assertIn(area + ".label", out.getvalue())
            continue

        pass

    pass

if __name__ == '__main__':
    unittest.main()
