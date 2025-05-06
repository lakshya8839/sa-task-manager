document.addEventListener("DOMContentLoaded", () => {
    const taskInput = document.querySelector('input[name="task"]');
    const addForm = document.querySelector('form[action="/"]');
    const tasks = document.querySelectorAll(".task-item");
  
    // Autofocus input
    if (taskInput) taskInput.focus();
  
    // Prevent empty submission
    addForm.addEventListener("submit", (e) => {
      if (!taskInput.value.trim()) {
        e.preventDefault();
        taskInput.style.border = "1px solid red";
        setTimeout(() => (taskInput.style.border = ""), 1500);
      }
    });
  
    // Animate task items
    tasks.forEach((task, i) => {
      task.style.opacity = 0;
      setTimeout(() => {
        task.style.transition = "opacity 0.4s ease";
        task.style.opacity = 1;
      }, i * 100);
    });
  });
  