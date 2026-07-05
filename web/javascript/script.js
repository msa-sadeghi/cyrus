let input = document.getElementById("input");
let addbtn = document.getElementById("add");
let list = document.getElementById("list");

let savedTasks = localStorage.getItem("tasks");
let tasks = JSON.parse(savedTasks) || [];

addbtn.addEventListener("click", function () {
  let taskText = input.value;

  tasks.push(taskText);

  localStorage.setItem("tasks", JSON.stringify(tasks));

  list.innerHTML = "";

  tasks.forEach(function (task) {
    list.innerHTML += "<li>" + task + "</li>";
  });
});

window.onload = function(){
  tasks.forEach(function (task) {
    list.innerHTML += "<li>" + task + "</li>";
  });
}
