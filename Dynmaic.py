from flask import Flask, request, render_template, redirect

dynamic = Flask(__name__)

posts = []

@dynamic.route('/', methods=['GET'])
def index():
    return render_template('index.html', posts=posts)

@dynamic.route('/posts', methods=['POST'])
def create_post():
    username = request.form.get('username')
    content = request.form.get('post')
    if username and content:
        posts.insert(0, {
            'username': username,
            'content': content
        })
    return redirect('/')

@dynamic.route('/discover', methods=['GET'])
def discover():
    return render_template('discover.html')

@dynamic.route('/user', methods=['GET'])
def user():
    return render_template('user.html')

@dynamic.route('/friends', methods=['GET'])
def friends():
    return render_template('friends.html')

if __name__ == '__main__':
    dynamic.run(debug=True, port=9000)
