# Project-3

[![Python application](https://github.com/qiuyixuan/Project-3/actions/workflows/python-app.yml/badge.svg)](https://github.com/qiuyixuan/Project-3/actions/workflows/python-app.yml)

Test Coverage: 94%  

### Extensions:
#### 1. Add Black to correct style errors in our code automatically.
We used the [Black](https://github.com/psf/black) formatter to reformat [app.py](src/app.py) and [test_app.py](tests/test_app.py).

#### 2. Add a calendar to our app, where each to-do item has a due date.
Users can select a due date in a drop-down calender.  
The app will compare the due date with today's and tomorrow's dates and generate a code `Today`, `Tomorrow`, or `Later` for each to-do item.

#### 3. Use a database along with Flask
We used Flask-SQLAlchemy to implement an [app](src/app_db.py) and here is the asscoiated [html file](src/templates/index.html).
