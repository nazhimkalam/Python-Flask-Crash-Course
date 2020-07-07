from flask import Flask                  # imports Flask

app = Flask(__name__)                    #__name__ is the __main__ or current module

#   ------------------------------------------------
#   Dynamic URLs 
#   ------------------------------------------------


@app.route('/')                          # url without parameters, just https://localhost:portNumber
def welcomeMsg():
    return "Hello World"

@app.route('/home/<string:name>')        # getting the url data as parameters
def hello(name):                
    return "Hello " + name

@app.route('/home/<int:id>')           
def newFunction(id):                
    return "Hello " + str(id)

@app.route('/home/users/<string:name>/posts/<int:id>')           
def newFunction2(name, id):                
    return "Hey" + name + " ,your post number is " + str(id)

#   ------------------------------------------------
#   http methods handling 
#   ------------------------------------------------


@app.route('/getData', methods=["GET"])
def getMethod():
    return "Getting data from server...'GET'"

@app.route('/sendData', methods=["POST"])   # this url will throw an error because you are trying to get from URL but it has the method = POST not to GET
def postMethod():
    return "Sending data to the server..."

@app.route('/both', methods=["GET","POST"])
def both():
    return "Getting data from server... because methods is set to 'POST' and 'GET' "



# main program to run
if __name__ == "__main__":              # runs in the debug mode to spot errors easily and auto complie 
    app.run(debug=True)
