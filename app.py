from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Creating Flask app to start working
newApp = Flask("newApp")

# this is where the database is stored
newApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogposts.db'

# creating database and linking with the Flask app we created
db = SQLAlchemy(newApp)

# Creating a class for the blogPost, because to work with the database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), default="Unknown")
    
    def __repr__(self):
        return "Blog post " + str(self.id)


allposts = [
    {
        "title": "Post 01",
        "content": "Content for my post 01 ..... is some random text some random text some random text ",
        "author": "Nazhim",
    },
    {
        "title": "Post 02",
        "content": "Content for my post 02 ..... is some random text some random text some random text ",
    }
]


@newApp.route('/')
def homePage():
    return render_template('index.html')


@newApp.route('/posts')
def postsPage():
    return render_template('posts.html', myPosts=allposts)


# main program to run
if __name__ == "__main__":
    newApp.run(debug=True)
