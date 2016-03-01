from datetime import datetime, timedelta
from geojson import Point


class User(object):
    def __init__(self,
                 user_id,
                 name,
                 point=None,
                 device=None,
                 timestamp=datetime.now() + timedelta(hours=6)):
        self.user_id = user_id
        self.name = name
        self.point = Point((
            point["coordinates"][0],
            point["coordinates"][1]
        ))
        self.device = Device(
            device["imei"],
            device["phone_number"]
        )
        self.timestamp = timestamp


class Device(object):
    def __init__(self, imei, phone_number):
        self.imei = imei
        self.phone_number = phone_number
