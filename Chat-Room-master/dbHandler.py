# This Script is for Handling Database...

import sqlite3 as sql 
DATABASE = 'chatRoom.db'

 # This function will update individual chatRoom table with 'comment' and 'username' according to 'chatRoomID'
def addChatToDB(chatRoomID,username,comment):
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    query = "INSERT INTO {}".format(chatRoomID)
    cur.execute(query + "(userName, userComment) VALUES (?,?)",(username,comment))
    conn.commit()
    conn.close()

# This function is used for retrieving chatData from individual chatroom Table
def retrieveChatRoom(chatRoomID,chatCount): # variable required: 'chatCount', 'chatRoomID'
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    query = "SELECT userName,userComment FROM {} WHERE id > {}".format(chatRoomID,chatCount)
    cur.execute(query)
    chatRooms = cur.fetchall()
    conn.close()
    return chatRooms

# This function is used for enlisting new chatroom name to the 'chatRoomID' table.
def createChatRoomID(chatRoomName):
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO chatRoomID(chatRoomName) VALUES(?)", (chatRoomName,)) 
    # Without the commaa behind the chatroom name sqlite will arise an error, 
    # cause sqlite will treat it as a grouped expression, not a tuple.
    conn.commit()
    conn.close()

# this function will generate new Table in Database with New 'Chat Room Name'. Check '__init__.py' 
def createChatRoomDB(chatRoomName):
    conn = sql.connect(DATABASE)
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS {}(id INTEGER primary key autoincrement,\
        userName TEXT not null, userComment TEXT not null)".format(chatRoomName)
    cur.execute(query)
    conn.commit()
    conn.close()
