from flask import Flask, render_template, request, redirect, url_for
#url_for to construct url, redirect for redirecting the users

app = Flask(__name__)      #Name of the file as it stands in current directory. It allows flask to find the app as unique.                                 #We can use anything instead of __name__.
blog = {
   'name': 'My awesome blog',
   'posts':{
      1:{
         'post_id':1,
         'title': 'First Post',
         'content': 'Hello,World!'
      },
      2:{
         'post_id':2,
         'title': 'Second Post',
         'content': 'Hello, Asia!'
      }
   }
}

@app.route('/')            #Python Decorator. When user arrives at this url on website, than the below function will be called.
def hello_world():
   #return "Hello World!"
   return render_template('home.jinja2',blog=blog)   #Browser does rendering of this.

@app.route('/post/<int:post_id>')
def post(post_id):
   post = blog['posts'][post_id]
   #return post['title']
   if not post:
      return render_template('404.jinja2',message="A post with id={post_id} was not found.")
   return render_template('post.jinja2', post=post)

#By default flask uses GET request.
@app.route('/post/create', methods=['GET','POST'])
def create():
   if request.method == 'POST':
      title = request.form.get('title')              #It is the name of the field and not id.
      content = request.form.get('content')
      post_id = len(blog['posts'])+1
      blog['posts'][post_id] = {'post_id': post_id, 'title': title, 'content': content}   #Inserting a post
      return redirect(url_for('post', post_id=post_id))    #url_for has 1st argument as function where to go, 2nd arg is the arguent that the function needs.
   return render_template('create.html')

if __name__ == '__main__':
   app.run()