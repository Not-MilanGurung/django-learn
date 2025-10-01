function deleteGame(name) {
	if (confirm("Are you sure you want to delete game '" +name+ "'?")) {
		document.getElementById('delete_form_' + name).submit();
	}
}
