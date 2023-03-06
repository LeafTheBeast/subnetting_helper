import unittest

from main import check_ip


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_check_ip_success(self):
        test_value = check_ip('123')
        self.assertEqual(test_value, True)

    def test_check_ip_fail_when_char(self):
        test_value = check_ip('ddd')
        self.assertEqual(test_value, False)

    def test_check_ip_fail_when_number_to_big(self):
        test_value = check_ip('400')
        self.assertEqual(test_value, False)


if __name__ == '__main__':
    unittest.main()
