document.addEventListener("DOMContentLoaded", function(){
    var nav_links = document.querySelectorAll("nav a");

    nav_links.forEach(function(link){
        link.addEventListener("mouseover", function(){
            link.style.backgroundColor = "yellow"; 
        });
        
        link.addEventListener("mouseout", function(){
            link.style.backgroundColor = "black"; 
        });
    });

    const showAlertButton = document.getElementById('show-alert');

    if (showAlertButton){
        showAlertButton.addEventListener("click", function(){
            alert("Tengo sueño!!");
        });
    }
});
