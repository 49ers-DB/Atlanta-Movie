import pytest
import functools
import datetime
import pymysql
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services.DBService import get_conn
from app.services.ManagerService import ManagerService


class TestManagerService(object):


    def test_TheaterOverview_NoFilters(self):

        TOTestDict = {}
        manager_service = ManagerService()
        Actual= manager_service.TheaterOverview('imbatman',TOTestDict)
        Expected =[
            {'Movie':"How to Train Your Dragon",'Release_Date':datetime.date(2010, 3,21),'Play_Date':None,'Duration':98},
            {'Movie':"4400 The Movie",'Release_Date':datetime.date(2019,8,12),'Play_Date':None,'Duration':130},
            {'Movie':"The First Pokemon Movie",'Release_Date':datetime.date(1998,7,19),'Play_Date':None,'Duration':75},
            {'Movie':"The King's Speech",'Release_Date':datetime.date(2010,11,26),'Play_Date':None,'Duration':119},
            {'Movie':"Avengers: Endgame",'Release_Date':datetime.date(2019,4,26),'Play_Date':None,'Duration':181},
            {'Movie':'Spaceballs','Release_Date':datetime.date(1987,6,24),'Play_Date':None,'Duration':96},
            {'Movie':"Spider-Man: Into the Spider-Verse",'Release_Date':datetime.date(2018,12,1),'Play_Date':None,'Duration':117},
            {'Movie':"Georgia Tech The Movie",'Release_Date':datetime.date(1985,8,13),'Play_Date':None,'Duration':100},
            {'Movie':"George P Burdell's Life Story",'Release_Date':datetime.date(1927,8,12),'Play_Date':None,'Duration':100},
            {'Movie':"Calculus Returns: A ML Story",'Release_Date':datetime.date(2019,9,19),'Play_Date':None,'Duration':314},
            {'Movie':"4400 The Movie",'Release_Date':datetime.date(2019,8,12),'Play_Date':datetime.date(2019,10,12),'Duration':130},
            {'Movie':"The First Pokemon Movie",'Release_Date':datetime.date(1998,7,19),'Play_Date':datetime.date(2018,7,19),'Duration':75},
            {'Movie':'Georgia Tech The Movie','Release_Date':datetime.date(1985,8,13),'Play_Date':datetime.date(1985,8,13),'Duration':100}]
        print(Actual)
        assert len(Expected) == len(Actual)
        assert sorted(Expected, key=functools.cmp_to_key(compare_movie)) == sorted(Actual, key=functools.cmp_to_key(compare_movie))


    def test_TheaterOverview_MinReleaseDate(self):

        TOTestDict = {'i_minReleaseDate':datetime.date(2010,11,26)}
        manager_service = ManagerService()
        Actual= manager_service.TheaterOverview('imbatman',TOTestDict)
        expected =[
            {'Movie':"4400 The Movie",'Release_Date':datetime.date(2019,8,12),'Play_Date':None,'Duration':130},
            {'Movie':"The King's Speech",'Release_Date':datetime.date(2010,11,26),'Play_Date':None,'Duration':119},
            {'Movie':"Avengers: Endgame",'Release_Date':datetime.date(2019,4,26),'Play_Date':None,'Duration':181},
            {'Movie':"Spider-Man: Into the Spider-Verse",'Release_Date':datetime.date(2018,12,1),'Play_Date':None,'Duration':117},
            {'Movie':"Calculus Returns: A ML Story",'Release_Date':datetime.date(2019,9,19),'Play_Date':None,'Duration':314},
            {'Movie':"4400 The Movie",'Release_Date':datetime.date(2019,8,12),'Play_Date':datetime.date(2019,10,12),'Duration':130}]

        print(Actual)
        assert len(expected) == len(Actual)
        assert sorted(expected, key=functools.cmp_to_key(compare_movie)) == sorted(Actual, key=functools.cmp_to_key(compare_movie))


    def test_TheaterOverview_ReleaseDate(self):

        TOTestDict = {'i_minReleaseDate':datetime.date(1985,8,13),
                    'i_maxReleaseDate':datetime.date(2010,11,26)
        }
        manager_service = ManagerService()
        Actual= manager_service.TheaterOverview('imbatman',TOTestDict)
        Expected =[
            {'Movie':"How to Train Your Dragon",'Release_Date':datetime.date(2010, 3,21),'Play_Date':None,'Duration':98},
            {'Movie':"The First Pokemon Movie",'Release_Date':datetime.date(1998,7,19),'Play_Date':None,'Duration':75},
            {'Movie':"The King's Speech",'Release_Date':datetime.date(2010,11,26),'Play_Date':None,'Duration':119},
            {'Movie':'Spaceballs','Release_Date':datetime.date(1987,6,24),'Play_Date':None,'Duration':96},
            {'Movie':"Georgia Tech The Movie",'Release_Date':datetime.date(1985,8,13),'Play_Date':None,'Duration':100},
            {'Movie':"The First Pokemon Movie",'Release_Date':datetime.date(1998,7,19),'Play_Date':datetime.date(2018,7,19),'Duration':75},
            {'Movie':'Georgia Tech The Movie','Release_Date':datetime.date(1985,8,13),'Play_Date':datetime.date(1985,8,13),'Duration':100}]
        print(Actual)
        assert len(Expected) == len(Actual)
        assert sorted(Expected, key=functools.cmp_to_key(compare_movie)) == sorted(Actual, key=functools.cmp_to_key(compare_movie))


    def test_TheaterOverview_PlayDate(self):

        TOTestDict = {'i_minPlayDate':datetime.date(2019,3, 19),
                    'i_maxPlayDate':datetime.date(2019, 11, 12)
        }
        manager_service = ManagerService()
        Actual= manager_service.TheaterOverview('imbatman',TOTestDict)
        Expected =[
            {'Movie':"4400 The Movie",'Release_Date':datetime.date(2019,8,12),'Play_Date':datetime.date(2019,10,12),'Duration':130}]
        print(Actual)
        assert len(Expected) == len(Actual)
        assert sorted(Expected, key=functools.cmp_to_key(compare_movie)) == sorted(Actual, key=functools.cmp_to_key(compare_movie))

        TOTestDict = {'i_minPlayDate':datetime.date(2019,3, 19),
                    'i_maxPlayDate':datetime.date(2019, 3, 19)
        }
        Actual = manager_service.TheaterOverview('imbatman',TOTestDict)
        Expected =[]
        print(Actual)
        assert len(Expected) == len(Actual)
        assert sorted(Expected, key=functools.cmp_to_key(compare_movie)) == sorted(Actual, key=functools.cmp_to_key(compare_movie))


    def test_Schedule_Movie(self):

        filterz = {'i_movName':'Spaceballs','i_movReleaseDate':datetime.date(1987,6,24),'i_movPlayDate':datetime.date(2030,6,24)}


        connection = get_conn()
        with connection.cursor() as cursor:
            sql_del = """delete From MoviePlay where movPlayDate = '2030-06-24'"""
            cursor.execute(sql_del)
            connection.commit()

            manager_service = ManagerService()

            manager_service.ScheduleMovie('imbatman',filterz)

            cursor.execute("select * from MoviePlay where movPlayDate = '2030-06-24'")
            data=cursor.fetchall()
            connection.commit()

            sql_del = """delete From MoviePlay where movPlayDate = '2030-06-24'"""
            cursor.execute(sql_del)
            connection.commit()

        connection.close()

        assert len(data)==1





def compare_movie(item1, item2):
    if item1['Movie'] < item2['Movie']:
        return -1
    elif item1['Movie'] > item2['Movie']:
        return 1
    else:
        return compare_play_date(item1, item2)

def compare_play_date(item1, item2):
    if item1['Play_Date'] is None and item2['Play_Date'] is None:
        return 0
    elif item1['Play_Date'] is None:
        return 1
    elif item2['Play_Date'] is None:
        return -1

    if item1['Play_Date'] < item2['Play_Date']:
        return -1
    elif item1['Play_Date'] > item2['Play_Date']:
        return 1
    else:
        return 0




