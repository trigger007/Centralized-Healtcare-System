var https = require('https');
var fs = require('fs');
var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var app = express();
const spawn = require("child_process").spawn;
var session = require('express-session');
const router = express.Router();
const fss = require('fs');
const sys = require('sys');
//dbst mysql = require('mysql');
var sqlite3 = require('sqlite3').verbose();
const url = require('url');
var g;
var user;
var staff;
var sess;
app.use(session({secret: 'ssshhhhh',saveUninitialized: true,resave: true}));

//Middleware
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname, 'public'))); //for configuring the path
app.set('views', path.join(__dirname, 'views')); //for configuring the path
app.listen(process.env.PORT || 3000,() => {
    console.log(`App Started on PORT ${process.env.PORT || 3000}`);
});
app.use('/',router);
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('view engine', 'ejs');

/*var db_data = {
    host : "remotemysql.com",
    user : "F7R05a0c2c",
    password: "FnOR6qpsy7",
    database: "F7R05a0c2c",
    "port" : "3306"
};*/

var que;

//var db = mysql.createdbnection(db_data);

let db = new sqlite3.Database('./lite.db',(err) => {              // The server is either down
    if(err) {                                     // or restarting (takes a while sometimes).
      console.log('error when dbnecting to db:', err);
    }                      
    console.log("Database dbnected!!");
  }); 
  
db.get("PRAGMA foreign_keys = ON")
db.run('PRAGMA busy_timeout = 6000');

que = 'CREATE TABLE IF NOT EXISTS USER(uid INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, username TEXT, password TEXT, address1 TEXT, address2 TEXT, faceno BLOB, booking1 INTEGER,FOREIGN KEY(booking1) REFERENCES GROUND(gid));';

db.all(que, function(err, result){
	if (err) throw err;
	console.log(result);
});

que = 'CREATE TABLE IF NOT EXISTS GROUND(gid INTEGER PRIMARY KEY, tid INTEGER, groundname TEXT, location TEXT,rating NUMBER,sportsname TEXT,safety TEXT,FOREIGN KEY(tid) REFERENCES TIMESLOTS(tid));';
db.all(que, function(err, result){
	if (err) throw err;
	console.log(result);
});

que = 'CREATE TABLE IF NOT EXISTS TIMESLOTS(tid INTEGER PRIMARY KEY, time REAL);';
db.all(que, function(err, result){
	if (err) throw err;
	console.log(result);
});

que = 'CREATE TABLE IF NOT EXISTS BOOKINGS(bid INTEGER PRIMARY KEY AUTOINCREMENT, gid INTEGER, uid INTEGER, FOREIGN KEY(gid) REFERENCES GROUND(gid), FOREIGN KEY(uid) REFERENCES USER(uid));'; 
db.all(que, function(err, result){
	if (err) throw err;
	console.log(result);
});



router.post('/logindetail', function(req, res){
	var data1 = req.body;
	sess = req.session;
	//res.render('loading');
	var spawnSync = require('child_process');
    py = spawnSync.spawnSync('python', ['./testingimg.py',`${data1.username}`]);
	var outputimg = py.stdout;
	console.log(`${outputimg}`);
	if (`${outputimg}`==1)
		{
			console.log("welcome");
			que = `SELECT uid FROM USER WHERE username='${data1.username}';`;
			db.all(que,function(err,result){
				if (err) throw err;
				console.log(result);
				sess.user = {
					userid : result[0]["uid"]
				};
			});
			sess.user = {
				username : data1.username
			};
			console.log(`${sess.user.username}`);
			//res.redirect('/?valid='+sess.user.username);
			res.redirect('/');
			res.end();
		}else
		{
			console.log("wrong user");
			res.redirect('/loginerror');
		}
	// que = `SELECT *  FROM USER WHERE username='${data1.username}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
   
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
	
		// var k=result[0];
		// console.log('1'+k);
		// console.log('USER');
		// console.log(k.username);
		// user=k.username;
		// console.log('the username is'+user);
		
		// if(result.length!=0)
			// res.write('1');

		// else 
			// res.write('0');

		// res.end();

	// });
	// console.log(data1);
});

