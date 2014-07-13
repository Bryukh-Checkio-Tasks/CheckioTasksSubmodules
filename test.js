function inc(x) {
    return function (y) {
        return x + y
    }
}

var inc1 = inc(1);
console.log(inc1(2)); // 3

function with_counter() {
    var i = 0;
    return function (x) {
        i++;
        return x + i;
    }
}

var c = with_counter(3);
console.log(c(0)); // 3
console.log(c(0)); // 3