function changeNumber(x) {
    var number = document.getElementById("number_cart").value;
    var z = eval(number);
    var y = eval(z+x);
    if(y<0) y=0;
    document.getElementById("number_cart").value=y;
}
function remove_cart() {
    document.getElementsByClassName("cart__content--card")[0].innerHTML="";
    document.getElementById("cart_empty").style.display="block";
}