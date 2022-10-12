//grap the elements from the dom tree
const todoInput = document.querySelector(".todo-input");
const todoButton = document.querySelector(".todo-button");
const todoList = document.querySelector(".todo-list");
const todoFilter = document.querySelector(".filter-todo");

//event listners
document.addEventListener('DOMContentLoaded',retriveItem);
todoButton.addEventListener('click',addtodo);
//event delegation
todoList.addEventListener('click',deletecheck);
todoFilter.addEventListener('click',filterItem);



function addtodo(event){
   if(todoInput.value==''){
       alert("add something");
       event.preventDefault();
   }
   else{
         //container for each task
   const newTodo = document.createElement('div');
   newTodo.className='todo';

   //list
   const newTodoItem = document.createElement('li');
   newTodoItem.className='todo-item';
   newTodoItem.innerText=todoInput.value;
   newTodo.appendChild(newTodoItem);
   //saving the input to the local storage.
   saveLocalStorage(todoInput.value);


   //checked button
   const checkedButton = document.createElement('button');
   checkedButton.innerHTML='<i class="fas fa-check"></i>'
   checkedButton.className='checked-btn';
   newTodo.appendChild(checkedButton);


   //trash button
   const trashButton = document.createElement('button');
   trashButton.className='trash-btn';
   trashButton.innerHTML='<i class="fas fa-trash"></i>'
   newTodo.appendChild(trashButton);

   //add the created container to ul
   todoList.appendChild(newTodo);

   //emptying todoinput after adding it to the list
   todoInput.value='';

   //prevent submitting the form
   event.preventDefault();
   }
   
}  

function deletecheck(e){
    if(e.target.className ==='trash-btn'){
       const todo = e.target.parentElement
       todo.classList.add('fall');
       removeFromStorage(todo);
       todo.addEventListener('transitionend',function(){
           todo.remove();
       });
    }
    if(e.target.className ==='checked-btn'){
       const todo =e.target.parentElement.classList.toggle('completed');
    }
    
}

function filterItem(e){
   
    const todos = Array.from(todoList.children);
    todos.forEach(function(todo){
        switch (e.target.value) {
            case 'All':
                todo.style.display="flex";
                break;
            case 'completed':
                if(todo.className == "todo completed"){
                 todo.style.display ="flex";
                }
                else{
                    todo.style.display ='none';
                }
                break;
            case 'uncompleted':
                if(todo.className =="todo"){
                    todo.style.display ="flex";
                }
                else{
                    todo.style.display ='none';
                }
                break;
            default:
                break;
        }
    })
   
}

function checkLocalStorage(){
    if(localStorage.getItem('todos')===null){
      return  todos =[];
    }
    else{
      return  todos =JSON.parse(localStorage.getItem('todos'));
    }
}
function saveLocalStorage(todo){
    const todos = checkLocalStorage();
    todos.push(todo);
    localStorage.setItem('todos',JSON.stringify(todos));
}

function removeFromStorage(todo){
  const deletedItem=todo.children[0].innerHTML;
  console.log(deletedItem);
  const todoListSaved= checkLocalStorage();
  const indexOfDeletedItem = todoListSaved.indexOf(deletedItem);
  todoListSaved.splice(indexOfDeletedItem,1);
  localStorage.setItem("todos",JSON.stringify(todoListSaved));

}

function retriveItem(){
    const storedTodos =checkLocalStorage();
    storedTodos.forEach(function(storedTodo){
        const newTodo = document.createElement('div');
        newTodo.className='todo';
     
        //list
        const newTodoItem = document.createElement('li');
        newTodoItem.className='todo-item';
        newTodoItem.innerText=storedTodo;
        newTodo.appendChild(newTodoItem);

                //checked button
        const checkedButton = document.createElement('button');
        checkedButton.innerHTML='<i class="fas fa-check"></i>'
        checkedButton.className='checked-btn';
        newTodo.appendChild(checkedButton);


        //trash button
        const trashButton = document.createElement('button');
        trashButton.className='trash-btn';
        trashButton.innerHTML='<i class="fas fa-trash"></i>'
        newTodo.appendChild(trashButton);

        //add the created container to ul
        todoList.appendChild(newTodo);

    })
   
}
