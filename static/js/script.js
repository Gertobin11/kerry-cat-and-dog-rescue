let logoDiv = document.querySelector(".logo-div");

let logo = document.querySelector(".logo");

let downIcons = Array.from(document.getElementsByClassName("fa"));

let dropDownItems = Array.from(document.querySelectorAll(".drop-list"));

let menuBtn = document.querySelector(".menu-btn");

let navList = document.querySelector(".nav-list")

let dropDownLinks = Array.from(document.getElementsByClassName("drop-down-link"))

let menuOpen = false;

let linkOpen = Boolean

// Function for opening and closing the mobile hamburger


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

// Functions for setting how the anchor texts appear on the screen

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

// Adding event listeners for when the nav is hovered over and exited

dropDownLinks.forEach(dropDownLink => {
    dropDownLink.addEventListener("mouseleave", function () {
        this.children[1].classList.remove("show", "show-ul")
        this.children[0].classList.remove("drop")
        this.children[1].classList.add("hide")
        hideDropDownItems()
        linkOpen = false
    })
})

dropDownLinks.forEach(dropDownLink => {
    dropDownLink.addEventListener("mouseenter", function () {
        this.children[1].classList.remove("hide")
        this.children[0].classList.add("drop")
        this.children[1].classList.add("show", "show-ul")
        linkOpen = true
        setTimeout(showDropDownItems, 200)
    })
})

// Event listener for whn the logo is hovered

logoDiv.addEventListener("mouseenter", function (event) {
    logo.classList.add('logo-rotate')
})

logoDiv.addEventListener("mouseleave", function (event) {
    logo.classList.remove('logo-rotate')
})



// Adding click functionality to the dog/cat/account links for ux in mobile views
dropDownLinks.forEach(dropDownLink => {
    dropDownLink.addEventListener("click", function() {
        if (linkOpen) {
            this.children[1].classList.remove("show", "show-ul")
            this.children[1].classList.add("hide")
            linkOpen = false;
        } else {
            this.children[1].classList.add("show", "show-ul")
            this.children[1].classList.remove("hide")
            linkOpen = true;
        }
    })
})


/// JavaScript for Dismissing the messages displayed to the user

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

const upBtn = document.getElementById("button-up");
const downBtn = document.getElementById("button-down");

window.onscroll = function () {
    scrollFunction()
}

const scrollFunction = () => {
    if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
        upBtn.style.display = "block";
    } else {
        upBtn.style.display = "none";
    }
}

function topFunction() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function scrollDown() {
    window.scrollBy({
        behavior: "smooth",
        top: 600
    })
}

upBtn.addEventListener('click', topFunction)
downBtn.addEventListener('click', scrollDown)