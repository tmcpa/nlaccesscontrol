import unittest
import yaml
from modules.permission_checker import permission_checker

class TestPermissionChecker(unittest.TestCase):

    # agent1 has permission(s)
    def test_has_permissions(self):
        result = permission_checker('agent1', ['read', 'write'])
        expected = '{"read": true, "write": true}'
        self.assertEqual(result, expected)

    # agent2 missing user
    def test_missing_user(self):
        result = permission_checker('agent2', ['read', 'write'])
        expected = '{"read": false, "write": false}'
        self.assertEqual(result, expected)

    # agent1 missing permission(s)
    def test_missing_permission(self):
        result = permission_checker('agent1', ['read', 'delete'])
        expected = '{"read": true, "delete": false}'
        self.assertEqual(result, expected)

    #check result value from yaml file
    def test_result_from_file(self):
        with open('agents.yaml') as file:
            expected = '{"write": true}'
            result = permission_checker('agent1', ['write'], 'agents.yaml')
            self.assertEqual(result, expected)
    

if __name__ == '__main__':
    unittest.main()