""" use 'python manage.py run' command to run up application in development environment"""

import os
from flask.ext.script import Manager
from photophile import app
from photophile.database import session, User, Category, Base

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    manager.run()
    
    
    
   