router.get('/loginerror', function (req, res) {
	res.render("exampleerrorlogin");
});

router.get('/logout',function(req,res,next){
	if(req.session){
		req.session.destroy((err)=>{
			sess = {};
			console.log("you have been logged out");
			res.redirect('/');
		});
	}
});

// app.get('/gstaffdetail', function(req, res){
	// var data = req.all;

	// console.log('this is ground staff site');
	// console.log('user is '+ user);
	// console.log(data.username);

	// que = `INSERT INTO GROUND SELECT sportname,gid,groundname,gaddress1,gaddress2,gaddress3,gzipcode,rating,gstaffid,slot,price  FROM GROUND2 WHERE username='${data.username}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);

	// });

	// console.log(data);
// });

router.post('/signupdetail', function(req, res){
	console.log("test");
	var data = req.body;
	//console.log("test:",data);
	que2 = `INSERT into USER(firstname,lastname,username,address1,address2,faceno,booking1) VALUES('${data.firstname}','${data.lastname}','${data.username}','${data.address1}','${data.address2}','${data.imgdata}',NULL);`;
	data_img = data['imgdata'];
	var data1 = data_img.replace(/^data:image\/\w+;base64,/, "");
	var buf = new Buffer(data1, 'base64');
	fss.writeFile('image.png', buf,(err,result)=>{
		if(err) throw err;
	});
	db.all(que2, function(err, result){
		if (err) throw err;
		console.log(result);
		res.end();
	});
	res.redirect('/');
	console.log(data);
});

// app.get('/staffsignupdetail', function(req, res){
	// var data = req.body;

	// que = `Insert into GROUND_STAFF VALUES('${data.staffname}','${data.staffid}','${data.mobileno}');`;
	// db.all(que, function(err, result){
		// if (err) throw err;

		// console.log(result);

		// res.end();

	// });
	// que = `Insert into GROUND VALUES('${data.sportname}','${data.gid}','${data.groundname}','${data.address1}','${data.address2}','${data.address3}','${data.zipcode}','${data.rating}','${data.staffid}','${data.slot}','${data.price}');`;
	// db.all(que, function(err, result){
		// if (err) throw err;

		// console.log(result);

		// res.end();

	// });
	// console.log(data);
// });

router.get('/football',function(req,res){
	//var data = req.body;
	//que = 'SELECT gid,tid,groundname,location,rating,sportsname from GROUND WHERE sportsname="football" and safety="1";';
	if(!sess){
		console.log(req.session);
		res.redirect('/login');
		res.end();
	}else
	{
	que1 = `SELECT * from GROUND WHERE sportsname='football' and safety='1';`;
	console.log(`${que1}`);
	db.all(que1,function(err,result){
		if(err) throw err;
		console.log(result);
		res.render('footballselect',{places:result,});
	});
	}
});

router.get('/footballbooked',function(req,res){
	//var data = req.body;
	//que = 'SELECT gid,tid,groundname,location,rating,sportsname from GROUND WHERE sportsname="football" and safety="1";';
	if(!sess){
		console.log(req.session);
		res.redirect('/login');
		res.end();
	}else
	{
	que1 = `SELECT * from GROUND WHERE sportsname='football' and safety='1';`;
	console.log(`${que1}`);
	db.all(que1,function(err,result){
		if(err) throw err;
		console.log(result);
		res.render('footballselectbooked',{places:result,});
	});
	}
});

router.get('/booking',function(req,res){
	var data = req.query.gid;
	console.log(`${data}`);
	que = `SELECT * FROM BOOKINGS WHERE gid='${data}';`;
	db.all(que,function(err,result){
		if (err) throw err;
		if(result.length!=0){
			console.log("invalid");
			console.log(result);
			res.redirect('/footballbooked');
		}else{
			console.log("valid");
			console.log(result);
			res.render('finalbooking',{ground:data});
		}
	});
});

