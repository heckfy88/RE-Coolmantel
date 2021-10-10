import math
from dataclasses import *
from SectionGeometryParamsClass import SectionGeometryParamsClass
from input_values import sectionCoordinate_mm, sectionRadius_mm, sectionCurveLength_mm


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
