// JavaScript source code

//Making Elements
function addElement() {
    var title = document.createElement("h2")
    title.innerText = "Title"
    var text = document.createElement("p")
    text.innerText = "paragraph"

    //Appending elements
    document.body.appendChild(title)
    document.body.appendChild(text) 
}

//Modify Element
function modifyContent(){
    var y = document.getElementById("change")
    y.innerHTML = "Element Changed"
}


//Change Attribute
function changeAttribute() {
    var img = document.getElementById("testimg")
    img.src = "https://upload.wikimedia.org/wikipedia/commons/7/73/Javascript-736400_960_720.png"
}

//Change CSS
function changeColor(color, id) {
    var element = document.getElementById(id)
    element.style.color = color
}

//Change to dark class
function darkMode() {
     document.body.classList.add("dark")
}

