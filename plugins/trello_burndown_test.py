import unittest
import cStringIO

import trello_burndown

class TrelloBurndownTest(unittest.TestCase):
    def setUp(self):
        self.out = cStringIO.StringIO()
        return

    def test_config_has_title(self):
        trello_burndown.config(out)
        self.assertIn("graph_title", self.out.getvalue())
        pass

    def test_config_has_labels(self):
        trello_burndown.config(out)
        for area in "todo", "doing", "done":
            self.assertIn(area + ".label", self.out.getvalue())
            continue
        pass

    pass

if __name__ == '__main__':
    unittest.main()
