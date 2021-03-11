// JavaScript source code

//making elements
var title = document.createElement("h2")
title.innerText = "Title"
var text = document.createElement("p")
text.innerText = "paragraph"

//appending elements to HTML document
document.body.appendChild(title)
document.body.appendChild(text) 

//modify element
var y = document.getElementById("change")
y.innerHTML = "Element Changed"

//change attribute
var img = document.getElementById("testimg")
img.src = "https://upload.wikimedia.org/wikipedia/commons/7/73/Javascript-736400_960_720.png"