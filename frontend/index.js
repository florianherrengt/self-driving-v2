var $element = $('input[type="range"]');

$element
  .rangeslider({
    polyfill: false
  })
  .on('input', function() {
    // updateOutput($output[0], this.value);
  });