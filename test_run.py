import unittest
from unittest.mock import patch
import run
import base64

class TestRun(unittest.TestCase):

    def test_generate_api_key(self):
        key = run.generate_api_key(32)
        decoded_key = base64.urlsafe_b64decode(key + '==')
        self.assertEqual(len(decoded_key), 32)  # 32 bytes

    @patch('run.os.getenv')
    def test_main(self, mock_getenv):
        mock_getenv.return_value = '32'
        with patch('builtins.print') as mock_print:
            run.main()
            mock_print.assert_called_once()

    def test_generate_api_key_different_length(self):
        key = run.generate_api_key(64)
        decoded_key = base64.urlsafe_b64decode(key + '==')
        self.assertEqual(len(decoded_key), 64)  # 64 bytes

    @patch('run.os.getenv')
    def test_main_different_length(self, mock_getenv):
        mock_getenv.return_value = '64'
        with patch('builtins.print') as mock_print:
            run.main()
            mock_print.assert_called_once()
            printed_key = mock_print.call_args[0][0].split('=')[1]
            decoded_key = base64.urlsafe_b64decode(printed_key + '==')
            self.assertEqual(len(decoded_key), 64)  # 64 bytes

    @patch('run.os.getenv')
    def test_main_invalid_length(self, mock_getenv):
        mock_getenv.return_value = 'invalid'
        with self.assertRaises(ValueError):
            run.main()