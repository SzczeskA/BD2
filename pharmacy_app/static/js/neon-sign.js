letters = [];

async function run(letters) {
    while (true) {
        shuffleArray(letters);
        for (var i = 0; i < letters.length; i++) {
            var color = sprintf("rgba(0, 0, 0, %f)", Math.random().toFixed(1));
            $(letters[i]).css("color", color);
            var sleep_time = 30 + Math.floor(200 * Math.random());
            await sleep(30);
        }
    }
}

$( document ).ready(function() {
    $('.letter').each(function(i, obj) {
        letters.push(obj);
    });
    run(letters);
});
