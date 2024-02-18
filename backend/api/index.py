from flask import Flask
from flask_cors import CORS
from api.views import views
from api.test_views import test_views

app = Flask(__name__)
CORS(app)

# Registering production endpoints
app.register_blueprint(views, url_prefix="/api")

# Registering test endpoints
app.register_blueprint(test_views, url_prefix="/api/test")
