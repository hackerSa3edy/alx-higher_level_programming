$('document').ready(function () {
  $('input#btn_translate').click(translate);
  $('input#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(url + $.param({ lang: $('input#language_code').val() }), function (data) {
    $('input#hello').text(data.hello);
  });
}
