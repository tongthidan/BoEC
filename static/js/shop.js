var acc = document.getElementsByClassName("accordion");
var i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}
// end category
var lowerSlider = document.querySelector('#lower');
var  upperSlider = document.querySelector('#upper');

document.querySelector('#two').value=upperSlider.value;
document.querySelector('#one').value=lowerSlider.value;

var  lowerVal = parseInt(lowerSlider.value);
var upperVal = parseInt(upperSlider.value);

upperSlider.oninput = function () {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);

    if (upperVal < lowerVal + 4) {
        lowerSlider.value = upperVal - 4;
        if (lowerVal == lowerSlider.min) {
        upperSlider.value = 4;
        }
    }
    document.querySelector('#two').value=this.value
};

lowerSlider.oninput = function () {
    lowerVal = parseInt(lowerSlider.value);
    upperVal = parseInt(upperSlider.value);
    if (lowerVal > upperVal - 4) {
        upperSlider.value = lowerVal + 4;
        if (upperVal == upperSlider.max) {
            lowerSlider.value = parseInt(upperSlider.max) - 4;
        }
    }
    document.querySelector('#one').value=this.value
}; 
// end slider price
window.addEventListener("load", function () {
  const dropdownItems = document.querySelectorAll(
  "#lightdropdown .dropdown-item"
  );
  const dropdownSelect = document.querySelector(
  "#lightdropdown .dropdown-select"
  );
  const dropdownSelectText = document.querySelector(
  "#lightdropdown .dropdown-selected"
  );
  const dropdownList = document.querySelector(
  "#lightdropdown .dropdown-list"
  );
  const dropdownCaret = document.querySelector(
  "#lightdropdown .dropdown-caret"
  );
  dropdownSelect.addEventListener("click", function () {
  dropdownList.classList.toggle("show");
  dropdownCaret.classList.toggle("fa-angle-up");
  });
  function handleSelectDropdown(e) {
  const { value } = e.target.dataset;
  dropdownSelectText.textContent = value;
  dropdownList.classList.remove("show");
  dropdownCaret.classList.remove("fa-angle-up");
  }
  dropdownItems.forEach((el) =>
  el.addEventListener("click", handleSelectDropdown)
  );
  });
  // end sortBy