import unittest
from llama import chat_loop, send_message, loading_bar 

class TestChatLoop(unittest.TestCase):
    def test_chat_loop(self):
       
        with unittest.mock.patch('builtins.input', return_value='hello'):
            with unittest.mock.patch('builtins.print'):
                chat_loop()

    def test_send_message(self):
       
        ai = 'llama3-8b-8192'
        message = 'Hello, world!'
        output = send_message(message, ai)
        self.assertIsInstance(output, str)

    def test_loading_bar(self):
       
       
        with unittest.mock.patch('builtins.print') as mock_print:
            loading_bar()
            mock_print.assert_called_with("\rLoading...")
            for i in range(5):
                mock_print.assert_any_call("\rLoading." + "." * (i + 1))

if __name__ == '__main__':
    unittest.main()