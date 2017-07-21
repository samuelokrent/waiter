api = {};

api.getOrders = function(cb) {
  $.get("/orders", cb);
}

api.claim = function(id, cb) {
  $.post("/claim/" + id, {
    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').attr('value')
  }, cb); 
}