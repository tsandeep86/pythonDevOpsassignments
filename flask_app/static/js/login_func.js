
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
		window.location.href="http://127.0.0.1:5000/default/boot";
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