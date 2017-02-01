# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from collections import namedtuple
import unittest
import tempfile

from azure.cli.core._util import get_file_json, todict, to_snake_case, truncate_text


class TestUtils(unittest.TestCase):

    def test_application_todict_none(self):
        the_input = None
        actual = todict(the_input)
        expected = None
        self.assertEqual(actual, expected)

    def test_application_todict_dict_empty(self):
        the_input = {}
        actual = todict(the_input)
        expected = {}
        self.assertEqual(actual, expected)

    def test_application_todict_dict(self):
        the_input = {'a': 'b'}
        actual = todict(the_input)
        expected = {'a': 'b'}
        self.assertEqual(actual, expected)

    def test_application_todict_list(self):
        the_input = [{'a': 'b'}]
        actual = todict(the_input)
        expected = [{'a': 'b'}]
        self.assertEqual(actual, expected)

    def test_application_todict_obj(self):
        MyObject = namedtuple('MyObject', 'a b')
        the_input = MyObject('x', 'y')
        actual = todict(the_input)
        expected = {'a': 'x', 'b': 'y'}
        self.assertEqual(actual, expected)

    def test_application_todict_dict_with_obj(self):
        MyObject = namedtuple('MyObject', 'a b')
        mo = MyObject('x', 'y')
        the_input = {'a': mo}
        actual = todict(the_input)
        expected = {'a': {'a': 'x', 'b': 'y'}}
        self.assertEqual(actual, expected)

    def test_load_json_from_file(self):
        _, pathname = tempfile.mkstemp()

        # test good case
        with open(pathname, 'w') as good_file:
            good_file.write('{"key1":"value1", "key2":"value2"}')
        result = get_file_json(pathname)
        self.assertEqual('value2', result['key2'])

        # test error case
        with open(pathname, 'w') as bad_file:
            try:
                bad_file.write('{"key1":"value1" "key2":"value2"}')
                get_file_json(pathname)
                self.fail('expect throw on reading from badly formatted file')
            except Exception as ex:  # pylint: disable=broad-except
                self.assertTrue(str(ex).find(
                    'contains error: Expecting value: line 1 column 1 (char 0)'))

    def test_to_snake_case_from_camel(self):
        the_input = 'thisIsCamelCase'
        expected = 'this_is_camel_case'
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)

    def test_to_snake_case_empty(self):
        the_input = ''
        expected = ''
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)

    def test_to_snake_case_already_snake(self):
        the_input = 'this_is_snake_cased'
        expected = 'this_is_snake_cased'
        actual = to_snake_case(the_input)
        self.assertEqual(expected, actual)

    def test_truncate_text(self):
        expected = 'stri [...]'
        actual = truncate_text('string to shorten', width=10)
        self.assertEqual(expected, actual)

    def test_truncate_text_not_needed(self):
        expected = 'string to shorten'
        actual = truncate_text('string to shorten', width=100)
        self.assertEqual(expected, actual)

    def test_truncate_text_zero_width(self):
        with self.assertRaises(ValueError):
            truncate_text('string to shorten', width=0)

    def test_truncate_text_negative_width(self):
        with self.assertRaises(ValueError):
            truncate_text('string to shorten', width=-1)


if __name__ == '__main__':
    unittest.main()
