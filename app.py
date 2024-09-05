from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)



# Import routes here to avoid circular imports
from routes import *

#if __name__ == '__main__':
#   app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
