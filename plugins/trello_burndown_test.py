import unittest
import cStringIO

import trello_burndown

class TrelloBurndownTest(unittest.TestCase):
    def setUp(self):
        self.out = cStringIO.StringIO()
        return

    def test_config_has_title(self):
        trello_burndown.config(self.out)
        self.assertIn("graph_title", self.out.getvalue())
        pass

    def test_config_has_labels(self):
        trello_burndown.config(self.out)
        for area in "todo", "doing", "done":
            self.assertIn(area + ".label", self.out.getvalue())
            continue
        pass

    def test_dict_extract(self):
        sample = { 'prefix_fruit': 'apple',
                   'prefix_planet': 'jupiter',
                   'unrelated_stuff': 'foobar' }
        expected =  { 'fruit': 'apple', 'planet': 'jupiter' }
        actual = trello_burndown.get_dict_extract('prefix_', sample)
        self.assertEqual(expected, actual)
        pass

    @unittest.skip("Set up the env before activating this test.")
    def test_response_is_not_empty(self):
        """This test requires some elaborate environment: export
        trello_burndown_test_url=https://api.trello.com/1/board/...
        trello_burndown_test_key=...
        trello_burndown_test_token=...
        Use this to find out whether the raw access to trello works."""
        board = trello_burndown.get_board_url()
        self.assertTrue(board.read().startswith('{'))
        pass

    pass

if __name__ == '__main__':
    unittest.main()
