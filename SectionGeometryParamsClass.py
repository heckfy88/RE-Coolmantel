import math
from dataclasses import *


@dataclass
class SectionGeometryParamsClass:
    """
    Класс геометрических параметров сечений
    """

    # Задаваемые в конструкторе параметры
    sectionCoordinate_M: list[float]                          # координата x, м
    sectionRadius_M: list[float]                              # радиус R, м
    sectionCurveLength_M: list[float]                         # длина образующей x_s, м

    # Вычисляемые значения
    sectionDiameterList_M: list[float] = field(init=False)         # диаметр D, м
    sectionSpecificDiameterList: list[float] = field(init=False)    # относительный диаметр D_
    sectionAreaList_M2: list[float] = field(init=False)            # площадь S, м^2
    sectionSpecificAreaList: list[float] = field(init=False)        # относительная площадь

    THROAT_DIAMETER: float = field(init=False)                 # критический диаметр Dкр, м
    THROAT_AREA: float = field(init=False)                     # критическая площадь Fкр, м^2

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
        for i in range(len(self.sectionCurveLength_M)-1):
            self.sectionCurveAreaDeltaList_M2.append(0.5 * math.pi
                                                     * (self.sectionDiameterList_M[i] + self.sectionDiameterList_M[i + 1])
                                                     * self.sectionCurveLength_M[i])
