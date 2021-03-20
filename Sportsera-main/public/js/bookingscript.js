var globe;
function test3(){   

var Location = document.getElementById("Location").value;
console.log("Location is " + Location);
var Slot=document.getElementById("Slot").value;
console.log("Slot is " + Slot);     
var Sport=document.getElementById("Sport").value;
console.log("Sport is " + Sport);     

var x={
	"Location":Location,
	"Slot":Slot,
  "Sport":Sport
};
var l;

 $.ajax({ url: "/bookingdetail",
      data: x,
      success: function(result){
        console.log('chala');
        console.log(result);
        l=result;
        
        
       console.log(l);
 console.log(result);
 
 var t=JSON.parse(l);
 window.globe=t;
 
 console.log(t);
 document.getElementById("inserthere").innerHTML='<div>'+t.groundname+'<input type="submit" onclick="test4()">'+'</div>';
      
  }});



console.log(x);

       


};

function test4()
{
	var l;
	console.log(window.globe);
	
	$.ajax({ url: "/bookingupdate",
      data: window.globe,
      success: function(result){
        console.log('chala');
        console.log(result);
        console.log(l);

        l=result;
        if(l=='ALREADY EXCEEDS MAX BOOKING')
        {
        	document.getElementById("inserthere").innerHTML='<div>'+l+'</div>';
        }
 
       
  }});


}
