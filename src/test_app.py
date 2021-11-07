"""
CS321
Project 3
Yixuan Qiu & Luhang Sun
"""

from app import *
import requests


# website_path = "https://salty-river-43291.herokuapp.com/"
website_path = "http://127.0.0.1:5000/"


def test_about():

    # simple way to test webpage (words for basic pages)
    assert about() == "A to-do app"

    # more intreesting way to test the the page works
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200  # success


def test_add():

    # creating a post request with data as if coming from form
    client = app.test_client()
    url = "/add"
    data = {"item": "to do"}
    response = client.post(url, data=data)

    # making sure we got redirected, and the request didn't fail
    assert response.status_code == 302  # redirect

    # making sure the home page now includes the added test data
    response = client.get("/")
    webpage_text = response.get_data()
    assert b"to do" in response.data

    # url = website_path + '/add'
    # myobj = {'visitor': 'New person'}

    # webpage = requests.post(url, data = myobj)

    # assert "New person" in webpage.text


def test_remove():
    # client = app.test_client()
    # url = "/remove"
    # data = {"item": "to do"}
    # response = client.get(url, data=data)

    # # get redirected
    # assert response.status_code == 404  # redirect because the page does not exist anymore after the removal

    # # making sure the home page does not include the removed test data
    # response = client.get("/")
    # webpage_text = response.get_data()
    # assert b"to do" not in response.data

    client = app.test_client()
    url = "/remove"
    data = {"item": "to do"}
    response = client.delete(url, data=data, follow_redirects=True)

    assert response.status_code == 200

    response = client.get("/")
    webpage_text = response.get_data()
    assert b"to do" not in response.data
