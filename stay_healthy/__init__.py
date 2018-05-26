# app/__init__.py

# from flask import Flask

# Initialize the app
# app = Flask(__name__, instance_relative_config=True)

# Load the views
# from app import views

# Load the config file
# app.config.from_object('config')

from flask import Flask, render_template
import os

app = Flask(__name__)
app.debug=True
app.secret_key = 'my secret key.'
import stay_healthy.views

if __name__ == "__main__":
    app.run()
