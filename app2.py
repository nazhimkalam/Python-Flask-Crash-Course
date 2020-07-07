from flask import Flask, render_template                

app = Flask(__name__)                   

#   ------------------------------------------------
#   Templates 
#   ------------------------------------------------

# we create a folder called "templates" and it has to be called "templates" itself

allposts = [
    {
        "title":"Post 01",
        "content":"Content for my post 01 ..... is some random text some random text some random text ",
        "author":"Nazhim"
    },
    {
        "title":"Post 02",
        "content":"Content for my post 02 ..... is some random text some random text some random text "
    }
    
]

@app.route('/')
def homePage():
    return render_template('index.html')   # like this it will search for the index.html file inside the templates folder by default
    
@app.route('/posts')
def postsPage():
    return render_template('posts.html', myPosts = allposts)


# main program to run
if __name__ == "__main__":              
    app.run(debug=True)
