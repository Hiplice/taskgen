function addHandler(object, event, handler, useCapture) {
    if (object.addEventListener) {
        object.addEventListener(event, handler, useCapture ? useCapture : false);
    } else if (object.attachEvent) {
        object.attachEvent('on' + event, handler);
    }
}
function tabInsertInit(obj) {
    var _obj = obj;
    if (window.opera) addHandler(obj, "keypress", function(evt) {tabInsert(evt, _obj);});
    else addHandler(obj, "keydown", function(evt) {tabInsert(evt, _obj);});
}
function tabInsert(evt, obj) {
    evt = evt || window.event;
    var key = evt.keyCode || evt.which;
    if (key == 9) {
        if (obj.nodeName) if (obj.nodeName.toLowerCase() == "textarea") obj.focus();
        if(document.selection) {
            var iesel = document.selection.createRange().duplicate();
            iesel.text = "\t";
        } else {
            var start = obj.selectionStart;
            var end = obj.selectionEnd;
            var left = obj.value.substring(0, start);
            var right = obj.value.substring(end);
            var scroll = obj.scrollTop;
            obj.value = left + "\t" + right;
            obj.selectionStart = obj.selectionEnd = start + 1;
            obj.scrollTop = scroll;
            obj.focus();
        }
        if(evt.preventDefault) evt.preventDefault();
        evt.returnValue = false;
        return false;
    }
}