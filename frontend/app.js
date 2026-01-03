const API = "http://127.0.0.1:5000";
let token = localStorage.getItem("token");

function saveToken(t) {
  token = t;
  localStorage.setItem("token", t);
}

function requireAuth() {
  if (!token) {
    alert("Please login first");
    throw new Error("Not authenticated");
  }
}

async function register() {
  const email = document.getElementById("reg-email").value;
  const password = document.getElementById("reg-password").value;

  if (!email || !password) {
    alert("Email and password required");
    return;
  }

  try {
    const res = await fetch(`${API}/auth/register`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Registration failed");

    alert("Registered successfully. You can now login.");
  } catch (err) {
    alert(err.message);
  }
}

async function login() {
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  if (!email || !password) {
    alert("Email and password required");
    return;
  }

  try {
    const res = await fetch(`${API}/auth/login`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Login failed");

    saveToken(data.token);
    alert("Logged in");
    loadNotes();
  } catch (err) {
    alert(err.message);
  }
}

function logout() {
  localStorage.removeItem("token");
  token = null;
  document.getElementById("notes").innerHTML = "";
  alert("Logged out");
}

async function createNote() {
  try {
    requireAuth();

    const title = document.getElementById("create-note-title").value;
    const content = document.getElementById("create-note-content").value;

    if (!title || !content) {
      alert("Title and content required");
      return;
    }

    const res = await fetch(`${API}/notes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({ title, content })
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || "Failed to create note");
    }

    document.getElementById("create-note-title").value = "";
    document.getElementById("create-note-content").value = "";

    loadNotes();
  } catch (err) {
    alert(err.message);
  }
}

async function loadNotes() {
  try {
    requireAuth();

    const id = parseInt(document.getElementById("list-note-id").value, 10);
    const list = document.getElementById("notes");
    list.innerHTML = "";

    const url = id === -1 ? `${API}/notes` : `${API}/notes/${id}`;

    const res = await fetch(url, {
      headers: { "Authorization": `Bearer ${token}` }
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Failed to load notes");

    const notes = Array.isArray(data) ? data : [data];

    notes.forEach(n => {
      const li = document.createElement("li");
      li.innerText = `${n.id}. ${n.title}: ${n.content}`;
      list.appendChild(li);
    });
  } catch (err) {
    alert(err.message);
  }
}

async function editNote() {
  try {
    requireAuth();

    const id = parseInt(document.getElementById("edit-note-id").value, 10);
    const title = document.getElementById("edit-note-title").value;
    const content = document.getElementById("edit-note-content").value;

    if (!id || !title || !content) {
      alert("Note ID, title and content required");
      return;
    }

    const res = await fetch(`${API}/notes/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({ title, content })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Failed to edit note");

    document.getElementById("edit-note-id").value = "";
    document.getElementById("edit-note-title").value = "";
    document.getElementById("edit-note-content").value = "";

    loadNotes();
  } catch (err) {
    alert(err.message);
  }
}

async function deleteNote() {
  try {
    requireAuth();

    const id = parseInt(document.getElementById("delete-note-id").value, 10);
    if (!id) {
      alert("Note ID required");
      return;
    }

    if (!confirm("Delete this note?")) return;

    const res = await fetch(`${API}/notes/${id}`, {
      method: "DELETE",
      headers: { "Authorization": `Bearer ${token}` }
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || "Failed to delete note");
    }

    document.getElementById("delete-note-id").value = "";
    loadNotes();
  } catch (err) {
    alert(err.message);
  }
}
