"use strict";

setTimeout(func, 1400);

function func() {
   // alert('selector ready');
   document.getElementById('jstree-tree').addEventListener('dblclick', update_search_bar);
}

function update_search_bar(){
   let result;
   let short_result;
   let str;
   result = document.getElementById('jstree-result').textContent;
   short_result = result.substring(9);
   short_result = short_result.substr(short_result.indexOf('-'));
   short_result = short_result.substring(1);
   document.getElementById('input-box').className = short_result;
   document.getElementById('input-box').value = short_result;
   // document.getElementById('query-bar').textContent = short_result;
   // document.getElementById('query-bar').value = short_result;

   // document.getElementById('decimal').value = result;

   // document.getElementById('sex-distribution').value = short_result;
   // document.getElementById('age-distribution').value = short_result;
   // document.getElementById('language-distribution').value = short_result;

   document.getElementById('jstree-result').value = short_result;
   // alert(document.getElementById('input-box').value
   // alert(document.getElementById('i'))
   // input_box.focus();
   // document.getElementById("input-box").contentWindow.location.reload()
   // reload()
}

// function reload(){
//    alert('in it');
//    let container = document.getElementById("input-box");
//     let content = container.innerHTML;
//     container.innerHTML= content;
//
//    //this line is to watch the result in console , you can remove it later
//     console.log("Refreshed");
// }