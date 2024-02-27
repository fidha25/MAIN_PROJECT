from flask import *
from public import public
from admin import admin 
from manager import manager
from staff import staff
app=Flask(__name__)

app.secret_key='34644'

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(manager)
app.register_blueprint(staff)

app.run(debug=True,port=5678)

