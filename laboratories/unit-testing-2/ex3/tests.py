import unittest
from unittest.mock import patch
from ex3 import calculate_total 

class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        with patch('ex3.read') as mock_read:
            mock_read.return_value = [10.5, 20.0, 5.5]
            
            result = calculate_total('dummy.txt')
            
            self.assertEqual(result, 36.0)
            
            mock_read.assert_called_once_with('dummy.txt')

if __name__ == '__main__':
    unittest.main()