"use strict";

setInterval(func, 200);

function func() {

    let result;
    let short_result;
   result = document.getElementById('jstree-result').textContent;
   short_result = result.substring(9);
   document.getElementById('input-box').focus();
   document.getElementById('input-box').value = short_result;

}
