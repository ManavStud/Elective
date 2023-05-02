const form = document.querySelector("form"),
    nextBtn = form.querySelector(".nextBtn"),
    // backBtn = form.querySelector(".backBtn"),
    allInput = form.querySelectorAll(".first input");


nextBtn.addEventListener("click", () => {
    allInput.forEach(input => {
        if (input.value != "") {
            form.classList.add('secActive');
        } else {
            form.classList.remove('secActive');
        }
    })
})

backBtn.addEventListener("click", () => form.classList.remove('secActive'));

function disableOption(selectedOption) 
        {
            var options = document.getElementsByTagName('option');
            for (var i = 0; i < options.length; i++) 
            {
                if (options[i].value == selectedOption.value && !selectedOption.disabled) 
                {
                options[i].disabled = true;
                } 
                else if (options[i].value != selectedOption.value && selectedOption.disabled) 
                {
                    options[i].disabled = false;
                }
            }
        }

