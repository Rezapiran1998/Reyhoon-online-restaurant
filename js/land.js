// hide scroll to top button
window.onscroll = function () {
  var pageOffset =
    document.documentElement.scrollTop || document.body.scrollTop;
  if (pageOffset >= 500) {
    document.getElementById("button").classList.add("show");
  } else {
    document.getElementById("button").classList.remove("show");
  }
};
