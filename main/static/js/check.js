/*$(document).ready(function() {
// Set the unload message whenever any input element get changed.
    $(':input').change(function() {
        setConfirmUnload(true);
    });
// Turn off the unload message whenever a form get submitted properly.
    $('form').submit(function() {
        setConfirmUnload(false);
    });
});
function setConfirmUnload(on) {
    var message = "Все несохраненные данные будут потеряны. Продолжить?";
    window.onbeforeunload = (on) ? function() { return message; } : null;
}
*/
