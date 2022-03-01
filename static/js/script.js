let catsLink = document.getElementById("cats-link")
let catList = document.getElementById("cats-list")
let dogsLink = document.getElementById("dogs-link")
let dogList = document.getElementById("dogs-list")
let logoDiv = document.querySelector(".logo-div")
let logo = document.querySelector(".logo")
let downIcons = Array.from(document.getElementsByClassName("fa"))
console.log(downIcons)
console.log(logo)
catList.classList.add("hide");
dogList.classList.add("hide");


catList.addEventListener("mouseleave", function (event) {
    console.log('listeneradded')
    catList.classList.remove("show")
    catList.classList.add("hide")
})

catsLink.addEventListener("click", function (event) {
    catList.classList.add("show")
    console.log('show')
})

dogList.addEventListener("mouseleave", function (event) {
    console.log('listeneradded')
    dogList.classList.remove("show")
    dogList.classList.add("hide")
})

dogsLink.addEventListener("click", function (event) {
    dogList.classList.add("show")
    console.log('show')
})

logoDiv.addEventListener("mouseenter", function(event) {
    logo.classList.add('logo-rotate')
})

logoDiv.addEventListener("mouseleave", function (event) {
    logo.classList.remove('logo-rotate')
})

catsLink.addEventListener("mouseenter", function(event) {
    downIcons[0].classList.add("drop")
})

catsLink.addEventListener("mouseleave", function (event) {
    downIcons[0].classList.remove("drop")
})

dogsLink.addEventListener("mouseenter", function (event) {
    downIcons[1].classList.add("drop")
})

dogsLink.addEventListener("mouseleave", function (event) {
    downIcons[1].classList.remove("drop")
})