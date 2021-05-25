from flask import Flask, render_template, request, jsonify
import dbHandler
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") # This page will be renderd for homeUrl

@app.route('/createChatRoom', methods= ['GET','POST'])
def createChatRoom():
    chatRoomDb = 'C' + str(int(time.time())) # Creating new Name of the chatroom ID according to UNIX timestamp.

    dbHandler.createChatRoomDB(chatRoomDb) # Creating new table in database for new chatroom.
    dbHandler.createChatRoomID(chatRoomDb) # Enlisting new 'database ID' to 'ChatRoomID' table.

    return(chatRoomDb) # returning name of the new chatroom, client side script will be executed according to this.

@app.route('/<chatRoomName>') # variable 'url' for any chatroom
def chatRoom(chatRoomName):
    return render_template("index.html", chatRoomName = chatRoomName) # This is common chatroom page, this will be renderd for any chatroom.


@app.route('/addChatToDB', methods= ['GET','POST'])
def addChatToDB():
    chatRoomID = request.form['chatRoomID'] #This data will come via ajax request, check 'main.js' file
    username = request.form['username'] # same as previous 
    comment = request.form['comment'] # same as previous 
    # chatCount = request.form['chatCount'] #This data will come via ajax request, this chat count will be incremented acoording to client side.

    dbHandler.addChatToDB(chatRoomID,username,comment) # comment and username will be inserted to db according to chatRoomID.
    
    return ('', 204) # For returning null value to client



@app.route('/fetchChatData', methods= ['GET','POST'])
def fetchChatData():
    chatCount = request.form['chatCount']
    chatRoomID = request.form['chatRoomID']

    chats = dbHandler.retrieveChatRoom(chatRoomID,chatCount)

    return jsonify(chats)


if __name__ == "__main__":
    app.run(debug=True)