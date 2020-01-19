"use strict";
$( document ).ready(function() {
    var currentDiv = document.getElementById("g-container");
    for (var i = 0; i < 5; i++) {
        currentDiv.appendChild(get_el());
    }
    var newDiv = document.createElement("div");
    document.body.insertBefore(newDiv, currentDiv);
    var newP = document.createElement("p");
    document.body.replaceChild(newP, newDiv);
    var container = newP.parentNode;
    console.log(container);
    document.body.removeChild(newP);

    var links = document.links;
    console.log("number of images: " + document.images.length);
    console.log("number of links: " + document.links.length);
    console.log("link 1: " + links.item(0));
    console.log("link 2: " + links.item(1));
    console.log("link 3: " + links.namedItem('garbage'));
    console.log("number of forms: " + document.forms.length);
    console.log("number of anchors: " + document.anchors.length);

    $("body").mousemove(function(e) {
        var a_font = 1.0;
        var a_bg = 1.0;
        if (e.pageX < 1000) {
            a_font = e.pageX / 1000;
        }
        if (e.pageY < 1000) {
            a_bg = e.pageY / 1000;
        }
        $(".text-line").css({
            "background-color": "rgba(0, 0, 0, " + a_bg + ")",
            "color": "rgba(0, 0, 0, " + a_font + ")"
        });
    })

});

function get_el() {
    var newDiv = document.createElement("div");
    newDiv.setAttribute("class", "text-line");
    $(newDiv).mouseover(function(e) {
        if (e.altKey && e.shiftKey && e.ctrlKey) {
            $(newDiv).html(e.screenX.toString() + e.screenY.toString());
        } else {
            $(newDiv).html("Don't You Know?");
        }
    });
    $(newDiv).mouseout(function() {
        $(newDiv).html("Who Are You?");
    });
    $(newDiv).mousedown(function() {
        $(newDiv).html("Are You Anyone?");
    });
    var newContent = document.createTextNode("Who Are You?");
    newDiv.appendChild(newContent);
    return newDiv;
}

function change_font() {
    var font = document.getElementById("font-select").value;
    $(".text-line").css("font-family", font);
}
