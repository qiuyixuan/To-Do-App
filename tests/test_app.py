from app import *
import requests


website_path = "https://salty-river-43291.herokuapp.com/"
#website_path = "http://127.0.0.1:5000/"

def test_about():
	
	# simple way to test webpage (words for basic pages)
	assert about() == "About us: Naser and the cool kids from CS321"

	# more intreesting way to test the the page works
	client = app.test_client()
	response = client.get("/about")
	assert response.status_code == 200  # success


def test_add():

	# creating a post request with data as if coming from form
	client = app.test_client()
	url = '/add'
	data = {'visitor': 'New person'}
	response = client.post(url, data=data)
	
	# making sure we got redirected, and the request didn't fail
	assert response.status_code == 302  # redirect

	# making sure the home page now includes the added test data
	response = client.get("/")
	webpage_text = response.get_data()
	assert b'New person' in response.data



	# url = website_path + '/add'
	# myobj = {'visitor': 'New person'}

	# webpage = requests.post(url, data = myobj)

	# assert "New person" in webpage.text