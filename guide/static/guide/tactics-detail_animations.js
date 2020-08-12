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