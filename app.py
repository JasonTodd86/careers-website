from flask import Flask
#flask is the module. Modules always are lower-case
#from the flask module, I want to import the Flask class
#this line makes the Flask class available in my script

app = Flask(__name__)
#an app is just an object of the class "Flask" - an instance of the blueprint
#every Flask app has a name
#__name__ is a special variable in Python that's assigned to the string "__main__" when you run the script directly

@app.route("/")
# This is a decorator. It tells Flask what URL should trigger our function
# In this case, the root URL "/" will trigger the hello_world function. When that URL is requested,
# this is telling Flask what function should be returned
def hello_world():
    #this is a function definition
    return "<p>Sup, world?!<p>"
    # This function returns an HTML paragraph when it's called
    # The text "Sup, world?!" will be displayed in the browser

if __name__ == "__main__":
    #this if statement only runs if the script is executed directly
    # It will NOT run if this file is imported as a module in another script
    app.run(host="0.0.0.0", port=5001, debug=True)
    # This line starts the Flask development server
    # host="0.0.0.0" makes the server publicly available
    # port=5001 sets the port number to 5001. Had to explicitly change it from 5000 because
    # port 5000 is often in use on Macs due to the AirPlay Receiver service
    # debug=True enables debug mode, which is helpful during development