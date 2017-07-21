function claim(id) {
  api.claim(id, function(data) {
    if(data.claimed) {
      alert("Claimed successfully!");
    } else {
      alert("Someone else has claimed this order already.");
    }
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
         }).html("Claim");
}

function tableEntry(order) {
  return $("<tr/>")
          .append($("<td/>").html(order.name))
          .append($("<td/>").html(order.description))
          .append($("<td/>").append(claimButton(order.pk)));
}

function displayOrders(orders) {
  console.log("displayOrders");
  console.log(orders);
  $table = $("#order_table");
  $table.html("");
  $table.append(headerRow());
  for(i = 0; i < orders.length; i++) {
    $table.append(tableEntry(orders[i]));
  }
}

function refreshOrders() {
  api.getOrders(displayOrders);
}

$(document).ready(function() {
  setInterval(refreshOrders, 5000);
});
