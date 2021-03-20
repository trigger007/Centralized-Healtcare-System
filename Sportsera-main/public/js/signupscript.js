function test2(){
console.log("start test2()");	
var firstname = document.getElementById("firstname").value;
console.log("username is" + firstname);
var lastname = document.getElementById("lastname").value;
console.log("username is" + lastname);
var username = document.getElementById("username").value;
console.log("username is" + username);
var password=document.getElementById("password1").value;
console.log("password is" + password);
var mobileno = document.getElementById("mobileno").value;
console.log("username is" + mobileno);
var address1 = document.getElementById("address1").value;
console.log("username is" + address1);            
var address2 = document.getElementById("address2").value;
console.log("username is" + address2);
var address3 = document.getElementById("address3").value;
console.log("username is" + address3);
var zipcode = document.getElementById("zipcode").value;
console.log("username is" + zipcode);

var x={"firstname": firstname,
"lastname":lastname,
"username":username,
"password":password1,
"mobileno":mobileno,
"address1":address1,
"address2":address2,
"address3":address3,
"zipcode":zipcode,
"password":password
};
console.log('b4 ajax',x);
 $.ajax({ url: "/signupdetail",
 		  data: x,
 		  success: function(result){
    	  console.log('chala');
  }});

console.log('hello:',x);


};

