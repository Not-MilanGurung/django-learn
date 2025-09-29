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
    if (!confirm("Are you sure you want to delete genre '" + name + "'?")) return;
    fetch(`/genres/${encodeURIComponent(name)}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // if needed for CSRF/session
        },
        credentials: 'include'  // required for JWT in cookies
    })
    .then(response => {
        if (response.status === 204) {
            // Success: remove genre from DOM
            document.getElementById('genre_' + name).remove();
        } else {
            return response.json().then(data => {
                alert("Error: " + (data.detail || "Could not delete genre."));
            });
        }
    })
    .catch(err => {
        console.error(err);
        alert("Network error while deleting genre.");
    });
}

function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? decodeURIComponent(match[2]) : null;
}

function confirmEdit(name) {
    const newName = document.getElementById('input_' + name).value;
    if (newName.trim() === '') {
        alert('New genre name cannot be empty.');
        return false;
    }
    if (confirm("Change genre '" + name + "' to '" + newName + "'?")) {
        fetch(`/genres/${encodeURIComponent(name)}/`, {
			method: 'DELETE',
			headers: {
				'X-CSRFToken': getCookie('csrftoken')  // if needed for CSRF/session
			},
			credentials: 'include'  // required for JWT in cookies
		})
		.then(response => {
			if (response.status === 204) {
				// Success: remove genre from DOM
				document.getElementById('genre_' + name).remove();
			} else {
				return response.json().then(data => {
					alert("Error: " + (data.detail || "Could not delete genre."));
				});
			}
		})
		.catch(err => {
			console.error(err);
			alert("Network error while deleting genre.");
		});
    }
}
