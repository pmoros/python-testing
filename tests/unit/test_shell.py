import unittest
from unittest.mock import patch

from app import shell


@patch("app.shell.os.path")
@patch("app.shell.os")
class TestShell(unittest.TestCase):
    def test_should_rm_remove_file_with_valid_path(self, mock_os, mock_path):
        """
        We have an insider, an object we can use to verify
        the functionality of another.
        """
        mock_path.isfile.return_value = True
        tmp_file_path = "tmp_test.txt"

        shell.rm(tmp_file_path)

        mock_os.remove.assert_called_with(tmp_file_path)

    def test_should_not_rm_remove_file_with_invalid_path(self, mock_os, mock_path):
        """
        We have an insider, an object we can use to verify
        the functionality of another.
        """
        mock_path.isfile.return_value = False
        tmp_invalid_file_path = "tmp_invalid_test.txt"

        shell.rm(tmp_invalid_file_path)

        mock_os.remove.assert_not_called()
