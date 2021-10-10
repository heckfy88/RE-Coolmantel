import math
from dataclasses import *
from input_values import sectionCoordinate_mm, sectionRadius_mm, sectionCurveLength_mm


@dataclass
class RefrigerantPropertiesClass:
    """
    Класс свойств охладителя
    """
    refrigerantTemperatureList: list[int]  # список температур охладителя по свойствам из таблицы
    refrigerantCapacityList: list[int]  # список темплоемкостей охладителя по свойствам из таблицы


@dataclass
class SectionGeometryParamsClass:
    """
    Класс геометрических параметров сечений
    """

    # Задаваемые в конструкторе параметры
    sectionCoordinate_M: list[float]  # координата x, м
    sectionRadius_M: list[float]  # радиус R, м
    sectionCurveLength_M: list[float]  # длина образующей x_s, м

    # Вычисляемые значения
    sectionDiameterList_M: list[float] = field(init=False)  # диаметр D, м
    sectionSpecificDiameterList: list[float] = field(init=False)  # относительный диаметр D_
    sectionAreaList_M2: list[float] = field(init=False)  # площадь S, м^2
    sectionSpecificAreaList: list[float] = field(init=False)  # относительная площадь

    THROAT_DIAMETER: float = field(init=False)  # критический диаметр Dкр, м
    THROAT_AREA: float = field(init=False)  # критическая площадь Fкр, м^2

    sectionCoordinateDeltaList_M: list[float] = field(init=False)  # дельта координаты delta_x, м
    sectionCurveAreaDeltaList_M2: list[float] = field(init=False)  # дельта площади боковой поверхности

    def __post_init__(self):
        self.sectionCoordinate_M = list(map(lambda x: x / 1000, self.sectionCoordinate_M))
        self.sectionRadius_M = list(map(lambda x: x / 1000, self.sectionRadius_M))
        self.sectionCurveLength_M = list(map(lambda x: x / 1000, self.sectionCurveLength_M))

        self.sectionDiameterList_M = list(map(lambda x: 2 * x, self.sectionRadius_M))

        self.THROAT_DIAMETER = min(self.sectionDiameterList_M)
        self.THROAT_AREA = (math.pi * pow(self.THROAT_DIAMETER, 2)) / 4

        self.sectionSpecificDiameterList = list(map(lambda x: x / self.THROAT_DIAMETER, self.sectionDiameterList_M))
        self.sectionAreaList_M2 = list(map(lambda x: math.pi * pow(x, 2), self.sectionRadius_M))
        self.sectionSpecificAreaList = list(map(lambda x: x / self.THROAT_AREA, self.sectionAreaList_M2))

        self.sectionCoordinateDeltaList_M = []
        for i in range(len(self.sectionCoordinate_M) - 1):
            self.sectionCoordinateDeltaList_M.append(abs(self.sectionCoordinate_M[i + 1]
                                                         - self.sectionCoordinate_M[i]))

        self.sectionCurveAreaDeltaList_M2 = []
        for i in range(len(self.sectionCurveLength_M) - 1):
            self.sectionCurveAreaDeltaList_M2.append(0.5 * math.pi
                                                     * (self.sectionDiameterList_M[i] + self.sectionDiameterList_M[
                i + 1])
                                                     * self.sectionCurveLength_M[i])


sections = SectionGeometryParamsClass(sectionCoordinate_mm, sectionRadius_mm, sectionCurveLength_mm)


