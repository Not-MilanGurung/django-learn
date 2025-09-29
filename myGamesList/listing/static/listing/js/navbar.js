function confirmLogout() {
	if (confirm("Are you sure you want to logout?")){
		document.getElementById("logout_form").submit();
	}
}