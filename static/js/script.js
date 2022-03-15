let catsLink = document.getElementById("cats-link");

let catList = document.getElementById("cats-list");

let dogsLink = document.getElementById("dogs-link");

let dogList = document.getElementById("dogs-list");

let accountLink = document.getElementById("account-link")

let accountList = document.getElementById("account-list")

let logoDiv = document.querySelector(".logo-div");

let logo = document.querySelector(".logo");

let downIcons = Array.from(document.getElementsByClassName("fa"));

let dropDownItems = Array.from(document.querySelectorAll(".drop-list"));

let menuBtn = document.querySelector(".menu-btn");

let navList = document.querySelector(".nav-list")

let menuOpen = false;

let catsLinkOpen = false;

let dogsLinkOpen = false;

let accountMenuOpen = false

menuBtn.addEventListener("click", () => {
    if (!menuOpen) {
        menuBtn.classList.add("open")
        navList.classList.add("show", "show-ul")
        menuOpen = true;
    } else {
        menuBtn.classList.remove("open", "show-ul")
        navList.classList.remove("show")
        menuOpen = false;
    }
})

catList.classList.add("hide");
dogList.classList.add("hide");
accountList.classList.add("hide")

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
    catList.classList.remove("show")
    catList.classList.add("hide")
    hideDropDownItems()
})

catsLink.addEventListener("mouseenter", function (event) {
    catList.classList.add("show", "show-ul")
    setTimeout(showDropDownItems, 200)
})

dogsLink.addEventListener("mouseleave", function (event) {
    dogList.classList.remove("show")
    dogList.classList.add("hide")
    hideDropDownItems()
})

dogsLink.addEventListener("mouseenter", function (event) {
    dogList.classList.add("show", "show-ul")
    setTimeout(showDropDownItems, 200)
})

accountLink.addEventListener("mouseleave", function (event) {
    accountList.classList.remove("show")
    accountList.classList.add("hide")
    hideDropDownItems()
})

accountLink.addEventListener("mouseenter", function (event) {
    accountList.classList.add("show", "show-ul")
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
    catsLinkOpen = true;
})

catsLink.addEventListener("mouseleave", function (event) {
    downIcons[0].classList.remove("drop")
    catsLinkOpen = false;
})

dogsLink.addEventListener("mouseenter", function (event) {
    downIcons[1].classList.add("drop")
    dogsLinkOpen = true;
})

dogsLink.addEventListener("mouseleave", function (event) {
    downIcons[1].classList.remove("drop")
    dogsLinkOpen = true
})

accountLink.addEventListener("mouseenter", function (event) {
    downIcons[2].classList.add("drop")
    accountLinkOpen = true;
})

accountLink.addEventListener("mouseleave", function (event) {
    downIcons[2].classList.remove("drop")
    accountLinkOpen = true
})

// Adding click functionality to the dog/cat/account links for ux in mobile views

dogsLink.addEventListener("click", () => {
    if (dogsLinkOpen) {
        dogList.classList.remove("show")
        dogList.classList.add("hide")
        dogsLinkOpen = false;
    } else {
        dogList.classList.add("show")
        dogList.classList.remove("hide")
        dogsLinkOpen = true;
    }
})

catsLink.addEventListener("click", () => {
    if (catsLinkOpen) {
        catList.classList.remove("show")
        catList.classList.add("hide")
        catsLinkOpen = false;
    } else {
        catList.classList.add("show")
        catList.classList.remove("hide")
        catsLinkOpen = true;
    }
})

accountLink.addEventListener("click", () => {
    if (accountLinkOpen) {
        accountList.classList.remove("show")
        accountList.classList.add("hide")
        accountLinkOpen = false;
    } else {
        accountList.classList.add("show")
        accountList.classList.remove("hide")
        accountLinkOpen = true;
    }
})

/// JavaScript for Dismiising the messages displayed to the user

let messages = Array.from(document.getElementsByClassName('message-container'))

let messageBtn = Array.from(document.getElementsByClassName('dismiss'))

messageBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        btn.parentNode.parentNode.remove()
    })
})

// Close Message alert after 3 seconds

messages.forEach(message => {
setTimeout(function () {
    message.remove();
}, 3000)
})