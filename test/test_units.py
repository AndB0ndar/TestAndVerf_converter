from unittest import TestCase

from units.units import UnitsManager


class TestUnits(TestCase):
    unitsManager = UnitsManager()

    def test_get_list_units(self):
        target = ['length', 'weight', 'volume_of_liquids']
        self.assertEqual(self.unitsManager.get_list_of_metrics(), target)

    def test_get_list_metric(self):
        target = ['american', 'old_russian', 'ci']
        self.assertEqual(self.unitsManager.get_list_of_units('length'), target)

    def test_get_list_of_unit(self):
        target = ['дюйм', 'фут', 'ярд', 'миля']
        self.assertEqual(self.unitsManager.get_list_of_unit('length', 'american'), target)

    def test_get_ratio(self):
        target = 0.0254
        self.assertEqual(self.unitsManager.get_ratio(('length', 'american', 'дюйм')), target)
