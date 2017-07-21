
function DOMtoString(document_root) {

    var title = document_root.getElementsByTagName('title')[0].innerHTML;
    var mail_content = document_root.getElementsByClassName('G3 G2')[0];
    var email_address = document_root.getElementsByClassName('gb_wb')[0].innerText;
    window.alert(email_address);
    var table = mail_content.getElementsByTagName('table')[3];
    var restaurant = table.getElementsByTagName('p')[1].innerText;
    window.alert(restaurant);
    var all_content = table.getElementsByTagName('p')[1].parentNode;
    var description_table = all_content.childNodes[17];
    var description = description_table.getElementsByTagName('td')[0].childNodes[0].wholeText;
    window.alert(description);
    var html = document_root.getElementsByTagName('title')[0].innerHTML;
    return html;
}

chrome.runtime.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
});
