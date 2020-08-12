// show tactics that fit search
function searchTips(event) {
  // Declare variables
  var input, filter, section, div, a, i, txtValue, search_description;

  search_description = document.getElementById('search_tips_description');
  search_description.style.display = "none";

  input = document.getElementById('search_tips');
  filter = input.value.toUpperCase().replace(/\s/g,'');  //!!CHECK WHETHER REPLACE PART IS VALID!!
  article = document.getElementById('tips');
  div = article.getElementsByTagName('div');

  // Loop through all list items, and hide those wh o don't match the search query
  for (i = 0; i < div.length; i++) {
    keywords = div[i].getElementsByClassName("keywords")[0];
    txtValue = keywords.textContent.replace(/\s/g,'') || keywords.innerText.replace(/\s/g,'');
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      div[i].style.display = "";
    } else {
      div[i].style.display = "none";
    }
  }

  tip_names = document.getElementsByClassName('tip_name')

  for (i = 0; i < tip_names.length; i++) {
    tip_name = tip_names[i];
    txtValue = tip_name.textContent.replace(/\s/g,'') || tip_name.innerText.replace(/\s/g,'');
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
        if (event.keyCode==13){
            tip_name.scrollIntoView({behavior: 'smooth'});
        }
    }
  }
}