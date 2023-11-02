$(document).ready(function () {
  $('INPUT#btn_translate, INPUT#language_code').on('click keyup', function (event) {
    if (event.type === 'click' || event.keyCode === 13) {
      const languageCode = $('INPUT#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
