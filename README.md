# Near-By-Services-And-Artist-Finder

# 👨‍💻 Tech stack

Here's a brief high-level overview of the tech stack the Well app uses:

- This project uses the [django](https://www.djangoproject.com/). django is a python back-end framework which supports MVC architecture.
- For persistent storage (database), the app uses the [SQLite](https://sqlite.org/index.html) package which allows the app to create a custom storage schema and save it to a local database.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/)  installed on your computer. From your command line:

````bash
# Clone the repository
$ git clone https://github.com/niyati03/near-by-services-and-artist-finder

# Go into the repository
$ cd near-by-services-and-artist-finder

# Create a Virtual Environment
$ python -m venv env # for windows 
or 
$ python3 -m venv env # for mac/linux

# Install dependencies
$ pip install -r requirements.txt
or
$ pip3 install -r requirements.txt

# create your database
$ python manage.py makemigrations 
or 
$ python3 manage.py migrate