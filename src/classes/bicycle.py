#
# @bicycle.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from src.classes.land import Land


class Bicycle(Land):
    """Class that represent Bicycle"""

    def __init__(self, name, price, has_motor, exercise_bike):
        """Constructor of Bicycle"""
        super().__init__(name, price, has_motor)
        self._exercise_bike = exercise_bike

    def display_data(self):
        """Return the next values of Bicycle: name, price, Has Motor and Exercise Bike"""
        return super().display_data() + ", Exercise Bike = " + str(self._exercise_bike)
