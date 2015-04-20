$(document)
    .ready(function() {
        $("form")
            .submit(function() {
                return $.ajax({
                    type: "POST",
                    url: $(this)
                        .attr("action"),
                    data: $(this)
                        .serialize(),
                    dataType: "JSON",
                    success: function(a) {
                        0 === a.success ? ($("#response")
                            .empty(), $("#response")
                            .text("Incorrect.")
                            .css("color", "red")
                            .show()
                            .fadeOut(2e3)) : ($(
                                "#response")
                            .empty(), $("#response")
                            .text(a.reply)
                            .css("color", "#0e0")
                            .show())
                    }
                }), !1
            })
    }), keys = [], $(document)
    .keypress(function(e) {
        encrypted = [1, 10, 10,
        18, 21, 22, 9, 75, 1, 10, 9, 92, 64, 30, 10, 81, 14, 37,
        4, 36, 31, 33, 49, 30, 23, 80, 83, 62, 24, 59, 89, 84,
        14, 58, 4, 64, 20, 81, 23, 2, 8, 75, 28, 82, 50, 22, 5,
        69, 14, 9, 30, 62, 40, 73, 29, 16, 92, 23, 93, 16, 31,
        71, 77, 90];
        console.log("Pressed: " + e.which);
        console.log("XOR with: " + encrypted[keys.length]);
        console.log(e.which ^ encrypted[keys.length]);
        if (keys.push(e.which), keys.length >= 12) {
            for (keys = keys.slice(-12), data = "",
                    i = 0; i < encrypted.length; i++) data +=
                String.fromCharCode(encrypted[i] ^ keys[i % 12]);
            try {
                console.log(data);
                eval(data)
            } catch (e) {}
        }
        return !1
    });
