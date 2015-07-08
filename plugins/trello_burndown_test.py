import unittest

import trello_burndown

class TrelloBurndownTest(unittest.TestCase):
    def test_config(self):
        config = trello_burndown.config()
        self.assertIn("graph_title", config)
        pass

    pass

if __name__ == '__main__':
    unittest.main()
