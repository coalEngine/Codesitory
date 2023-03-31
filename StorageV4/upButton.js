const btnScroll = document.querySelector("#btnScroll");
 
 
        btnScroll.addEventListener("click", function () {
 
           window.scrollTo({
               left: 0,
               top: 0,
               behavior: "smooth"
           })
        })
