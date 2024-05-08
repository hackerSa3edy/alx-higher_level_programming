$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    dataType: 'json',
    success: function (response) {
      $('div#hello').text(response.hello);
      // console.log(response);
    }
  });
});
