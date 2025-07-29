from app import app
from app.models import User, db
# LOADS THE FLASK APP, AND ALL THE DEPENDENCIES, WITHOUT RUNNING THE SERVER
# DEBUG MODE IS ALSO USEFUL: Set the system variable FLASK_DEBUG=1

# implementing "leaderboard" from previous project, so may not need this

@app.shell_context_processor
def make_shell_context():
    ''' For testing in terminal. '''
    return {'db':db, 'User':User}