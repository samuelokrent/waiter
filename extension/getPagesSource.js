
function DOMtoString(document_root) {
   
    var title = document_root.getElementsByTagName('title')[0].innerHTML;
    var mail_content = document_root.getElementsByClassName('G3 G2')[0];
    var email_address = document_root.getElementsByClassName('gb_wb')[0].innerText;
    var name = document_root.getElementsByClassName('gb_ub gb_vb')[0].innerText;
    //window.alert(email_address);
    var table = mail_content.getElementsByTagName('table')[3];
    var restaurant = table.getElementsByTagName('p')[1].innerText;
    //window.alert(restaurant);
    var all_content = table.getElementsByTagName('p')[1].parentNode;
    var description_table = all_content.childNodes[17];
    var description = description_table.getElementsByTagName('td')[0].childNodes[0].wholeText;
    //window.alert(description);
    var string = "";
    var office;
    if(restaurant.includes('San Francisco')) {
      office = "San Francisco";
    }  else {
      office = "Palo Alto";
    }
    //var office = "Palo Alto";
    var confirm_message = string.concat("Hey ",name,"\nAre you sure you want to donate ",description," from ", restaurant, "?");
    if(window.confirm(confirm_message) == true)  {
      $.post("https://claimed.localtunnel.me/create", JSON.stringify({'office': office, 'name':name, 'description':description,'restaurant':restaurant,'email':email_address}) )
      .fail(function(response) { console.log(response); });
      
    }
    var html = document_root.getElementsByTagName('title')[0].innerHTML;
    return html;
}

chrome.runtime.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
});
