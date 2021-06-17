
function hasClassChild(el, className)
{
    // if (el.classList)
    //     return el.classList.contains(className);
    // return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
    var x= el.querySelectorAll(className);
    if(x.length>0) return true;
    return false;
}
function addClass(el, className)
{
    if (el.length>0)
        el.forEach(element => {
            element.classList.add(className);
        });
    // else {
    //     el.classList.add(className);
    // }
       
}
function removeClass(el, className)
{
    if (el.length>0)
        el.forEach(element => {
            element.classList.remove(className);
        });
}
menu();
sidebarTogger();
function menu() {
    var toggle = document.querySelectorAll(".side_item");
    var removerToggersider=document.querySelectorAll(".sidebar-container");
    var removermargin=document.getElementsByClassName("main_container")[0];
    
   for (var j = 0; j < toggle.length; j++) {
    toggle[j].addEventListener("click", function () {
        removeClass(removerToggersider,"codan1");
        removermargin.classList.remove("marginleft");
        document.getElementsByClassName("main_container")[0].classList.remove("rotate180");
        var x =this.querySelectorAll("ul");
        x[0].classList.toggle("active");
        var y = this.querySelectorAll(".menu-item")[0].querySelectorAll("i");
        y[1].classList.toggle("mystyle");
    });
   }
}
function sidebarTogger() {
    var toggle = document.querySelectorAll(".codan");
    var menuactive = document.querySelectorAll(".side_item>ul");
   for (var j = 0; j < toggle.length; j++) {
    toggle[j].addEventListener("click", function () {
        menuactive.forEach(element => {
            element.classList.remove('active');
            element.parentElement.querySelectorAll("i")[1].classList.remove("mystyle");
        });
        document.getElementsByClassName("sidebar-container")[0].classList.toggle("codan1");
        document.getElementsByClassName("nav__left")[0].classList.toggle("rotate180");
        document.getElementsByClassName("main_container")[0].classList.toggle("marginleft");
    });
   }
}
function profile() {
    document.getElementById("myDropdown").classList.toggle("show");
}