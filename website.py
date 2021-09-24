import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import date
import time
import threading
import random
import subprocess
import requests
import website
from replit import db
#delete key from db curl -XDELETE $REPLIT_DB_URL/Test
#db faq https://docs.replit.com/hosting/database-faq

#curl $REPLIT_DB_URL/   GET DB VALUE


readhtml = ''

def readhtmlfunc():
  readh = open("templates/adminbackup.html", "r")
  website.readhtml = readh.read(-1)
    


def prepend_line(file_name, line):
          """ Insert given string as a new line at the beginning of a file """
          # define name of temporary dummy file
          dummy_file = file_name + '.bak'
          # open original file in read mode and dummy file in write mode
          with open("templates/announcementscode.html", 'r') as read_obj, open(dummy_file, 'w') as write_obj:
              # Write given line to the dummy file
              write_obj.write(line + '\n')
              # Read lines from original file one by one and append them to the dummy file
              for line in read_obj:
                  write_obj.write(line)
          # remove original file
          os.remove(file_name)
          # Rename dummy file as the original file
          os.rename(dummy_file, file_name)


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

about=''
dashuser = ''
session = False
sessionlogin = False
mainadmin = 'hidden'
adminuser = ''
import website
'''
def ses():
  global session
ses()
'''

'''
def authorize():
  if website.session == False:
    return redirect(url_for('login'))
    print('unauthorized')
    print(website.session)
  else:
    print('authorized')
    website.session = False
    print(website.session)
'''

@app.route("/")
def home():
  return render_template('home.html')

@app.route("/invite")
def invite():
  return render_template('invite.html')

@app.route("/info")
def info():
  return render_template('info.html')

@app.route("/announcements")
def announcements():
  return render_template('announcements.html')
  

@app.route("/helpbotgud")
def secret():
  return render_template('secret.html')

@app.route("/codeeditor")
def code():
  return render_template('codeeditor.html')

@app.route('/suggest')
def form():
  success = ''
  disabled = ''
  User = ''
  Suggestion = ''
  hidden = ''
  return render_template('form.html', success=success, disabled=disabled, User=User, Suggestion=Suggestion, hidden=hidden)

@app.route("/admin")
def admin():
  login = 'https://www.help-bot.tk/login'
  return render_template('admin.html', session=website.session, login=login, html=website.readhtml, admin=website.mainadmin, adminu=website.adminuser)

@app.route("/test")
def test():
  return render_template('testpage.html')

@app.route("/denied")
def denied():
  return render_template('403.html')

@app.route("/login")
def loginpage():
  return render_template('login.html')

@app.route("/dashboard")
def dash():
  return render_template('dashboard.html', sessionlogin=website.sessionlogin, dashuser=website.dashuser, about=website.about)

@app.route("/dashlogin")
def dlogin():
  return render_template('dlogin.html')

@app.route("/signup")
def signup():
  return render_template('signup.html', success='', disabled='', user='', password='')

@app.route("/community")
def community():
  dashusers = db['dashuserdata']
  split = dashusers.split('┻')
  uc = 0
  code = ''
  about = ''
  user = ''
  for u in split:
    tempcode = ''
    if uc % 2 == 0 or uc == 0:
      user = '<div class="row"><div class="side"><h2>'+u+'</h2>'
    else:
      about = '<b>about: </b><p>'+u+'</p></div></div><hr>'
      tempcode = user+about
      code = code+tempcode
      about = ''
      user = ''
    uc = uc + 1

  return render_template('community.html', users=code)


'''
@app.route("/proxy")
def proxy():
  bashCommand = "nodejs app.js"
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output, error = process.communicate()
'''

