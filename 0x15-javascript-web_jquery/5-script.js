$('DIV#add_item').click(function () {
  const newItem = $('<li>Item</li>');
  $('UL.my_list').append(newItem);
});
