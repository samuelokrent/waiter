function claim(id) {
  api.claim(id, function(data) {
    if(data.claimed) {
      alert("Claimed successfully: " + data.name + "'s order of " +
      data.description + " from " + data.restaurant + "!");
    } else {
      alert("Someone else has claimed this order already.");
    }
    $("#entry-"+id).remove();
  });
}

function headerRow() {
  return $("<thead/>").html(
            "<th>Restaurant</th>" +
            "<th>Food</th>" +
            "<th>Action</th>"
         );
}

function claimButton(id) {
  return $("<button/>").click(function() {
            claim(id);
         }).html("Claim").addClass("btn").addClass("btn-info");
}

function tableEntry(order) {
  return $("<tr/>").attr("id", "entry-"+order.id)
          .append($("<td/>").html(order.restaurant))
          .append($("<td/>").html(order.description))
          .append($("<td/>").append(claimButton(order.id)));
}

function displayOrders(orders) {
  console.log("displayOrders");
  console.log(orders);
  $table = $("#order_table_body");
  $table.empty();
  for(i = 0; i < orders.length; i++) {
    console.log(orders[i]);
    $table.append(tableEntry(orders[i]));
  }
}

function refreshOrders() {
  api.getOrders(displayOrders);
}

$(document).ready(function() {
  refreshOrders();
  setInterval(refreshOrders, 5000);
});
