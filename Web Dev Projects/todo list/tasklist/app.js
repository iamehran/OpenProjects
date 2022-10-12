const form =document.querySelector("#task-form");
const taskList = document.querySelector(".collection");
const clearBtn = document.querySelector("#clear-tasks");
const filter = document.querySelector("#filter");
const taskInput = document.querySelector("#task");

//load all the event listners
loadEventListner();

function loadEventListner(){
    form.addEventListener('submit',addTask);
    taskList.addEventListener('click',removeElement);
    clearBtn.addEventListener('click',clearall);
}

function addTask(e){
    if(taskInput.value == ''){
        alert("add some task");
 
    }
    else{
     //create a li element and append into the task list
        const li = document.createElement("li");
        li.className="collection item";
        li.innerText = taskInput.value;
      
        e.preventDefault();
           
        //create a link
        const a =document.createElement("a");
        a.className = "secondary-content";
        a.innerHTML= '<i class="fa fa-remove"></i>';
        li.appendChild(a);
        taskList.appendChild(li);
        
        li.appendChild(a);
        taskList.appendChild(li);
        taskInput.value = '';
    }
   
}

function removeElement(e){
    if(e.target.parentElement.className =="secondary-content"){
        taskList.removeChild(e.target.parentElement.parentElement);
    }
   
}
function clearall(e){
    taskList.innerHTML ='';
}

