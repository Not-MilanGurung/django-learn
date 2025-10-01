function confirmPassword(){
	var form = document.getElementById('registerForm') 
	const pass = form.password.value;
	const confirm = form.password_confirm.value;
	if (pass !== confirm) {
		alert("Passwords do not match!");
	}
	else {
		form.submit()
	}
	
}