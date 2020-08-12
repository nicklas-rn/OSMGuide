const menuBtn = document.querySelector('.menu-btn');
const pagelinks = document.getElementById('pagelinks');
const navBar = document.getElementById('navbar')
let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.height = "34%";
    pagelinks.style.display = "block";
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.height = "6%";
  }
});


// make words which have //...// around them bold
boldText()

function boldText(){
    var x, i
    // only execute when desired item exists
    if (document.getElementsByClassName("content")){
      var strings = document.getElementsByClassName("content");
      for (x = 0; x < strings.length; x++){
        var string = strings[x].innerHTML;
        var splitstring = string.split("//");
        document.getElementsByClassName("content")[x].innerHTML = splitstring[0];
        for (i = 1; i < splitstring.length; i++) {
           // document.getElementById("beginners_guide_content").innerHTML += splitstring[i];
            if (i % 2 == 0){
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i];
            }
            else {
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i].bold();
          }
        }    
    }
  }
}


//turn words with --...@link@-- around them into a link that leads to the link between @...@
linkText()

function linkText(){
    var x, i
    // only execute when desired item exists
    if (document.getElementsByClassName("content")){
      var strings = document.getElementsByClassName("content");
      for (x = 0; x < strings.length; x++){
        var string = strings[x].innerHTML;
        var splitstring = string.split("--");
        document.getElementsByClassName("content")[x].innerHTML = splitstring[0];
        for (i = 1; i < splitstring.length; i++) {
           // document.getElementById("beginners_guide_content").innerHTML += splitstring[i];
            if (i % 2 == 0){
                document.getElementsByClassName("content")[x].innerHTML += splitstring[i];
            }
            else {
                var processed_string = splitstring[i].split("@");
                document.getElementsByClassName("content")[x].innerHTML += processed_string[0].link(processed_string[1]);
          }
        }    
    }
  }
}


