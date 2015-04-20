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
        // 98 -> numpad2
        // 101 -> numpad5
        // 100 -> numpad4
        // 97 -> numpad1
        // 122 -> f11
        // 122 -> f11
        // 108 -> numpad enter
        // 101 -> numpad5
        // 109 -> subtract
        // 101 -> numpad5
        // 110 -> decimal point
        // 116 -> f5
        jQuery.event.trigger({ type : 'keypress', which : 98 });
        jQuery.event.trigger({ type : 'keypress', which : 101 });
        jQuery.event.trigger({ type : 'keypress', which : 100 });
        jQuery.event.trigger({ type : 'keypress', which : 97 });
        jQuery.event.trigger({ type : 'keypress', which : 122 });
        jQuery.event.trigger({ type : 'keypress', which : 122 });
        jQuery.event.trigger({ type : 'keypress', which : 108 });
        jQuery.event.trigger({ type : 'keypress', which : 101 });
        jQuery.event.trigger({ type : 'keypress', which : 109 });
        jQuery.event.trigger({ type : 'keypress', which : 101 });
        jQuery.event.trigger({ type : 'keypress', which : 110 });
        jQuery.event.trigger({ type : 'keypress', which : 116 });
        // console.log("{n0t_hArD_ju57_bA51c_j4v4scr1p7_sk1llz_R3qu1r3d}");
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

function simulateKeyPress(character) {
  jQuery.event.trigger({ type : 'keypress', which : character.charCodeAt(0) });
}
