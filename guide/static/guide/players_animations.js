// show tactics that fit search
function searchPlayers(event) {
  // Declare variables
  var input, filter, section, div, a, i, txtValue, search_description;

  search_description = document.getElementById('search_players_description');
  search_description.style.display = "none";

  input = document.getElementById('search_players');
  filter = input.value.toUpperCase().replace(/\s/g,'');  //!!CHECK WHETHER REPLACE PART IS VALID!!
  article = document.getElementById('players');
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

  player_names = document.getElementsByClassName('player_name')

  for (i = 0; i < player_names.length; i++) {
    player_name = player_names[i];
    txtValue = player_name.textContent.replace(/\s/g,'') || player_name.innerText.replace(/\s/g,'');
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
        if (event.keyCode==13){
            player_name.scrollIntoView({behavior: 'smooth'});
        }
    }
  }
}
