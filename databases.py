from flask import Flask, render_template, request, redirect
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


@newApp.route('/')
def homePage():
    return render_template('index.html')


@newApp.route('/posts', methods=['GET', 'POST'])
def postsPage():

    if request.method == 'POST':

        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']

        # adding an object to the database
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)  
        db.session.add(new_post)

        # It's mandatory to commit
        db.session.commit()

        return redirect('/posts')
    else:
        allposts = BlogPost.query.all()
        return render_template('posts.html', myPosts=allposts)

