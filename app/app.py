from flask import Flask, Blueprint
from frontend.routes import app_blueprint

app = Flask(__name__)


app.config.update(dict(
	SECRET_KEY="mysecretkey one",
	WTF_CSRF_SECRET_KEY="a secret key two"

	))

app.register_blueprint(app_blueprint)

app.run(host="127.0.0.1", port=5000, debug=True)