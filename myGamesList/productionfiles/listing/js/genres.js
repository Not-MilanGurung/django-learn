function enableEdit(name) {
    document.getElementById('display_' + name).style.display = 'none';
    document.getElementById('input_' + name).style.display = 'inline';
    document.getElementById('edit_' + name).style.display = 'inline';
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
