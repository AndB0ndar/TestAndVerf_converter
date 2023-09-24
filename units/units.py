class UnitsManager:
    _metrics = {
        'length': {
            'american': {
                'дюйм': 0.0254,
                'фут': 0.3048,
                'ярд': 0.9144,
                'миля': 1609.3,
            },
            'old_russian': {
                'вершок': 0.0254,
                'пядь': 0.3048,
                'локоть': 0.9144,
                'аршин': 1609.3,
                'сажень': 1609.3,
                'верста': 1609.3,
                'поприще': 1609.3,
            },
            'ci': {
                'мм': 0.001,
                'см': 0.01,
                'метр': 1,
                'км': 1000,
            }
        },
        'weight': {
            'american': {
                'тонна': 1016,
                'центнер': 50.8,
                'фунт': 0.4536,
                'унция': 0.02835,
            },
            'old_russian': {
                'лот': 0.012797,
                'фунт': 0.410,
                'восьмушка': 0.050,
                'пуд': 16.38,
                'батман': 4.1,
                'берковец': 163.8,
            },
            'ci': {
                'миллиграмм': 0.001,
                'грамм': 1,
                'килограмм': 1000,
            }
        },
        'volume_of_liquids': {
            'american': {
                'гиль': 0.1180,
                'пинта': 0.4732,
                'кварта': 0.9464,
                'галон': 3.7854,
                'баррель': 119.24,
            },
            'old_russian': {
                'чарка': 0.12,
                'штоф': 1.23,
                'сороковка': 0.307,
                'ведро': 12.3,
                'осьмуха': 1.55,
                'бочка': 492,
            },
            'ci': {
                'мл': 0.001,
                'л': 1,
            }
        },
    }

    def get_list_of_metrics(self):
        return list(self._metrics.keys())

    def get_list_of_units(self, metrics):
        return list(self._metrics[metrics].keys())

    def get_list_of_unit(self, metrics, units):
        return list(self._metrics[metrics][units].keys())

    def get_ratio(self, unit: tuple):
        return self._metrics[unit[0]][unit[1]][unit[2]]
