from unittest import TestCase
from units.units import Units


class TestUnits(TestCase):
    def test_get_list_units(self):
        target = ['length', 'weight', 'volume_of_liquids']
        self.assertEqual(Units.get_list_units(), target)

    def test_get_list_metric(self):
        target = ['american', 'old_russian', 'ci']
        self.assertEqual(Units.get_list_metrics(), target)
