from converters.converter import Converter
from units.units import UnitsManager


def input_dialog(unitsManager: UnitsManager):
    inpt_str = "\n"
    for x in unitsManager.get_list_of_metrics():
        inpt_str += f"{x}\n"
    metric = input(f"Выберите тип метрики ({inpt_str}): ").lower()

    print("ВЫБОР СИСТЕМЫ ИЗМЕРИНИЙ ИЗ КОТОРОЙ ПЕРЕВОДИМ")
    inpt_str = "\n"
    for x in unitsManager.get_list_of_units(metric):
        inpt_str += f"{x}\n"
    units = input(f"Выберите систему измерений ({inpt_str}): ").lower()
    inpt_str = "\n"
    for x in unitsManager.get_list_of_unit(metric, units):
        inpt_str += f"{x}\n"
    unit = input(f"Выберите величину из которой будете переводить ({inpt_str}): ").lower()
    from_unit = (metric, units, unit)

    print("ВЫБОР СИСТЕМЫ ИЗМЕРИНИЙ В КОТОРУЮ ПЕРЕВОДИМ")
    inpt_str = "\n"
    for x in unitsManager.get_list_of_units(metric):
        inpt_str += f"{x}\n"
    units = input(f"Выберите систему измерений ({inpt_str}): ").lower()
    inpt_str = "\n"
    for x in unitsManager.get_list_of_unit(metric, units):
        inpt_str += f"{x}\n"
    unit = input(f"Выберите величину из которой будете переводить ({inpt_str}): ").lower()
    to_unit = (metric, units, unit)

    print("ВВОД ЗНАЧЕНИЯ")
    value = int(input(f"Введите значение: "))

    return from_unit, to_unit, value


if __name__ == '__main__':
    unitsManager = UnitsManager()
    from_unit, to_unit, value = input_dialog(unitsManager)
    converter = Converter(unitsManager.get_ratio(from_unit), unitsManager.get_ratio(to_unit))
    print(converter.convert_units(value))
