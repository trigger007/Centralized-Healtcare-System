$(document).ready(function(){

    var chatCount = 0

    $('#createChatRoom').click(function(e){

        $.ajax({
            type : 'GET',
            url: '/createChatRoom' // sending ajax POST request to the url createChatRoom, check '__init__.py' file
        }).done(function(chatRoomDb){ // this request will be executed after server responds with valid data
            $('#chatRoomLink').html(`
                <h2>Your Chat Room...</h2>
                <code style="padding:10px; font-size:1.2em">http://127.0.0.1:5000/${chatRoomDb}</code>   
                <a style="margin-left:10px;" class="btn btn-info" id="visitChatRoom" href="http://127.0.0.1:5000/${chatRoomDb}" target="_blank">Visit</a>
            `);
        });

        e.preventDefault();
    });

    // create a ajax function which will send the 'username' , 'comment', 'chatCount' to the server

    $('#submitComment').click(function(e){

        var chatRoomID = $('#chatRoomID').text();
        var username = $('#userName').val();
        var comment = $('#addComment').val();


        if(username == "" || comment == ""){
            alert('Please fill Up all Fields');
            return false
        }
        $('#addComment').val('');

        $.ajax({
            
            data: {
                "chatRoomID" : chatRoomID,
                "username" : username,
                "comment" : comment
            },
            url: '/addChatToDB',
            type: 'POST'
        });

        e.preventDefault();
    });
    

    // This function is used for fetching chat from server

    function fetchChat(){

        var chatRoomID = $('#chatRoomID').text();

        $.ajax({
            data:{
                "chatCount" : chatCount,
                "chatRoomID" : chatRoomID
            },
            type: 'POST',
            url: '/fetchChatData'
        }).done(function(chats){
            $.each(chats, function( index, value ) {
              $('#chat').append( value[0] + " : " + value[1] + "\n");
              chatCount += 1
            });
            $('#chatCount').html(chatCount)
        })
    }

    setInterval(fetchChat, 1000);

});