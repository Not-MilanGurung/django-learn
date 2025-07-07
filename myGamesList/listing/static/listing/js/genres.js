function enableEdit(name) {
    document.getElementById('display_' + name).style.display = 'none';
    document.getElementById('edit_confirm_' + name).textContent = 'Confirm';
    document.getElementById('delete_cancel_' + name).textContent = 'Cancel';

    document.getElementById('input_' + name).style.display = 'inline';
}

function cancelEdit(name) {
	document.getElementById('display_' + name).style.display = 'inline';
	document.getElementById('edit_confirm_' + name).textContent = 'Edit';
	document.getElementById('delete_cancel_' + name).textContent = 'Delete';

	document.getElementById('input_' + name).style.display = 'none';
}

function deleteCancel(name) {
	var deleteCancelbtn = document.getElementById('delete_cancel_' + name);
	if (deleteCancelbtn.textContent == 'Delete') {
		confirmDelete(name);
	}
	else {
		cancelEdit(name);
	}

}

function editConfirm(name) {
	var editConfirmbtn = document.getElementById('edit_confirm_'+name);
	if (editConfirmbtn.textContent == 'Edit') {
		enableEdit(name);
	}
	else {
		confirmEdit(name);
	}
}

function confirmDelete(name) {
    if (confirm("Are you sure you want to delete genre '" + name + "'?")) {
        document.getElementById('delete_form_' + name).submit();
    }
}

function confirmEdit(name) {
    const newName = document.getElementById('input_' + name).value;
    if (newName.trim() === '') {
        alert('New genre name cannot be empty.');
        return false;
    }
    if (confirm("Change genre '" + name + "' to '" + newName + "'?")) {
        document.getElementById('edit_form_' + name).submit();
    }
}
