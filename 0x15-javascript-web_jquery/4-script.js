$(document).ready(function () {
  $('div#toggle_header').on('click', function () {
    $('header').toggleClass('green');
    $('header').toggleClass('red');
  });
});
