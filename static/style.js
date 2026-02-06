const form = document.getElementById("studentForm");
const list = document.getElementById("studentsList");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const course = document.getElementById("course").value;

    await fetch("/add-student", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, course })
    });

    form.reset();
    loadStudents();
});

async function loadStudents() {
    const res = await fetch("/students");
    const data = await res.json();

    list.innerHTML = "";
    data.students.forEach(student => {
        const li = document.createElement("li");
        li.textContent = `${student.name} - ${student.course}`;
        list.appendChild(li);
    });
}

loadStudents();