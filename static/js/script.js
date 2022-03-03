let catsLink = document.getElementById("cats-link")
let catList = document.getElementById("cats-list")
let dogsLink = document.getElementById("dogs-link")
let dogList = document.getElementById("dogs-list")
let logoDiv = document.querySelector(".logo-div")
let logo = document.querySelector(".logo")
let downIcons = Array.from(document.getElementsByClassName("fa"))
let dropDownItems = Array.from(document.querySelectorAll(".drop-list"))
catList.classList.add("hide");
dogList.classList.add("hide");

const showDropDownItems = () => {
    dropDownItems.forEach(item => {
        item.classList.add("show-opacity")
    })
}

const hideDropDownItems = () => {
    dropDownItems.forEach(item => {
        item.classList.remove("show-opacity")
    })
}

dropDownItems.forEach(item => {
    item.classList.add("hide-opacity")
})

hideDropDownItems()


catsLink.addEventListener("mouseleave", function (event) {
    console.log('listeneradded')
    catList.classList.remove("show")
    catList.classList.add("hide")
    hideDropDownItems()
})

catsLink.addEventListener("mouseenter", function (event) {
    catList.classList.add("show", "show-ul")
    setTimeout(showDropDownItems, 200)
})

dogsLink.addEventListener("mouseleave", function (event) {
    console.log('listeneradded')
    dogList.classList.remove("show")
    dogList.classList.add("hide")
    hideDropDownItems()
})

dogsLink.addEventListener("mouseenter", function (event) {
    dogList.classList.add("show", "show-ul")
    console.log('show')
    setTimeout(showDropDownItems, 200)
})

logoDiv.addEventListener("mouseenter", function (event) {
    logo.classList.add('logo-rotate')
})

logoDiv.addEventListener("mouseleave", function (event) {
    logo.classList.remove('logo-rotate')
})

catsLink.addEventListener("mouseenter", function (event) {
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