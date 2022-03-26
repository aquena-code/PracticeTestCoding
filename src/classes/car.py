#
# @car.py Copyright (c) 2022 Jalasoft.
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


class Car(Land):
    """Class that represent Car"""

    def __init__(self, name, price, has_motor, use_gas):
        """Constructor of Car"""
        super().__init__(name, price, has_motor)
        self._use_gas = use_gas

    def display_data(self):
        """Return the next values of Car: name, price, Has Motor and Use Gas"""
        return super().display_data() + ", Use Gas = " + str(self._use_gas)
