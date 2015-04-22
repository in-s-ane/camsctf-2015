var fs = require("fs");
function read(f) {
      return fs.readFileSync(f).toString();
}
function include(f) {
      eval.apply(global, [read(f)]);
}
include("sha256.js")

/*
var array = [
    "\x30\x31\x31\x30\x31\x31\x30\x31\x31\x31\x31\x31\x31\x30\x30\x31\x31\x31\x31\x30\x31\x31\x31\x31\x31\x30\x31\x31\x30\x30\x31\x31\x30\x31\x31\x30\x30\x30\x30\x30\x31\x30\x30\x30\x30\x30\x30\x31\x31\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31\x31",
    "\x6C\x65\x6E\x67\x74\x68", "\x70\x75\x73\x68", "", "\x6A\x6F\x69\x6E",
    "\x73\x6C\x69\x63\x65", "\x63\x68\x61\x72\x43\x6F\x64\x65\x41\x74",
    "\x64", "\x72\x65\x76\x65\x72\x73\x65"
];
*/

var given = [
    "01101101111110011110111110110011011000001000000110000000000000000000000000000000000001111111111111111111111111111111111",
    "length",
    "push",
    "",
    "join",
    "slice",
    "charCodeAt",
    "d",
    "reverse"
]

function checkpass(password) {
    var binary = given[0];
    var tempNumbers = [];
    var hashed = password;//String(CryptoJS.SHA256(password));
    for (i = 0; i < hashed["length"]; i++) {
        if (!isNaN(parseFloat(hashed[i])) && isFinite(hashed[i])) {
            tempNumbers["push"](parseInt(hashed[i]))
        }
    };
    //console.log(tempNumbers);
    if ((tempNumbers[0] << 1 | 1) !== 19) { // tempNumbers[0] = 9
        console.log(1);
        return false
    };
    if (parseInt(tempNumbers["slice"](1, 4)["join"]("")) !== 3 * 111) { // tempNumbers[1,2,3] = 333
        console.log(2);
        return false
    };
    if ((parseInt(tempNumbers["slice"](4, 10)["join"]("")) ^ 272670) !== 0) { // tempNumbers[4,5,6,7,8,9] = 272670
        console.log(3);
        return false
    };
    // hashed[0]["charCodeAt"](0) = 57 since hashed[0] = "9"
    if (parseInt(tempNumbers["slice"](10, 20)["join"]("")) - 1026989203 != hashed[0]["charCodeAt"](0)) { // tempNumbers[10,11,12,13,14,15,16,17,18,19] = 1026989260
        console.log(4);
        return false
    };
    if (parseInt(tempNumbers["slice"](20, 25)["join"]("")) !== 483) { // tempNumbers[20,21,22,23,24] = 00483
        console.log(5);
        return false
    };
    // 7 * 11 * 13 * 47287 * 477497 * 2641907 = tempNumbers[25-end] = 59712329280582550000
    console.log(tempNumbers["slice"](25, tempNumbers["length"])["join"](""));
    console.log(parseInt(tempNumbers["slice"](25, tempNumbers["length"])["join"]("")))
    if (parseInt(tempNumbers["slice"](25, tempNumbers["length"])["join"]("")) / 2641907 !== 7 * 11 * 13 * 47287 * 477497) { 
        console.log(6);
        return false
    };
    if (hashed[2] != "d") {
        console.log(7);
        return false
    };
    var combined_hash = hashed[6] + hashed[13] + hashed[24] +
        hashed[25] + hashed[26] + hashed[32] + hashed[33] +
        hashed[34] + hashed[37] + hashed[39] + hashed[42] +
        hashed[43] + hashed[46] + hashed[54] + hashed[55] +
        hashed[58] + hashed[60]; // 17 chars, probably hex
    var number_binary = [];
    for (i = 0; i < combined_hash["length"]; i++) {
        number_binary["push"](combined_hash[i]["charCodeAt"](0).toString(2))
    };
    var reversed_binary = [];
    for (i = 0; i < number_binary[0]["length"]; i++) { // 0 -> 7
        for (j = 0; j < number_binary["length"]; j++) { // 0 -> 17
            reversed_binary["push"](number_binary[j][i]) // Look at binary_decypt.py for this decryption. It gives the majority of the hex chars (a-f range)
        }
    };
    if (reversed_binary["reverse"]()["join"]("") != binary) {
        console.log(8);
        return false
    };
    return true
}

console.log(
    checkpass("93d332c726701a0269892600ffa04835acc97a1c23fc29c2805825ba50c0f000")
)
