# Pyramid Learning Journal

A simple Pyramid app for a learning journal blog.

**Authors**:

- Zach Taylor
- the class of Code Fellows Python 401d5

## Routes:

- `/home` - the home page and a listing of all articles
- `/create` - to create a new blog post
- `/update` - the page for updating a blog post
- `/detail` - page displaying details of blog post

## Set Up and Installation:

- Clone this repository to your local machine.

- Once downloaded, `cd` into the `pyramid_learning_journal` directory.

- Begin a new virtual environment with Python 3 and activate it.

- `cd` into the next `pyramid_learning_journal` directory. It should be at the same level of `setup.py`

- `pip install` this package as well as the `testing` set of extras into your virtual environment.

- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

## To Test

- If you have the `testing` extras installed, testing is simple. If you're in the same directory as `setup.py` type the following:

```
$ tox
```