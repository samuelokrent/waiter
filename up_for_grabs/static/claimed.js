window.orders = [];

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

function findNewOrder(l1, l2) {
  if(l2.length > l1.length) {
    return l2[l2.length - 1];
  } else {
    for(i = 0; i < l2.length; i++) {
      order = l2[i];
      var found = false;
      for(j = 0; j < l1.length; j++) {
        if(l1[j].id = order.id) {
          found = true;
          break;
        }
      }
      if(!found) {
        // This order is in l2 but not l1
        return order;
      }
    }
    // Lists are the same
    return false;
  }
}

function processOrders(orders) {
  var newOrder = findNewOrder(window.orders, orders);
  if(newOrder) {
    notify(newOrder);
  }
  window.orders = orders;
  console.log("processOrders");
  console.log(orders);
  $table = $("#order_table_body");
  $table.empty();
  for(i = 0; i < orders.length; i++) {
    console.log(orders[i]);
    $table.append(tableEntry(orders[i]));
  }
}

function refreshOrders() {
  api.getOrders(processOrders);
}

function notify(order) {
  if (Notification.permission !== "granted")
    Notification.requestPermission();
  else {
    var notification = new Notification('Up for grabs!', {
      icon: 'http://localhost:8000/static/logo.png',
      body: "Claim it now: " + order.description
    });

  }

}

$(document).ready(function() {
  refreshOrders();
  setInterval(refreshOrders, 5000);

  if (!Notification) {
    alert('Desktop notifications not available in your browser. Try Chromium.'); 
    return;
  }

  if (Notification.permission !== "granted")
    Notification.requestPermission();
});
