$(".phone_menu").click(function () {
    $(".menu2").slideToggle(800);
})

const swiper = new Swiper('.swiper-container', {
  // Optional parameters
  // cssMode: true,
  spaceBetween: 100,
  loop: true,
  effect: 'fade',
  speed: 2000,
  autoplay: {
      delay: 8000,
      disableOnInteraction: false,
  },
  direction: 'horizontal',

  // If we need pagination

  // Navigation arrows
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
      el: '.swiper-scrollbar',
  },
});


    




// $(".hamburger__button").click(function () {
//   $(this).css("margin-bottom", "100px");
// })