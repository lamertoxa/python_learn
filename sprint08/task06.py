import unittest
from unittest.mock import patch


def file_parser(path, find, replace_str=None):
    if replace_str:
        with open(path, "r+") as doc:
            replaced = doc.read()
        with open(path, "w") as doc:

            doc.write(replaced.replace(find, replace_str))
            return f"Replaced {replaced.count(find)} strings"
    else:
        with open(path) as doc:
            return f"Found {doc.read().count(find)} strings"


class ParserTest(unittest.TestCase):

    def test_replace(self):
        with open("replace1.txt", "w") as doc:
            doc.write(("s" * 5) + "Aa" + ("oL" * 9))
        # mock_get_replace.return_value = "No strings"
        expect = "Replaced 9 strings"
        result = file_parser("replace1.txt", "L", "@")
        self.assertEqual(expect, result)

    def test_read(self):
        with open("replace1.txt", "w") as doc:
            doc.write(("s" * 5) + "Aa" + ("oL" * 9))
        # mock_get_replace.return_value = "No strings"
        expect = "Found 9 strings"
        result = file_parser("replace1.txt", "L")
        self.assertEqual(expect, result)


