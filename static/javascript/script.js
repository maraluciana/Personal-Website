window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  var navbar = document.getElementById("navbar");
  var navbarImage = document.getElementById("navbarimage");
  var navbarTitle = document.getElementById("navbartitle");

  var collection = document.getElementsByClassName("white-text");
  

  if (window.innerWidth > 960){
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
      navbar.style.backgroundColor = "white";

      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style', 'color:#444 !important');
      }

      navbarTitle.setAttribute('style', 'color:#444 !important');
      navbarTitle.style.fontSize = "20px";

      navbarImage.height = 60;
      navbarImage.width = 70;

    }
    else{
      navbar.style.backgroundColor = "transparent";

      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style', 'color:#f7f7f7 !important');
      }

      navbarTitle.setAttribute('style', 'color:#f7f7f7 !important');
      navbarTitle.style.fontSize = "25px";

      navbarImage.height = 100;
      navbarImage.width = 120;
    }
  }
  else{
    navbar.style.backgroundColor = "white";

    for (let i = 0; i < collection.length; i++) {
      collection[i].setAttribute('style', 'color:#444 !important');
    }

    navbarTitle.setAttribute('style', 'color:#444 !important');
    navbarTitle.style.fontSize = "20px";

    navbarImage.height = 100;
    navbarImage.width = 120;
  }
  
}