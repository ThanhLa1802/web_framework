const deleteNote = (noteId) => {
    console.log(noteId)
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({note_id: noteId}),
    }).then( (response) => {
    window.location.href = "/";
    })
}