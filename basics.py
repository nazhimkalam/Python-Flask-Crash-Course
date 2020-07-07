from flask import Flask                  # imports Flask

myApp = Flask(__name__)                    #__name__ is the __main__ or current module

#   ------------------------------------------------
#   Dynamic URLs 
#   ------------------------------------------------


@myApp.route('/')                          # url without parameters, just https://localhost:portNumber
def welcomeMsg():
    return "Hello World"

@myApp.route('/home/<string:name>')        # getting the url data as parameters
def hello(name):                
    return "Hello " + name

@myApp.route('/home/<int:id>')           
def newFunction(id):                
    return "Hello " + str(id)

@myApp.route('/home/users/<string:name>/posts/<int:id>')           
def newFunction2(name, id):                
    return "Hey" + name + " ,your post number is " + str(id)

#   ------------------------------------------------
#   http methods handling 
#   ------------------------------------------------


@myApp.route('/getData', methods=["GET"])
def getMethod():
    return "Getting data from server...'GET'"

@myApp.route('/sendData', methods=["POST"])   # this url will throw an error because you are trying to get from URL but it has the method = POST not to GET
def postMethod():
    return "Sending data to the server..."

@myApp.route('/both', methods=["GET","POST"])
def both():
    return "Getting data from server... because methods is set to 'POST' and 'GET' "



# main program to run
if __name__ == "__main__":              # runs in the debug mode to spot errors easily and auto complie 
    myApp.run(debug=True)