@dataclass
class CoolingPathParamsClass:
    """
    Класс параметров тракта охлаждения.
    Требует создания объекта sections класса SectionGeometryParamsClass
    """
    # Задаваемые в конструкторе параметры

    pathInnerJacketThickness: float
    pathOuterJacketThickness: float
    pathCoolingRibThickness: float
    pathCoolingRibHeight: float
    pathCoolingRibAngle_grad: float

    # Константы

    MINIMAL_COOLING_RIB_STEP: float = 2.5 / 1000
    MAX_COOLING_RIB_STEP: float = 5.5 / 1000

    # Вычисляемые значения
    pathCoolingRibAngle_rad: float = field(init=False)
    pathAverageThroatDiameter: float = field(init=False)
    pathThroatSectionRibAmount: int = field(init=False)
    pathAverageDiameterList: list[float] = field(init=False)

    pathCoolingRibStepList: list[float] = field(init=False)
    pathCoolingRibAmountList: list[int] = field(init=False)

    pathFlowAreaList: list[float] = field(init=False)
    pathHydraulicDiameterList: list[float] = field(init=False)

    def __post_init__(self):

        self.pathCoolingRibAngle_rad = self.pathCoolingRibAngle_grad * math.pi / 180

        self.pathAverageThroatDiameter: float = sections.THROAT_DIAMETER + 2 * self.pathInnerJacketThickness + self.pathCoolingRibHeight

        self.pathThroatSectionRibAmount: int = int(math.pi * self.pathAverageThroatDiameter * math.cos(
            self.pathCoolingRibAngle_rad) / self.MINIMAL_COOLING_RIB_STEP)
        self.pathThroatSectionRibAmount = (self.pathThroatSectionRibAmount,
                                           self.pathThroatSectionRibAmount - 1)[
            self.pathThroatSectionRibAmount % 2 != 0]

        self.pathAverageDiameterList = list(
            map(lambda x: x + 2 * self.pathInnerJacketThickness + self.pathCoolingRibHeight,
                sections.sectionDiameterList_M))

        self.pathCoolingRibStepList = []
        self.pathCoolingRibAmountList = []
        self.computeCoolingRibAmountNStep(
            self.pathCoolingRibStepList,
            self.pathCoolingRibAmountList,
            self.pathCoolingRibAngle_grad
        )
        self.pathFlowAreaList = []
        self.pathHydraulicDiameterList = []
        self.computeFlowAreaNHydraulicDiameter(self.pathFlowAreaList, self.pathHydraulicDiameterList)

    def computeCoolingRibAmountNStep(self, pathCoolingRibStepList, pathCoolingRibAmountList, pathCoolingRibAngle_grad):
        """
        Метод вычисляет количество ребер на каждом участке и шаг между ними:

        :param pathCoolingRibStepList: list[float]
        :param pathCoolingRibAmountList: list[int]
        :param pathAverageDiameterList: list[float]
        :param pathCoolingRibAngle_grad: float ????????
        """
        sectionRibAmount = self.pathThroatSectionRibAmount
        for section in range(len(self.pathAverageDiameterList) - 1):
            sectionRibStep = math.pi * self.pathAverageDiameterList[section] * math.cos(
                pathCoolingRibAngle_grad) / sectionRibAmount

            if sectionRibStep <= self.MAX_COOLING_RIB_STEP:
                pathCoolingRibStepList.append(sectionRibStep)
                pathCoolingRibAmountList.append(sectionRibAmount)
                sectionRibAmount = self.pathThroatSectionRibAmount
                section += 1
            else:
                sectionRibAmount *= 2

    def computeFlowAreaNHydraulicDiameter(self, pathFlowAreaList, pathHydraulicDiameterList):
        """
        Метод вычисляет площадь проходного сечения по нормали и гидравлический диаметр

        :param pathFlowAreaList: list[float]
        :param pathHydraulicDiameterList: list[float]
        :return:
        """
        for section in range(len(self.pathCoolingRibStepList)):
            pathFlowAreaList.append(self.pathCoolingRibStepList[section]
                                    * self.pathCoolingRibHeight
                                    * self.pathCoolingRibAmountList[section]
                                    * (1 - self.pathCoolingRibThickness / self.pathCoolingRibStepList[section]))
            pathHydraulicDiameterList.append(2 * self.pathCoolingRibHeight
                                             * (self.pathCoolingRibHeight - self.pathCoolingRibThickness)
                                             / (self.pathCoolingRibStepList[
                                                    section] - self.pathCoolingRibThickness + self.pathCoolingRibHeight))


path = CoolingPathParamsClass(0.001, 0.003, 0.001, 0.015, 0)

print(path.pathCoolingRibAmountList)
