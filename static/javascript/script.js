window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  var navbar = document.getElementById("navbar");
  var navbarImage = document.getElementById("navbarimage");
  var collection = document.getElementsByClassName("white-text");

  if (window.innerWidth > 960){
    if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120) {
      navbar.style.backgroundColor = "white";

      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style', 'color:black !important');
      }

      navbarImage.height = 60;
      navbarImage.width = 70;

    }
    else{
      navbar.style.backgroundColor = "transparent";

      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style', 'color:white !important');
      }

      navbarImage.height = 100;
      navbarImage.width = 120;
    }
  }
  else{
    navbar.style.backgroundColor = "white";

    for (let i = 0; i < collection.length; i++) {
      collection[i].setAttribute('style', 'color:black !important');
    }

    navbarImage.height = 100;
    navbarImage.width = 120;
  }
  
}