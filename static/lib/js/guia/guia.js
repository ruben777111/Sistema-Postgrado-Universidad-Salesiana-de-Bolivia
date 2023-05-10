function listarGuias(){
    $.ajax({
        url:"/guia/listar_guia/",
        type: "get",
        dataType: "json",
        success: function(response){
            console.log(response);
        }


    });
}
var $ = jQuery.noConflict();
$(document).ready(function(){
    listarGuias();
});