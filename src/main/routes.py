from . import app

@app.route("/")
def home():
	return "Oolááá"