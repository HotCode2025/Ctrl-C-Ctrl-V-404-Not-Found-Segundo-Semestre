// Ejercicio 2: Crear un sistema simple de gestión de tareas

function createTaskManager() {

    let tasks = [];

    return {

        addTask: function(task) {

           tasks.push({ id: tasks.length + 1, description: task, completed: false });

        },

        completeTask: function(taskId) {

            const task = tasks.find(t => t.id === taskId);

            if (task) {
                task.completed = true;
                console.log(`Tarea ${taskId} ${task.description} completada`);
            }else {
                console.log("Tarea no encontrada");
            }

        },

        listTasks: function() {

            return tasks;

        }

    };

}


// Uso:

// Crear un gestor de tareas
const myTasks = createTaskManager();

// Agregar tareas
myTasks.addTask("Aprender JavaScript");

myTasks.addTask("Practicar coding challenges");

myTasks.addTask("Hacer ejercicio");

// completar una tarea
myTasks.completeTask(1);

myTasks.completeTask(4); // Tarea no encontrada

// Listar todas las tareas
console.log(myTasks.listTasks());