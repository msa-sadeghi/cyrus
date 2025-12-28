let notes = []
let currentFilter = "all"

function loadNotes(){
    let stored = localStorage.getItem('notes')
    if(stored){
        notes = JSON.parse(stored)
    }
}

function saveNotes(){
    localStorage.setItem("notes", JSON.stringify(notes))
}

function addNote(){
    let title = document.getElementById("noteTitle").value
    let content = document.getElementById("noteContent").value
    let category = document.getElementById("noteCategory").value

    let note = {
        id : Date.now(),
        title:title,
        content:content,
        category:category,
        date:new Date()
    }
    notes.push(note)
    document.getElementById("noteTitle").value = ''
    document.getElementById("noteContent").value = ''
    saveNotes()
    renderNotes()
}
function renderNotes(){
    let grid = document.getElementById("notesGrid")
    let filtered = currentFilter === "all" ? notes :
    notes.filter(note => note.category === currentFilter)
    if(filtered.length === 0){
        grid.innerHTML = `
        <div>
        <div class="empty-state-icon">📝</div>
                <p>there is no note </p>
                <p style="font-size: 14px; margin-top: 10px;">  Add your first note  </p>
            
        </div>
        `
        return
    }
    grid.innerHTML =  ''
    filtered.forEach(note => {
        let noteDiv = document.createElement("div")
        noteDiv.className = "note"
        let headerDiv = document.createElement("div")
        headerDiv.className = 'note-header'

        let categorySpan =  document.createElement('span')
        categorySpan.className = `note-category category-${note.category}`
        categorySpan.textContent = note.category

        headerDiv.append(categorySpan)
        noteDiv.append(headerDiv)
        grid.append(noteDiv)
        
        
    })

}