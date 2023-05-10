
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('marcarTodo').addEventListener('click', function(e) {
        e.preventDefault();
        //seleccionarTodo();
        checkAll();
    });
    document.getElementById('desmarcarTodo').addEventListener('click', function(e) {
        e.preventDefault();
        //desmarcarTodo();
        uncheckAll();
    });
});

function seleccionarTodo() {
    for (let i=0; i < document.f1.elements.length; i++) {
        if(document.f1.elements[i].type === "checkbox") {
            document.f1.elements[i].checked = true;
        }
    }
}

function desmarcarTodo() {
    for (let i=0; i<document.f1.elements.length; i++) {
        if(document.f1.elements[i].type == "checkbox") {
            document.f1.elements[i].checked = false
        }
    }
}

function checkAll() {
    document.querySelectorAll('#data input[type=checkbox]').forEach(function(checkElement) {
        checkElement.checked = true;
    });
}

function uncheckAll() {
    document.querySelectorAll('#data input[type=checkbox]').forEach(function(checkElement) {
        checkElement.checked = false;
    });
}
