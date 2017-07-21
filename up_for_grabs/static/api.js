api = {};

api.getOrders = function(cb) {
  $.get("/orders", cb);
}

api.claim = function(id, cb) {
  $.get("/claim/" + id, cb); 
}
