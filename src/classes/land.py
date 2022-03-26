#
# @land.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from src.classes.transport import Transport


class Land(Transport):
    """Class that represent Land"""

    def __init__(self, name, price, has_motor):
        """Constructor of Land"""
        super().__init__(name, price)
        self._has_motor = has_motor

    def display_data(self):
        """Return the name, price and Has Motor of Land"""
        return "name = " + super().get_name() + ", price = " + str(super().get_price())\
               + ", Has Motor = " + str(self._has_motor)