router.post('/confirmed',function(req,res){
	var data = req.query.gid;
	var data1 = req.body;
	console.log(`${sess.user.username}`);
	console.log("I have reached here");
	console.log(`${data}`);
	console.log(`${data1.bookdate}`);
	que = `INSERT INTO BOOKINGS(gid,uid) VALUES ('${data}','${sess.user.userid}');`;
	db.all(que,function(err,result){
		if (err) throw err;
		console.log('success');
		res.redirect('/');
	});
});

router.get('/workout',function(req,res){
	if(!req.session){
		res.redirect('/login');
	}else{
	res.render('exercise2');
	}
});

router.get('/currentbookings',function(req,res){
	que = `SELECT GROUND.groundname,TIMESLOTS.time FROM ((BOOKINGS INNER JOIN GROUND ON BOOKINGS.gid = GROUND.gid) INNER JOIN TIMESLOTS ON TIMESLOTS.tid = GROUND.tid) WHERE BOOKINGS.uid='${sess.user.userid}';`
	console.log(`${sess}`);
	db.all(que,function(err,result){
		if (err) throw err;
		console.log('success');
		console.log(result);
		res.render('current',{status:result});
	});
});

// router.get('/bookingdetail', function(req, res){
	// var data = req.all;

	// que = `SELECT * FROM GROUND WHERE sportname='${data.Sport}' and slot='${data.Slot}' and gaddress3='${data.Location}';`;
	// db.all(que, function(err, result){
		// if (err) throw err;

		// console.log(result);
		// var k;
		// k=JSON.stringify(result);
		// if(result.length==0)
		// {
			// res.write('no grounds available');
		// }
		// else
		// {

		// res.write(k);}

		// res.end();
		// });
	// });

// router.get('/bookingupdate', function(req, res){
// var data = req.all;
// console.log('the name of the user is '+user);

	// que=`SELECT booking1,booking2 FROM USER WHERE username='${user}'`;
	// db.all(que, function(err, result){
		
		// if (err) throw err;
		
	
			// console.log(result);
			// console.log(JSON.stringify(result[0].booking1));
				// console.log(JSON.stringify(result[0].booking2));

			// if(JSON.stringify(result[0].booking1)=='null')
		// {
			// console.log('inside if    @@@@@@@@@@@@@@@@@@');
			// que = `update USER set booking1='${data.groundname}' where username='${user}'`;
			// db.all(que, function(err, result){
			// if (err) throw err;

			// console.log(result);
			// console.log('chalgaya');
			// var k;
			// res.end();
		// });
		// }
		// else if(JSON.stringify(result[0].booking2)=='null')
		// {
			// console.log('inside elseif    @@@@@@@@@@@@@@@@@@');
			// que = `update USER set booking2='${data.groundname}' where username='${user}'`;
			// db.all(que, function(err, result){
			// if (err) throw err;

			// console.log(result);
			// console.log('chalgaya');
			// var k;
			// res.end();

		// });
		// }

	// else 
		// {
			// var k='ALREADY EXCEEDS MAX BOOKING';
			// res.write(k);
		// console.log('nhi chala');
		// res.end();
	// }

	



	/*que = `update USER set booking1='${data.groundname}' where username='${user}'`;
	db.all(que, function(err, result){
		if (err) throw err;

		console.log(result);
		console.log('chalgaya');
		var k;
		

		res.end();

	});*/

	// console.log(data);
// });
	
	
	// que=`INSERT INTO GROUND2(username) VALUES('${user}');`
	// db.all(que, function(err, result){
			// if (err) throw err;

			// console.log(result);
			// console.log('chalgaya');
			// var k;
		

			// res.end();

		// });

	// que=`DELETE FROM GROUND WHERE groundname='${data.groundname}' and slot='${data.slot}';`
	// db.all(que, function(err, result){
			// if (err) throw err;

			// console.log(result);
			// console.log('chalgaya');
			// var k;
		

			// res.end();

		// });		



// });

