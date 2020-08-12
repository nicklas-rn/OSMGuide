// show tactics that fit search
function searchTactics() {
  // Declare variables
  var input, filter, section, div, a, i, txtValue, search_description;
 
  search_description = document.getElementById('search_tactics_description');
  search_description.style.display = "none";

  input = document.getElementById('search_tactics');
  filter = input.value.toUpperCase().replace(/\s/g,'');  //!!CHECK WHETHER REPLACE PART IS VALID!!
  article = document.getElementById('counter_tactics');
  div = article.getElementsByTagName('div');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < div.length; i++) {
    title = div[i].getElementsByTagName("h5")[0];
    txtValue = title.textContent.replace(/\s/g,'') || title.innerText.replace(/\s/g,'');
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      div[i].style.display = "";
    } else {
      div[i].style.display = "none";
    }
  }
}


// show tactic against weaker Opponent
function weakerOpponent(i) {
  var weaker_opponent_nav, stronger_opponent_nav, 
  weaker_opponent_section, stronger_opponent_section;

  weaker_opponent_nav = document.getElementsByClassName('weaker_opponent_nav')[i];
  stronger_opponent_nav = document.getElementsByClassName('stronger_opponent_nav')[i];
  weaker_opponent_section = document.getElementsByClassName('weaker_opponent')[i];
  stronger_opponent_section = document.getElementsByClassName('stronger_opponent')[i];

  weaker_opponent_nav.style.backgroundColor = "d9d9d9";
  stronger_opponent_nav.style.backgroundColor = "white";
  weaker_opponent_section.style.display = "";
  stronger_opponent_section.style.display = "none";
} 

// show tactic against stronger opponent
function strongerOpponent(i) {
  var weaker_opponent_nav, stronger_opponent_nav, 
  weaker_opponent_section, stronger_opponent_section;

  weaker_opponent_nav = document.getElementsByClassName('weaker_opponent_nav')[i];
  stronger_opponent_nav = document.getElementsByClassName('stronger_opponent_nav')[i];
  weaker_opponent_section = document.getElementsByClassName('weaker_opponent')[i];
  stronger_opponent_section = document.getElementsByClassName('stronger_opponent')[i];

  weaker_opponent_nav.style.backgroundColor = "white";
  stronger_opponent_nav.style.backgroundColor = "d9d9d9";
  weaker_opponent_section.style.display = "none";
  stronger_opponent_section.style.display = "";
}


// run function one time so that weaker opponent is pre-set

div = document.getElementsByClassName("weaker_opponent_nav")

for (x = 0; x < div.length; x++) {
  weakerOpponent(x)
}


// go to counter tactics -> set this as default
counterTactics()
function counterTactics() {
  blue_line = document.getElementById('blue_line');
  overall_tactics = document.getElementById('overall_tactics');
  counter_tactics = document.getElementById('counter_tactics');

  blue_line.style.transform = "translateX(0%)";
  overall_tactics.style.display = "none";
  counter_tactics.style.display = "";
}

// go to overall tactics
function overallTactics() {
  blue_line = document.getElementById('blue_line');
  overall_tactics = document.getElementById('overall_tactics');
  counter_tactics = document.getElementById('counter_tactics');

  blue_line.style.transform = "translateX(100%)";
  overall_tactics.style.display = "";
  counter_tactics.style.display = "none";
}



//Link to detail view of tactic
const title = document.getElementsByClassName('counter_tactic_title');
for (i = 0; i < title.length - 1; i++) {
  const innertitle = document.getElementsByClassName('counter_tactic_title')[i].innerHTML.replace(/ /g, "_");
  title[i].addEventListener('click', () => {
     string = "/tactics/" + innertitle;
     window.location.href = string;
  });
}