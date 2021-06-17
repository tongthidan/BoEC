var slideIndex = 0;
function plusSlides(n) {
   
  showSlides_hand( slideIndex+=n);
}
showSlides();
function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slide-item");
   for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }   
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block"; 
setTimeout(showSlides, 3000);
}
function showSlides_hand(n){
    var i;
  var slides = document.getElementsByClassName("slide-item");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
   for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }   
  // slides[slideIndex-1].style.display = "block";
}
var slide_product=1;
ShowProduct(slide_product);
function nextProduct(n) {
   
  ShowProduct(slide_product+=n);
}
function ShowProduct(n) {
  var x;
  var slides = document.getElementsByClassName("slide_product_item");
  console.log(slides.length);
  if (n > slides.length) {slide_product = 1}
  if (n < 1) {slide_product = slides.length}
   for (x = 0; x < slides.length; x++) {
      slides[x].style.display = "none";
  }   
  slides[slide_product-1].style.display = "block"; 
  
}

function tabs(x) {
  document.getElementById("featured_product").style.display="none";
  document.getElementById("new_product").style.display="none";
  document.getElementById("on_sale").style.display="none";

  if(x.value==="featured_product"||x.value==="new_product"||x.value==="on_sale"){
    document.getElementById(x.value).style.display="block";
    document.querySelectorAll(".product__list--item .active")[0].classList.remove("active");
    x.classList.add("active");
  }
}

