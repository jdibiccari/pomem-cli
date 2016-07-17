from mock import patch, MagicMock
from unittest import TestCase
from multiline_input import multiline_input

raw_input_value = ["Shall I compare thee to a summer's day?",
				   "Thou art more lovely and more temperate:",
				   "Rough winds do shake the darling buds of May,",
				   "And summer's lease hath all too short a date:",
				   "Sometime too hot the eye of heaven shines,",
				   "And often is his gold complexion dimm'd;",
				   "And every fair from fair sometime declines,",
				   "By chance, or nature's changing course, untrimm'd;",
				   "@@"]

expected = "\n".join(raw_input_value[:-1]) + "\n"

class TestMultiLineInput(TestCase):
    def test_yes(self):
    	mock = MagicMock(side_effect=raw_input_value)
        with patch('__builtin__.raw_input', mock) as _raw_input:
            self.assertEqual(multiline_input(), expected)
