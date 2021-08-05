***
## Web Scrapper with Python
### Its a python based web srapper which save the data to MongoDB.
__Requirements:__
- Install `python3` in the system.
- Check to see if your Python installation has `pip`. Enter in your terminal:
  ```bash
  $ pip -h
  ```
- If help text of pip is not available then install pip from [here](#https://pip.pypa.io/en/latest/installation/).
- Install the `virtualenv` package for virtual environments.
  ```bash
  $ pip install virtualenv
  ```
- At first make a environment file `venv` in this project
- Assuming you have python 3 in default ``python`` command.
  ```bash
  $ cd scrapper
  $ python -m venv venv
  $ source venv/bin/activate
  ```
- Now install all the requirements in `requirements.txt` file.
  ```bash
  $ pip install -r requirements.txt
  ```
- Copy the ``.env.example`` file as ``.env``. setup required credentials

__Prerequisite:__
- Have to download and specify the chromeWebdriver path in  `DRIVER_PATH` variable in ``.env`` file.
  Without this, project will not start.
  This is actually system's (OS) installed chrome driver path.
    - ChromeDriver can be downloaded from  [here](#https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.19) .
- Here linux version of chromedriver is used. its in ``driver`` folder.
- Create a MongoDB cloud atlas or install mongo in local. In this project it is used mongo db cloud

__Run:__
  ```bash
  $ python index.py 
  ``` 
__Other Information:__
- As the site which will be scrapped is build as a SPA, so selenium is used as a scrapper .

***
