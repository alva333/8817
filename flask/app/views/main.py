"""
IMPORTANT : 
Leave the root route to the Elastic Beanstalk load balancer health check, 
it performs a GET to '/' every 5 seconds and expects a '200' response
If you change the root route, 
you need to change the health check in the Elastic Beanstalk console
"""

from flask import Blueprint, request, jsonify
from app import db
from app.models.models import User
from datetime import datetime

main_bp = Blueprint('main_bp', __name__)

# IMPORTANT : leave the root route to the Elastic Beanstalk Load Balancer health c
@main_bp.route('/', methods=['GET']) 
def EB_healthcheck():
    return 'OK', 200

@main_bp.route('/register', methods=['POST']) 
def register_user():
    try:
        
        data = request.get_json()
        print('\n\nData\n\n',data,'\n\n')
        new_user = User(
            username =  data["username"],
            password_hash = "1234",
            created_at = datetime.utcnow(),
            active = datetime.utcnow()
        ) 
        db.session.add(new_user) 
        db.session.commit() 
        return 'User added', 200
    
    except Exception as e:
        db.session.rollback()
        return f'An error occurred: {str(e)}', 500
    
@main_bp.route('/listusers', methods=['GET'])
def list_users():
    try:
        users = db.session.query(User).all()
        return jsonify([str(u) for u in users])
    except Exception as e:
        db.session.rollback()
        return f'An error has occured: {str(e)}', 500
    
    