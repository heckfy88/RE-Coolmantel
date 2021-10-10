from dataclasses import dataclass
from builtins import int


@dataclass
class RefrigerantSubstancePropertiesClass:
    """
    Класс свойств охладителя
    """
    refrigerantTemperatureList: list[int]  # список температур охладителя по свойствам из таблицы
    refrigerantCapacityList: list[int]     # список темплоемкостей охладителя по свойствам из таблицы


kerosene = RefrigerantSubstancePropertiesClass
kerosene.refrigerantCapacityList = [10, 20]
kerosene.refrigerantTemperatureList = [20031031, 4032402402]