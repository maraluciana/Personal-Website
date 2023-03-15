window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  var navbar = document.getElementById("navbar");
  var navbarImage = document.getElementById("navbarimage");
  var navbarTitle = document.getElementById("navbartitle");

  var collection = document.getElementsByClassName("white-text");

  for (let i = 0; i < collection.length; i++) {
    collection[i].addEventListener("mouseover", function(){
      this.style.color = "#1abc9c";
    });

    collection[i].addEventListener("mouseout", function(){
      this.setAttribute('style', 'color:#444 !important');
    });
  }

  
  if (window.innerWidth > 960){
    if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120) {
      navbar.style.backgroundColor = "white";
      

      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style', 'color:#444 !important');

        collection[i].addEventListener("mouseover", function(){
          this.style.color = "#1abc9c";
        });
    
        collection[i].addEventListener("mouseout", function(){
          this.setAttribute('style', 'color:#444 !important');
        });
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

        collection[i].addEventListener("mouseover", function(){
          this.style.color = "#1abc9c";
        });
    
        collection[i].addEventListener("mouseout", function(){
          this.setAttribute('style', 'color:#f7f7f7 !important');
        });
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


      collection[i].addEventListener("mouseover", function(){
        this.style.color = "#1abc9c";
      });
  
      collection[i].addEventListener("mouseout", function(){
        this.setAttribute('style', 'color:#444 !important');
      });
    }

    navbarTitle.setAttribute('style', 'color:#444 !important');
    navbarTitle.style.fontSize = "20px";

    navbarImage.height = 100;
    navbarImage.width = 120;
  }
  
}
