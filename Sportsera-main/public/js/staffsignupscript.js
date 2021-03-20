function test2(){            
var firstname = document.getElementById("firstname").value;
console.log("Groundname is" + firstname);
var lastname = document.getElementById("lastname").value;
console.log("Sportname is" + lastname);
var username = document.getElementById("username").value;
console.log("username is" + username);
var gid = document.getElementById("gid").value;
console.log("gid is" + gid);
var slot = document.getElementById("slot").value;
console.log("slot is" + slot);
var price = document.getElementById("price").value;
console.log("price is" + price);

var staffname=document.getElementById("staffname").value;
console.log("staffname is" + staffname);
var password=document.getElementById("password1").value;
console.log("staffid is" + password);
var mobileno = document.getElementById("mobileno").value;
console.log("username is" + mobileno);
var address1 = document.getElementById("address1").value;
console.log("username is" + address1);            
var address2 = document.getElementById("address2").value;
console.log("username is" + address2);
var address3 = document.getElementById("address3").value;
console.log("username is" + address3);
var zipcode = document.getElementById("zipcode").value;
var rating=3.5;
var price=350;
console.log("username is" + zipcode);

var x={
"groundname": firstname,
"gid":gid,
"sportname":lastname,
"username":username,
"staffid":password1,
"mobileno":mobileno,
"address1":address1,
"address2":address2,
"address3":address3,
"zipcode":zipcode,
"password":password,
"rating":rating,
"price":price
};

 $.ajax({ url: "/staffsignupdetail",
 		  data: x,
 		  success: function(result){
    	  console.log('chala');
  }});

console.log(x);


};

