// JavaScript source code

//list of cart item objects
var cartItems = [
    {
        imgPath: "./img/green-tea.jpg",
        nameOfTea: "green tea",
        size: "small",
        quantity: 2,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/white-tea.jpg",
        nameOfTea: "white tea",
        size: "small",
        quantity: 2,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/chamomile-tea.jpg",
        nameOfTea: "chamomile tea",
        size: "medium",
        quantity: 4,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/herbal-tea.jpg",
        nameOfTea: "herbal tea",
        size: "medium",
        quantity: 4,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/lemon-tea.jpg",
        nameOfTea: "lemon tea",
        size: "medium",
        quantity: 4,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/rose-tea.jpg",
        nameOfTea: "rose tea",
        size: "large",
        quantity: 8,
        priceArray: [3, 5, 7]
    },
    {
        imgPath: "./img/vanilla-tea.jpg",
        nameOfTea: "vanilla tea",
        size: "large",
        quantity: 7,
        priceArray: [3, 5, 7]
    }
]

var items_container = document.getElementById("cart-items")

//iterating through the list of cart item objects
for (var n of cartItems) {
    var cartElement = document.createElement("div")
    cartElement.classList.add("card")
    cartElement.innerHTML = `
    <img class="tea-picture" src=${n.imgPath} alt="${n.nameOfTea} image">
    <div class="nameOfTea"><b>${n.nameOfTea}</b></div>
    <div class="size-quantity"><b>size: </b>${n.size}</b><br/><b>quantity:</b> ${n.quantity}</div>
    <div class="price-delete"><b>price: </b> 34$ <button class="delete">delete item</button></div>
    `
    items_container.appendChild(cartElement)
}
