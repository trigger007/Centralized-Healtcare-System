function test6(){   

var username = document.getElementById("username").value;
console.log("username is" + username);
var password=document.getElementById("password1").value;
console.log("password is" + password);     

var x={
  "username":username,
  "password":password
};

 $.ajax({ url: "/gstafflogindetail",
      data: x,
      success: function(result){
        console.log('chala');
        console.log(result);
        if (result=='1')
          window.location.href='http://localhost:3000/gstaffmaintainance';
        else 
          document.getElementById("submitbutton").innerHTML="<div>not a valid peroson</div>";
  }});
  
  
console.log(x);
       


};

