# Project-3

[![Python application](https://github.com/qiuyixuan/Project-3/actions/workflows/python-app.yml/badge.svg)](https://github.com/qiuyixuan/Project-3/actions/workflows/python-app.yml)

Test Coverage: 94%  

Heroku App Link: https://glacial-plains-37331.herokuapp.com  

The app worked well locally, but the page on the Heroku app might need to be refreshed several times after a button is clicked.


### Extensions:
#### 1. Add Black to correct style errors in our code automatically.
We used the [Black](https://github.com/psf/black) formatter to reformat [app.py](src/app.py) and [test_app.py](tests/test_app.py).

#### 2. Add a calendar to our app, where each to-do item has a due date.
Users can select a due date in a drop-down calender.  
The app will compare the due date with today's and tomorrow's dates and generate a code `Today`, `Tomorrow`, or `Later` for each to-do item.

#### 3. Use a database along with Flask
We used Flask-SQLAlchemy to implement an [app](src/app_db.py) and here is the asscoiated [html file](src/templates/index.html).

#### 4. Add a tag filtering feature
Users can filter to-do items they added to each to-do item using the drop down tag filter, which for now allows single entry tag searches and a reset function that reverts the form back to the full list of to-do-list.
