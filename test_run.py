import unittest
from unittest.mock import patch, MagicMock
import run

class TestRun(unittest.TestCase):

    def test_generate_api_key(self):
        key = run.generate_api_key(32)
        self.assertEqual(len(key), 43)  # 32 bytes == 43 characters in base64

    @patch('run.os.getenv')
    def test_main(self, mock_getenv):
        mock_getenv.return_value = '32'
        with patch('builtins.print') as mock_print:
            run.main()
            mock_print.assert_called_once()