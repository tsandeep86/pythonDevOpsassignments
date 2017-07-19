
function login() {
	username= document.getElementById('username').value;
	password=document.getElementById('password').value;
	console.log(username,password);
	$.ajax( {
	type:'GET',
	url:'/get_data/',
	data:{'username':username,'password':password},
	dataType:"json",
	success:function (data) {
		console.log(">>>>",data);
	if (data['result']=='True'){
		console.log(data);
		window.location.href="http://127.0.0.1:5000/userinput";
	}
	
	else{
		console.log("In else")
		window.location.href="http://127.0.0.1:5000/logonpage";
	     console.log("In else")
		}
	},
	error:function(error) {
		console.log(error);
		}
	});
console.log('exit');
}

function username() {
	username= document.getElementById('username').value;
	console.log(username);
	$.ajax( {
	type:'GET',
	url:'/userinfo/',
	data:{'username':username},
	dataType:"json",
	success:function (data) {
		console.log(">>>>",data);
	if (data){
		console.log(data);
		var route= data.result;
		var name= data.name;
		console.log(route, name);
		window.location.href=route;
	
	}
	
	else{
		console.log("In else")
		window.location.href="http://127.0.0.1:5000/userinput";
	     console.log("In else")
		}
	},
	error:function(error) {
		console.log(error);
		}
	});
console.log('exit');
}