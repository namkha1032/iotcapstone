function timedCount() {
    var i = sessionStorage.getItem("wors");
    sessionStorage.setItem("wors", i + 1);
    console.log(sessionStorage.getItem("wors"));
    postMessage(sessionStorage.getItem("wors"));
    setTimeout("timedCount()", 500);
}

timedCount();
