# flask/application.py , 
    
"""
the script to start the app:
"""
    
from flask import Flask
from app import create_app, db
# the models need to be created before calling the db.create_all()
from app.models.models import User

application = create_app()

with application.app_context() :
        db.create_all()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
