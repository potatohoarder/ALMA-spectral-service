import os
import flask

def create_app(test_config=None): # Application Factory. Creates an instance of the Flask class and sets things up
	app = flask.Flask(__name__) # __name__ is the name of the current Python module
		
	@app.route("/splatalogue")
	def splatalogue():
		
		
	return(app)