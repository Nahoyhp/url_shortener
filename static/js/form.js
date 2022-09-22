$(document).ready(function () {
  $('form').on('submit', function (event) {
    $.ajax({
      data: {
        input: $('#input_url').val()
      },
      type: 'POST',
      url: '/'
    })
      .done(function (data) {
        $('#successAlert').text(
          data.input + " is shorten to " + data.shorten
        ).show();
      });
    event.preventDefault();
  });
});