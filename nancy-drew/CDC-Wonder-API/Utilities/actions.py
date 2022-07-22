import unittest

class Action(unittest.TestCase):

    def trigger_an_error(self, error_type, test_action):

        with self.assertRaises(error_type) as exception:
            test_action

        triggered_error = exception.exception

        return triggered_error