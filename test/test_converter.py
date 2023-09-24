from unittest import TestCase

from converters.converter import Converter


class TestConverter(TestCase):
    def test_convert_units(self):
        converter = Converter(0.5, 5)
        value = 7
        target = 0.7
        self.assertEqual(converter.convert_units(value), target)
