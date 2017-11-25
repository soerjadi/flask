# Python Flask example
this just sample project for learning web with flask

How to
------
*please make sure you have python 2 or you have virtualenv on your environment

* first step install the dependencies
```bash
$ pip install -r requirements.txt
```

* copy `example-config.py` to `config.py`
* edit `config.py`
* change `DEBUG` to `False` and `MODE` to `production` if this application in production
* run `tup` *make sure you have `Tupfile` installed on your environment
* run the application
```bash
$ python server.py
```