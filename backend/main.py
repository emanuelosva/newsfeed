"""Main flas server"""

# Required imports
from app import create_app
from flask_cors import CORS

# Initialize app and enable cors
app = create_app()
CORS(app)

# Initialize server
if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0')