router.get('/', function(req, res){
	//console.log(req.query.valid);
	if(req.session.user)
	{
	res.render('index',{authenticated:req.session.user.username});
	}else{
		res.render('index',{authenticated:0});
	}
});

/*app.get('/signup', function(req, res){
	res.render('signup');
});*/

router.get('/signup', function(req, res){
	res.render('examplesignup');
});

/*app.get('/login', function(req, res){
	res.render('login');
});*/

router.get('/login', function(req,res){
	res.render('examplelogin');
});

router.get('/bookings', function(req, res){
	res.render('bookings');
});
// router.get('/gstaff', function(req, res){
	// res.render('gstaff');
// });
// router.get('/gstaffadd', function(req, res){
	// res.render('gstaffadd');
// });
// router.get('/gstaffloginadd', function(req, res){
	// res.render('gstaffloginadd');
// });
// app.get('/gstafflogin', function(req, res){
	// res.render('gstafflogin');
// });
// app.get('/staffsignup', function(req, res){
	// res.render('staffsignup');
// });

// app.get('/gstaffmaintainance', function(req, res){
	// res.render('gstaffmaintainance');
// });
// app.get('/gstafflogindetail', function(req, res){
	// var data = req.all;

	// que = `SELECT *  FROM GROUND_STAFF WHERE staffname='${data.username}' and staffid='${data.password}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=result[0];
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k.staffname);
		// staff=k.staffname;
		// console.log('the username is'+staff);
		
		// if(result.length!=0)
			// res.write('1');

							

		// else 
			// res.write('0');

		// res.end();

	// });

	// console.log(data);
// });
// app.get('/gstaffloginadddetail', function(req, res){
	// var data = req.all;

	// que = `SELECT *  FROM GROUND_STAFF WHERE staffname='${data.username}' and staffid='${data.password}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=result[0];
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k.staffname);
		// staff=k.staffname;
		// console.log('the username is'+staff);
		
		// if(result.length!=0)
			// res.write('1');

							

		// else 
			// res.write('0');

		// res.end();

	// });

	// console.log(data);
// });
// app.get('/gstaffmaintainancedetail', function(req, res){
	// var data = req.all;

	// que = `SELECT *  FROM GROUND A, GROUND_STAFF B WHERE B.staffid=A.gstaffid and staffname='${staff}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
		// staffid=result[0].gstaffid;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=JSON.stringify(result);
		// res.write(k);
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k);
		// res.end();
		
		
		
	// });

	// console.log(data);
// });
// app.get('/gstaffmaintainancedetail2', function(req, res){
	// var data = req.all;

	// que = `DELETE FROM GROUND WHERE gstaffid='${staffid}' and slot='${data.slot}'` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=JSON.stringify(result);
		// res.write(k);
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k);
		// res.end();
		
		
		
	// });

	// console.log(data);
// });
// app.get('/gstaffadddetail', function(req, res){
	// var data = req.all;

	// que = `SELECT *  FROM GROUND A, GROUND_STAFF B WHERE B.staffid=A.gstaffid and staffname='${staff}';` ;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// g=result[0];
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=JSON.stringify(result);
		// res.write(k);
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k);
		// res.end();
		
		
		
	// });

	// console.log(data);
// });

// app.get('/gstaffadddetail2', function(req, res){
	// var data = req.all;

	// que = `INSERT into GROUND VALUES('${g.sportname}','${g.gid}','${g.groundname}','${g.gaddress1}','${g.gaddress2}','${g.gaddress3}','${g.gzipcode}','${g.rating}','${g.gstaffid}','${data.slot}','${g.price}');`;

	// db.all(que, function(err, result){
		// if (err) throw err;
    
		// console.log('RESULT');
		// console.log(result);
		// console.log('RESULT LENGTH');
		// console.log(result.length);
		
		// var k=JSON.stringify(result);
		// res.write(k);
		//console.log('1'+k);
		// console.log('USER');
		// console.log(k);
		// res.end();
		
		
		
	// });

	// console.log(data);
// });