@app.route("/admin", methods=['GET', 'POST'])
def adminform():
  if request.method == 'POST':
    admin = request.form.getlist('admin[]')
    if str(admin[0]) == 'Glitchedcheses#2190':
      website.mainadmin = ''
      time.sleep(1)
      website.mainadmin = 'hidden'
    else:
      print('not main admin')
    if 'announce' in request.form:
      admin = request.form.getlist('admin[]')
      title = request.form.getlist('title[]')
      content = request.form.getlist('content[]')
      today = today = date.today()
      Today = today.strftime("%m/%d/%y")
      prepend_line("templates/announcementscode.html", "<div class='row'>\n<div class='side'>\n<h2>"+Today+' -'+str(admin[0])+", "+str(title[0])+"</h2>\n<p>"+str(content[0])+"</p>\n</div>\n</div>\n<hr>\n")
      success = 'successfully sent announcement! <a href="/announcements"><b>click here to go to view your announcement.</b></a>'
      return render_template('admin.html', success=success, adminu=str(admin[0]), admin=website.mainadmin)
          
    elif "adduser" in request.form:
      admin = request.form.getlist('admin[]')
      adminuser = request.form.getlist('addadmin[]')
      adminpass = request.form.getlist('addpass[]')
      userpass = ','+str(adminuser[0])+','+str(adminpass[0])
      userstore = db["users"]
      db["users"] = userstore+userpass
      success = 'successfully added user to data base!'
      return render_template('admin.html', success=success, adminu=str(admin[0]), admin=website.mainadmin)
      #use this to get values                    curl $REPLIT_DB_URL/users
      #then remove the user with                 curl $REPLIT_DB_URL -d 'users='


    else:
      if request.method == 'POST':
        defs = str(random.randint(0, 10000))
        question = request.form.getlist('question[]')
        answer = request.form.getlist('answer[]')
        admin = request.form.getlist('admin[]')
        f = open("templates/infocode.html", "a")
        f.write('<script>function ShowHide'+defs+'(){var shContent'+defs+' = document.getElementById("show_hide_content'+defs+'");var linkName'+defs+' = document.getElementById("show_hide_tlink'+defs+'");if(linkName'+defs+'.innerText == "Show"){linkName'+defs+'.innerText = "Hide"; shContent'+defs+'.style.display = "block";}else{linkName'+defs+'.innerText = "Show";shContent'+defs+'.style.display = "none";}}</script>\n<style>#show_hide_content'+defs+'{margin-top: 10px; width: 500px; height: 200px; border: solid 1px #000000; padding: 5px; background-color: #FFFFFF; overflow: auto;}</style>\n<p>'+str(question[0])+'</p>\n<a href="" id="show_hide_tlink'+defs+'" onclick="ShowHide'+defs+'();return false;">Show</a>\n<div id="show_hide_content'+defs+'" style="display: none;">\n'+str(answer[0])+'\n</div>\n<hr>\n')
        success = 'successfully added faq question! <a href="/info"><b>click here to go to view your faq question.</b></a>'
        return render_template('admin.html', success=success, adminu=str(admin[0]), admin=website.mainadmin)





      '''
      f = open("templates/announcementscode.html", "a")
      f.write("<!--announcement-->\n<div class='row'>\n<div class='side'>\n<h2>"+Today+", "+str(title[0])+"</h2>\n<p>"+str(content[0])+"</p>\n</div>\n</div>\n<hr>\n")
      return redirect(url_for('announcements'))
      '''




user1 = my_secret = os.environ['user1']
pass1 = my_secret = os.environ['pass1']
user2 = my_secret = os.environ['user2']
pass2 = my_secret = os.environ['pass2']
user3 = my_secret = os.environ['user3']
pass3 = my_secret = os.environ['pass3']
user4 = my_secret = os.environ['user4']
pass4 = my_secret = os.environ['pass4']

def sessionsec():
  time.sleep(1)
  website.session = False
  website.readhtml = ''
  website.mainadmin = 'hidden'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
      try:
        users = db["users"]
        split = users.split(",")
        findpass = split.index(request.form['username'])
        findpass = findpass + 1
        password = split[findpass]

        suspendedacc = ['testacc', '']

        for i in suspendedacc:
          if request.form['username'] == i:
            warning = 'You account is suspended, and going under review.'
            return render_template('login.html', warning=warning)

        if request.form['username'] in split and request.form['password'] == password:
          if request.form['username'] == 'Glitchedcheses#2190':
            website.session = True
            threading.Thread(target=sessionsec).start()
            website.mainadmin = ''
            website.adminuser = request.form['username']
            print(request.form['username']+' Logged in')
            return redirect(url_for('admin'))
          else:
            website.session = True
            threading.Thread(target=sessionsec).start()
            website.adminuser = request.form['username']
            return redirect(url_for('admin'))
        else:
          error = 'Invalid Credentials. Please try again.'
          return render_template('login.html', error=error)
      except:
        error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)


