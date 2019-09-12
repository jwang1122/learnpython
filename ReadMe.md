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
click triangle on top right
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

## Python tutorial YouTube

[Class](https://www.youtube.com/watch?v=apACNr7DC_s)

[Function](https://www.youtube.com/watch?v=NE97ylAnrz4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=12)

[Map, Filter, Reduce](https://www.youtube.com/watch?v=hUes6y2b--0)

[lambda Expression](https://www.youtube.com/watch?v=25ovCm9jKfA)

[Tuple](https://www.youtube.com/watch?v=NI26dqhs2Rk)

[CSV](https://www.youtube.com/watch?v=Xi52tx6phRU)

[File](https://www.youtube.com/watch?v=4mX0uPQFLDU)

[Exception](https://www.youtube.com/watch?v=nlCKrKGHSSk)

[Random](https://www.youtube.com/watch?v=zWL3z7NMqAs)

[Recursion](https://www.youtube.com/watch?v=Qk0zUZW-U_M)

[JSON](https://www.youtube.com/watch?v=pTT7HMqDnJw)

[Function](https://www.youtube.com/watch?v=NE97ylAnrz4)

[Lambda Expression](https://www.youtube.com/watch?v=25ovCm9jKfA)

[Unit test](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

[Web Django](https://www.youtube.com/watch?v=OTmQOjsl0eg)
[OOP](https://www.youtube.com/watch?v=qiSCMNBIP2g)

[MongoDB](https://www.youtube.com/watch?v=onuOSdOWcqQ)

[SQLLite](https://www.youtube.com/watch?v=pd-0G0MigUA)

[10 Tips, Tricks](https://www.youtube.com/watch?v=C-gEQdGVXbk&t=21s)

[5 mistakes](https://www.youtube.com/watch?v=zdJEYhA2AZQ&t=104s)

[Help](https://www.youtube.com/watch?v=BVXv0-1Rcc8&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=8)

[pyDoc](https://www.youtube.com/watch?v=URBSvqib0xw&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=33)

[Decrator](https://www.youtube.com/watch?v=FsAPt_9Bf3U)

## 5 Common mistakes
1. name your file as standard library;
2. name your variable as standard function name;

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

## Run unittest
```bash
Johns-MacBook-Pro:learnpython wangqianjiang$ python -m unittest test_circle
```