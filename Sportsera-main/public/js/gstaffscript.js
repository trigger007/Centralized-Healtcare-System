function test5(){   

var username = document.getElementById("username").value;
console.log("username is" + username);


var x={
	"username":username
};

 $.ajax({ url: "/gstaffdetail",
 		  data: x,
 		  success: function(result){
    	  console.log('chala');
    	  console.log(result);
  			
  }});
	
	
console.log(x);
       


};
