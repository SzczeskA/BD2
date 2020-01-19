"use strict";

function get_id_string(x, y) {
    return sprintf("%d,%d", x, y);
}

function get_coords(elem) {
    var box = elem.getBoundingClientRect();

    var body = document.body;
    var docEl = document.documentElement;

    var scrollTop = window.pageYOffset || docEl.scrollTop || body.scrollTop;
    var scrollLeft = window.pageXOffset || docEl.scrollLeft || body.scrollLeft;

    var clientTop = docEl.clientTop || body.clientTop || 0;
    var clientLeft = docEl.clientLeft || body.clientLeft || 0;

    var top = box.top + scrollTop - clientTop;
    var left = box.left + scrollLeft - clientLeft;

    return {top: Math.round(top), left: Math.round(left)};
}

function get_elements() {
    var cells = [];
    var height = 25;
    var width = 25;
    var i;
    var j;
    var elem;
    var coords;
    for (i = 0; i < height; i += 1) {
        for (j = 0; j < width; j += 1) {
            elem = document.getElementById(get_id_string(i, j));
            coords = get_coords(elem);
            cells.push({
                elem: elem,
                alpha: 0.5,
                x: 12 + coords.left,
                y: 12 + coords.top
            });
        }
    }
    shuffleArray(cells);
    return cells;
}

var clicks = [];
var wave = {speed: 40, amplitude: 0.4, freq: 0.15, fade: 1.2}; //speed in px/s
var elems = [];

function distance(elem, ev) {
    //console.log({el: elem, ev: ev});
    return Math.sqrt((elem.x - ev.x) * (elem.x - ev.x) + (elem.y - ev.y) * (elem.y - ev.y));
}

function calculate_alpha_from_one_event(elem, click) {
    var time = Date.now() - click.t;
    var dist = distance(elem, click);
    //console.log({dist: dist, time: time, wxt: wave.speed * time / 1000});
    if (dist < wave.speed * time / 1000) {
        time -= 1000 * dist / wave.speed;
        var phase = time / (1 / wave.freq);
        var alpha = wave.amplitude * Math.sin(phase * Math.PI) / Math.pow(wave.fade, time / 1000);
        //console.log(alpha);
        return alpha;
    }
    return 0.0;
}

function calculate_alpha(elem) {
    var alpha = 0.5;
    var i;
    for (i = (clicks.length > 3) ? clicks.length - 3 : 0; i < clicks.length; i += 1) {
        alpha += calculate_alpha_from_one_event(elem, clicks[i]);
    }
    if (alpha > 1.0) {
        return 1.0;
    } else if (alpha < 0) {
        return 0;
    }
    return alpha;
}
async function run() {
    var i;
    var elem;
    var alpha;
    while (true) {
        for (i = 0; i < elems.length; i += 1) {
            elem = elems[i];
            alpha = calculate_alpha(elem);
            if (Math.abs(alpha - elem.alpha) >= 0.1) {
                elem.elem.style.backgroundColor = sprintf("rgba(0, 0, 0, %s)", alpha.toFixed(2));
                elem.alpha = alpha;
            }
            await sleep(1);
        }
    }
}

function click_event_handler(event) {
    clicks.push({x: event.clientX, y: event.clientY, t: Date.now()});
}

$(document).ready(function() {
    elems = get_elements();
    window.addEventListener("click", click_event_handler);
    run();
});
