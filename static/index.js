setTimeout(function() {
    let alertElement = document.getElementById("autoDismissAlert");
    if (alertElement) {
        alertElement.classList.remove("show");
        alertElement.classList.add("fade");
        setTimeout(() => alertElement.remove(), 500); // Remove element after fade-out
    }
}, 5000); // 5 seconds

function deleteNote(noteId) {
    fetch('/delete-note', {
        method: "POST",
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = '/'
    })
}