(() => {
    // Name all the elements in the carousel
    const itemClassName = "carousel-card"
    const items = Array.from(document.getElementsByClassName(itemClassName));
    const totalItems = items.length;
    let slide = 0;
    let moving = true;
    console.log(items)
    console.log(totalItems)

    // Set classes
    function setInitialClasses() {
        // Targets the previous, current, and next items
        // This assumes there are at least three items.
        items[totalItems - 1].classList.add("prev");
        items[0].classList.add("active");
        items[1].classList.add("next");
    }

    // Adding Event Liseners to the buttons
    function setEventListeners() {
        let next = document.getElementsByClassName('carousel-button-next')[0];
        let prev = document.getElementsByClassName('carousel-button-prev')[0];
        next.addEventListener('click', moveNext);
        prev.addEventListener('click', movePrev);
        // Adding event listeners to add animation when the button is clicked
        next.addEventListener('click', function() {
            next.classList.add('button-push')
            console.log('adding class')
            setTimeout(() => next.classList.remove('button-push'), 1100)
        });
        prev.addEventListener('click', function () {
            prev.classList.add('button-push');
            setTimeout(() => prev.classList.remove('button-push'), 1100)
        });
    }
    
    // Next navigation handler
    function moveNext() {
        // Check if moving
        if (!moving) {
            // If it's the last slide, reset to 0, else +1
            if (slide === (totalItems - 1)) {
                slide = 0;
            } else {
                slide++;
            }
            // Move carousel to updated slide
            moveCarouselTo(slide);
        }
    }
    // Previous navigation handler
    function movePrev() {
        // Check if moving
        if (!moving) {
            // If it's the first slide, set as the last slide, else -1
            if (slide === 0) {
                slide = (totalItems - 1);
            } else {
                slide--;
            }

            // Move carousel to updated slide
            moveCarouselTo(slide);
        }
    }

    function disableInteraction() {
        // Set 'moving' to true for the same duration as our transition.
        // (0.5s = 500ms)

        moving = true;
        // setTimeout runs its function once after the given time
        setTimeout(function () {
            moving = false
        }, 500);
    }

    function moveCarouselTo(slide) {
        // Check if carousel is moving, if not, allow interaction
        if (!moving) {
            console.log('function called')
            // temporarily disable interactivity
            disableInteraction();
            // Update the "old" adjacent slides with "new" ones
            let newPrevious = slide - 1;
            let newNext = slide + 1;
            let oldPrevious = slide - 2;
            let oldNext = slide + 2;
            // Test if carousel has more than three items
            if ((totalItems - 1) > 3) {
                // Checks and updates if the new slides are out of bounds
                if (newPrevious <= 0) {
                    oldPrevious = (totalItems - 1);
                } else if (newNext >= (totalItems - 1)) {
                    oldNext = 0;
                }
                // Checks and updates if slide is at the beginning/end
                if (slide === 0) {
                    newPrevious = (totalItems - 1);
                    oldPrevious = (totalItems - 2);
                    oldNext = (slide + 1);
                } else if (slide === (totalItems - 1)) {
                    newPrevious = (slide - 1);
                    newNext = 0;
                    oldNext = 1;
                }
                // Now we've worked out where we are and where we're going, 
                // by adding/removing classes we'll trigger the transitions.
                // Reset old next/prev elements to default classes
                items[oldPrevious].className = itemClassName;
                items[oldNext].className = itemClassName;
                // Add new classes
                items[newPrevious].classList = itemClassName + " prev";
                items[slide].classList = itemClassName + " active";
                items[newNext].classList = itemClassName + " next";
                console.log(items[newPrevious].classList)
                console.log(items[slide].classList)
                console.log(items[newNext].classList)
            }
        }
        else {
            console.log('function not called')
        }
    }
    function initCarousel() {
        setInitialClasses();
        setEventListeners();
        // Set moving to false so that the carousel becomes interactive
        moving = false;
    }
    initCarousel()
})();