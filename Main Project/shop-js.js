// JavaScript source code

//list of tea objects
var teaList = [
    {
        imgPath: "./img/green-tea.jpg",
        nameOfTea: "green tea",
        priceArray: [3,5,7]
    },
    {
        imgPath: "./img/white-tea.jpg",
        nameOfTea: "white tea",
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/chamomile-tea.jpg",
        nameOfTea: "chamomile tea",
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/herbal-tea.jpg",
        nameOfTea: "herbal tea",
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/lemon-tea.jpg",
        nameOfTea: "lemon tea",
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/rose-tea.jpg",
        nameOfTea: "rose tea",
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/vanilla-tea.jpg",
        nameOfTea: "vanilla tea",
        priceArray: [3, 5, 7]
    }
]

var items_container = document.getElementById("items")

//iterating through the list of tea objects
for (var n of teaList) {
    var teaElement = document.createElement("div")
    teaElement.classList.add("card")
    teaElement.innerHTML = `
    <img src= ${n.imgPath} alt="${n.nameOfTea} image">
    <p class="nameOfTea"><b>${n.nameOfTea}</b></p>
    <div class="size-selection">
        <div class="size">small</div>
        <div class="size">medium</div>
        <div class="size">large</div>
    </div>
    <button class="add-to-cart">add to cart</button>
    <div class = "price"><b>price:</b> ${n.priceArray[0]}\u20AC</div>
    `
    items_container.appendChild(teaElement)
}
