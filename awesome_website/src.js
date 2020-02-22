options = {
            indicators: true
          };
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.carousel');
  var instances = M.Carousel.init(elems, options);
  let switch_image = () => {
    instances[0].next()
  }
  setInterval(switch_image,5000);
});
  document.getElementById("fab1").addEventListener("click", function(){
  M.toast(
    {
      html: "I hate frontend its a pain",
      activationPercent:0.2,
      classes:'myToast rounded'
    });
});

