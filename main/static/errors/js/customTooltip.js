let elem = $(".how-to-screenshot");

let message;
if (navigator.appVersion.includes("Macintosh")) {
    message = "⌘-ctrl-shift-4";
}
else if (navigator.appVersion.includes("Windows")) {
    message = "Open Snipping Tool --> New";
}
elem.attr("data-tooltip", `To get screenshot into clipboard:\n${message}\n(click for more details)`);