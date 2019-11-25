import pytest
import functools
import datetime

import pymysql
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.services.CustomerService import CustomerService
from app.services.DBService import db_reset


class TestCustomerService(object):


  def test_ExploreMovie(self):
    #MoviePlay.movName,
     # MoviePlay.'comName':,
     #  Theater.thStreet,
     # Theater.thCity,
     #  Theater.thState,
     #   Theater.thZipcode,
     #thName
     #  MoviePlay.movPlayDate\

    expected = [
      {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,10,12),'thName':"ABC Theater",'comName':"Awesome Theater Company",'thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
      {'movName':"The First Pokemon Movie",'movPlayDate':datetime.date(2018,7,19),'thName':"ABC Theater",'comName':"Awesome Theater Company",'thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
      {'movName':'Georgia Tech The Movie','movPlayDate':datetime.date(1985,8,13),'thName':'ABC Theater','comName':'Awesome Theater Company','thStreet':'880 Color Dr','thCity':'Austin','thState':'TX','thZipcode':'73301'},
      {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,4,2),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,9,12),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':"The King's Speech",'movPlayDate':datetime.date(2019,12,20),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':'Spaceballs','movPlayDate':datetime.date(2000,2,2),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':'Georgia Tech The Movie','movPlayDate':datetime.date(2019,9,30),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2010,5,20),'thName':'Cinema Star','comName':'4400 Theater Company','thStreet':'100 Cool Place','thCity':'San Francisco','thState':'CA','thZipcode':'94016'},
      {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,22),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,23),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':'Spaceballs','movPlayDate':datetime.date(1999,6,24),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2019,10,22),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':"George P Burdell's Life Story",'movPlayDate':datetime.date(2019,7,14),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':"The King's Speech",'movPlayDate':datetime.date(2019,12,20),'thName':'Main Movies','comName':'EZ Theater Company',"thStreet":"123 Main St",'thCity':"New York",'thState':'NY','thZipcode':'10001'},
      {'movName':'Spaceballs','movPlayDate':datetime.date(2010,4,2),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
      {'movName':'Spaceballs','movPlayDate':datetime.date(2023,1,23),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
      {'movName':'Calculus Returns: A ML Story','movPlayDate':datetime.date(2019,10,10),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
      {'movName':'Calculus Returns: A ML Story','movPlayDate':datetime.date(2019,12,30),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
      {'movName':'Spider-Man: Into the Spider-Verse','movPlayDate':datetime.date(2019,9,30),'thName':'ML Movies','comName':'AI Theater Company','thStreet':'314 Pi St','thCity':'Pallet Town','thState':'KS','thZipcode':'31415'},
      {'movName':'How to Train Your Dragon','movPlayDate':datetime.date(2010,3,25),'thName':'Star Movies','comName':'EZ Theater Company','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA','thZipcode':'30332'},
      {'movName':"4400 The Movie",'movPlayDate':datetime.date(2019,8,12),'thName':'Star Movies','comName':'EZ Theater Company','thStreet':'745 GT St','thCity':'Atlanta','thState':'GA','thZipcode':'30332'}
    ]

    customer_service = CustomerService()
        # i_movName = filters.get("i_movName")
        # i_comName = filters.get("i_comName")
        # i_city = filters.get("i_city")
        # i_state = filters.get("i_state")
        # i_minMovPlayDate = filters.get("i_minMovPlayDate")
        # i_maxMovPlayDate = filters.get("i_maxMovPlayDate")

    # filters = {
    #   'i_movName':
    #   'i_comName':
    #   'i_city':
    #   'i_state':
    #   'i_minMovPlayDate':
    #   'i_maxMovPlayDate':
    # }
    filters = {
      'i_city':"",
      'i_state':""
    }

    actual = customer_service.ExploreMovie(filters)

    assert len(expected) == len(actual)
    assert sorted(actual, key=functools.cmp_to_key(compare_movie)) == sorted(expected, key=functools.cmp_to_key(compare_movie))


def compare_movie(item1, item2):
    if item1['movName'] < item2['movName']:
        return -1
    elif item1['movName'] > item2['movName']:
        return 1
    else:
        return compare_theater_name(item1, item2)

def compare_theater_name(item1, item2):
    if item1['thName'] < item2['thName']:
        return -1
    elif item1['thName'] > item2['thName']:
        return 1
    else:
        return compare_play_date(item1, item2)

def compare_play_date(item1, item2):
    
    if item1['movPlayDate'] < item2['movPlayDate']:
        return -1
    elif item1['movPlayDate'] > item2['movPlayDate']:
        return 1
    else:
        return 0


