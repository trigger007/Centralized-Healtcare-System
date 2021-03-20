var globe;
var j;
function test7(){   


x='';
 $.ajax({ url: "/gstaffadddetail",
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
 var a=[];
 window.j=a;
 document.getElementById("heading").innerHTML='<div>'+t[0].groundname+'</div>';
 for(i=0;i<t.length;i++)
 {
  a.push(t[i].slot);
 
  }
  console.log(a);    
  var s='';
  for(i=0;i<t.length;i++)
  {
    s=s+a[i]+' ';
  }
  console.log(s);

  document.getElementById("inserthere").innerHTML='<div>The available slots are: '+s+'</div><br><div>Enter the slot that is to be made open</div><input type="text" id="inputofuser"><br><input type="button" value="submit" onclick="check()">';

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
var n;


function check(){
  console.log(window.j);
  var p=document.getElementById("inputofuser").value;
  console.log(p);
  console.log(window.j.includes(p));
  if(!(window.j.includes(p)))
  {
    window.n=p;
    console.log(window.n);
    test8();
  }
  else
    document.getElementById("inserthere2").innerHTML='<div>'+'Slot already exists'+'</div>';
}

function test8(){
console.log(window.n);
var h=window.n;
console.log(h);
var sdata={"slot": h};
console.log("chalgaya");  
console.log(sdata);
$.ajax({ url: "/gstaffadddetail2",
      data: sdata,
      success: function(result){
        console.log('chala');
        console.log(result);
        console.log(result);
        
          window.location.href='http://localhost:3000/gstaffadd';
        
  }});

}