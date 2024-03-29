import unittest
from unittest.mock import patch, mock_open
# import pytest

from source.data_repo import DataRepository


class TestUser(unittest.TestCase):
    
    
    # def setUp(self) -> None:
    #     return super().setUp()
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.data_repo = DataRepository("user_file_path","another/file/path")

    def test_create_user(self):
        # self.data_repo = DataRepository("user_file_path","another/file/path")
        user_added = self.data_repo.add_user("Test","TestPassword", b"KEY")
        self.assertEqual(user_added,"Test TestPassword KEY")
        
    def test_write_file(self):
        fake_file_path = "users.txt"
        fake_user_name = "Test1"
        fake_password ="testpassword1"
        fake_key = b"fake_key1"
        expected_output = " ".join([fake_user_name, fake_password, fake_key.decode()])
        with patch('source.data_repo.open', mock_open()) as mocked_file:
            actual_output = self.data_repo.add_user(fake_user_name,fake_password, fake_key)
            mocked_file.assert_called_once_with(fake_file_path,'a')
        # self.assertEqual(actual_output,expected_output)
        
        
    # def test_read_user(self):
    #     read_user = self.data_repo.get_users()
    #     expected_output = "someuser"
    #     self.assertEqual(read_user , expected_output)
        
        
    # def test_create_two_new_user(self):
    #     data_repo = DataRepository("user_file_path","another/file/path")
    #     user_added = data_repo.add_user("Test","TestPassword", b"KEY")
    #     user_added = data_repo.add_user("Test","TestPassword", b"KEY")
    #     self.assertEqual(user_added,"Test TestPassword KEY")
        