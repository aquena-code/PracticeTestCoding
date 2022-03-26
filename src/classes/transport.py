#
# @transport.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class Transport:
    """Class that represent Transport"""

    def __init__(self, name, price):
        """Constructor of Transport"""

        self._name = name
        self.price = price

    def get_name(self):
        """Return the name of Transport"""
        return self._name

    def get_price(self):
        """Return the price of Transport"""
        return self.price
