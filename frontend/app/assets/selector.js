"use strict";

setTimeout(func, 1400);

function func() {
   document.getElementById('jstree-tree').addEventListener('dblclick', update_search_bar);
}

function update_search_bar() {
   let result;
   let short_result;
   let str;
   result = document.getElementById('jstree-result').textContent;
   short_result = result.substring(9);
   short_result = short_result.substr(short_result.indexOf('-'));
   short_result = short_result.substring(1);
   document.getElementById('input-box').className = short_result;
   document.getElementById('input-box').value = short_result;
   document.getElementById('jstree-result').value = short_result;
}