def usersec():
  time.sleep(1)
  website.sessionlogin = False
  website.dashuser = ''
  website.about = ''

@app.route('/dashlogin', methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
      try:
        userdata = db["dashuserdata"]
        splitt = userdata.split("┻")
        user = request.form.getlist('username[]')
        passs = request.form.getlist('password[]')
        user = str(user[0])
        passs = str(passs[0])
        users = db["dashusers"]
        split = users.split(",")
        findpass = split.index(user)
        findpass = findpass + 1
        password = split[findpass]
        
        suspendedacc = ['']

        for i in suspendedacc:
          if user == i:
            warning = 'You account is suspended, and going under review.'
            return render_template('dlogin.html', warning=warning)
        if user in split and passs == password:
          if user not in splitt:
            website.about = ''
          else:
            findabout = splitt.index(user)
            findabout = findabout + 1
            website.about = splitt[findabout] 
          website.sessionlogin = True
          threading.Thread(target=usersec).start()
          website.dashuser = user    
          print(user+' Logged in')      
          return redirect(url_for('dash'))
        else:
          error = 'Invalid Credentials. Please try again.'
          return render_template('dlogin.html', error=error)
      except:
        error = 'Invalid Credentials. Please try again.'
        return render_template('dlogin.html', error=error)

@app.route("/signup", methods=['GET', 'POST'])
def signupacc():
  if request.method == 'POST':
    user = request.form.getlist('username[]')
    passs = request.form.getlist('password[]')
    checkuser = db["dashusers"].split(',')
    if str(user[0]) not in checkuser:
      userpass = ','+str(user[0])+','+str(passs[0])
      userstore = db["dashusers"]
      db["dashusers"] = userstore+userpass
      success = 'successfully signed up! <a href="/dashlogin"><b>Click here to login</b></a>'
      username = str(user[0])
      password = str(passs[0])
      return render_template('signup.html', success=success, disabled='disabled', user=username, password=password)
    else:
      username = str(user[0])
      password = str(passs[0])
      error = 'Please choose another username, the username "'+username+'" is already in use'
      return render_template('signup.html', error=error, disabled='', user=username, password=password)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashdata():
  if request.method == 'POST':
    success = 'successfully updated user about!'
    userdata = db["dashuserdata"]
    about = request.form.getlist('about[]')
    user = request.form.getlist('user[]')
    user = str(user[0])
    about = str(about[0])
    abbout = about
    split = userdata.split("┻")
    if user not in split:
      split.append(user)
      split.append(about)
      splitt = '┻'.join(split)
      db["dashuserdata"] = splitt
      return render_template('dashboard.html', success=success, dashuser=user, about=abbout)
    else:
      findabout = split.index(user)
      findabout = findabout + 1
      aboutcurrent = split[findabout]
      split[findabout] = about
      db["dashuserdata"] = '┻'.join(split)
      return render_template('dashboard.html', success=success, dashuser=user, about=abbout)
      

'''
suspend account


warning = 'You account is suspended, and going under review.'
return render_template('login.html', warning=warning)


'''




@app.route('/suggest', methods = ['POST', 'GET'])
def result():
  success = ''
  disabled = ''
  User = ''
  Suggestion = ''
  hidden = ''
  if request.method == 'POST':
    user = request.form.getlist('user[]')
    suggestion = request.form.getlist('suggestion[]')
    
    f = open("templates/suggestions.txt", "a")
    f.write("\n<br>Suggestion by: "+str(user[0])+', <br>\nSuggestion: '+str(suggestion[0])+"\n<br>\n")
    f.close()
    
    success = ' your suggestion is stored in a database!'
    disabled = 'disabled'
    User = str(user[0])
    Suggestion = str(suggestion[0])
    hidden = 'hidden'
    return render_template('form.html', success=success, disabled=disabled, User=User, Suggestion=Suggestion, hidden=hidden)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.run(host="0.0.0.0")

