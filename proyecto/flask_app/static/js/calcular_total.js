document.addEventListener("DOMContentLoaded", () => {
    let total = 0
    $(".subtotales").each(function(){
        total += Number($(this).text());
    });
    $("#total").text(total + " Gs")
    $("#amount").val(total/7163)
});


function desaparecerboton(){
    var boxMensaje = document.querySelector(".mensaje_flash");
    boxMensaje.remove()
}