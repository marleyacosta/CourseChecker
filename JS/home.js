var term = "0";
var major = "0";

$('#home_arrow').click(function() {
  term = $('#semester').find(":selected").val();
  major = $('#college_major').find(":selected").val();

  if (term == "0") {
    window.alert("ERROR: Must select a semester!");
    return;
  }
  if (major == "0") {
    window.alert("ERROR: Must select a major!");
    return;
  }

  if (major == "CS") {
    var element = document.getElementById("cs_flow");
    if (element.style.display == "none")
      element.style.display = "block";
  }

  $('html, body').animate({
    scrollTop: $("#cs_flow").offset().top
  }, 1500);
});
