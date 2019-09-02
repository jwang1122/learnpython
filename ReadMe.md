# Python Programing

## Start Python command line

```python
c:\> py
```

## VSCode for Python

The VS Code extension for Python: Python for VSCode.

## Write to a file named "guru99.txt"
```python
f = open("guru99.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))

f.close()
```

## Execute Python file

```python
c:\> py add.py
c:\> py game.py
right-click mouse, select "Run Python file in terminal."
```

## import Python module, and use the module

```python
>>> import add
>>> import fib
>>> fib.fib(1000)
```

## Download Visual Code

[Download Visual Code](https://code.visualstudio.com/)
![web page](vscode.jpg)

[Start up Visual Code](https://code.visualstudio.com/docs?start=true)

## Create a virtual environment

```bash
PS C:\Users\V801625\workspace\python> py -m venv venv
```
where -m means create a module, first venv is virtual environment, second is the name of the newly created virtual environment.

PS C:\Users\V801625\workspace\python> & c:/Users/V801625/workspace/python/venv/Scripts/activate.ps1
(venv) PS C:\Users\V801625\workspace\python>

where (venv) means the virtual environment is up and running.

## Install pip requests

```bash
(venv) PS C:\Users\V801625\workspace\python> pip install requests
 python -m pip install --upgrade pip
```

## Debug
1. Select break point in the code
2. click bug on left tool bar
3. select configuration if no yet
4. click green triangle beside "Debug"

## Python.path
Global python installation
```json
    {"python.pythonPath": "C:\\Users\\V801625\\AppData\\Local\\Programs\\Python\\Python37\\python.exe",}
```
Local Environment
```json
    {"python.pythonPath": "c:\\Users\\V801625\\workspace\\python\\venv\\Scripts\\python.exe",}
```

## Set/Get Environment Variables

```sh
C:\Users\V801625\workspace\python>set FLASK_APP=flaskblog.py
C:\Users\V801625\workspace\python>echo %FLASK_APP%

PS C:\Users\V801625\workspace\python> Get-ChildItem Env:
```

## install database sql package

```bash
C:\Users\V801625\workspace\python>pip install flask-sqlalchemy
(venv) C:\Users\V801625\workspace\python\Flask_Blog>py
>>> from flaskblog import db
>>> db.create_all()
>>> from flaskblog  import User,Post
>>> user_1 = User(username='John',email='jw@live.com',password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='Ailian',email='aw@live.com',password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
>>> User.query.first()
>>> User.query.filter_by(username='John').all()
>>> User.query.filter_by(username='John').first()
>>> user = User.query.filter_by(username='John').first()
>>> user.id
>>> user.username
>>> user = User.query.get(2)

>>> post1 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
>>> post2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)
>>> db.session.add(post1)
>>> db.session.add(post2)
>>> db.session.commit()
>>> for post in user.posts:
...     print(post.title)
...
>>> post = Post.query.first()
>>> post
Post('Blog 1', '2019-09-02 12:38:04.828772')
>>> post.id
>>> post.user_id
>>> post.author
User('Ailian', 'aw@live.com', 'default.jpg')
```
## MongoDB
Install package
```bash
(venv) C:\Users\V801625\workspace\python\Flask_Blog>pip install pymongo
```