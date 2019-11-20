import pytest
from ..services.ManagerService import ManagerService

import pymysql

class TestManagerService(object):



    def test_TheaterOverview(self):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='trixie3008',
                             db='moviez',
                             charset='utf8mb4',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
        TOTestDict = {}
        manager_service = ManagerService(connection)
        Actual=manager_service.TheaterOverview('imbatman',TOTestDict)
        Expected=[
            {'Movie':"How to Train Your Dragon",'Release_Date':'2010-03-21','Play_Date':None,'Duration':98},
            {'Movie':"4400 The Movie",'Release_Date':'2019-08-12','Play_Date':None,'Duration':130},
            {'Movie':"The First Pokemon Movie",'Release_Date':'1998-07-19','Play_Date':None,'Duration':75},
            {'Movie':"The King's Speech",'Release_Date':'2010-11-26','Play_Date':None,'Duration':119},
            {'Movie':"Avengers: Endgame",'Release_Date':'2019-04-26','Play_Date':None,'Duration':181},
            {'Movie':'Spaceballs','Release_Date':'1987-06-24','Play_Date':None,'Duration':96},
            {'Movie':"Spider-Man: Into the Spider-Verse",'Release_Date':'2018-12-01','Play_Date':None,'Duration':117},
            {'Movie':"Georgia Tech The Movie",'Release_Date':'1985-08-13','Play_Date':None,'Duration':100},
            {'Movie':"George P Burdell's Life Story",'Release_Date':'1927-08-12','Play_Date':None,'Duration':100},
            {'Movie':"Calculus Returns: A ML Story",'Release_Date':'2019-09-19','Play_Date':None,'Duration':314},
            {'Movie':"4400 The Movie",'Release_Date':'2019-08-12','Play_Date':'2019-10-12','Duration':130},
            {'Movie':"The First Pokemon Movie",'Release_Date':'1998-07-19','Play_Date':'2018-07-19','Duration':75},
            {'Movie':'Georgia Tech The Movie','Release_Date':'1985-08-13','Play_Date':'1985-08-13','Duration':100}]
        print(Actual)
        assert len(Expected) == len(Actual)
        assert Expected == Actual


