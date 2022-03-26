#
# @list_land_transport.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class ListLandTransport:
    """Class that represent ListLandTransport"""

    # list of Lands object
    _land_list = []

    def add_land(self, land):
        """Add an object to the list"""
        self._land_list.append(land)

    def display(self):
        """Display all values of each object into the list"""
        for land in self._land_list:
            print(land.display_data())
