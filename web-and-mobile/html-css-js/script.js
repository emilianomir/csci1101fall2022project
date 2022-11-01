window.addEventListener("load", function ()
{
    // Get click element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // Counter Value.
    let counter = 0;

    // Click Button Function.
    let clickButtonFunction = function ()
    {
        // Increment counter.
        counter++;

        // Update counter Value.
        clickCounterElement.innerHTML = counter;
    };

    // Attach button function.
    clickButtonElement.addEventListener("click", clickButtonFunction);

});