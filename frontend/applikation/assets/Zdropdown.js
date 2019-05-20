setTimeout(wholeFunc, 1000);  //this is heavily needed as it will load before the whole baum can be initialized

function wholeFunc() {


    let toggle = document.getElementsByClassName('caret');
    let i;

    for (i = 0; i < toggle.length; i++) {
        // alert('in it');
        toggle[i].addEventListener("click", function () {
            this.parentElement.querySelector('.nested').classList.toggle('active');
            this.classList.toggle('caret-down');
        });
    }
}