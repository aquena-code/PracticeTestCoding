#
# @main.py Copyright (c) 2022 Jalasoft.
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
from src.classes.bicycle import Bicycle
from src.classes.car import Car
from src.classes.list_land_transport import ListLandTransport


if __name__ == "__main__":

    # Declare Land objects
    land1: Land = Bicycle("BMX", 1200, False, True)
    land2: Land = Car("Ferrari", 850000, True, False)
    land3: Land = Bicycle("Scott", 300, False, True)
    land4: Land = Car("Honda", 23000, True, False)

    # Declare a ListLandTransport
    list_land_transport = ListLandTransport()

    # Add objects to the list
    list_land_transport.add_land(land1)
    list_land_transport.add_land(land2)
    list_land_transport.add_land(land3)
    list_land_transport.add_land(land4)

    # Display all objects of the list
    list_land_transport.display()
