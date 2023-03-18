document.addEventListener("DOMContentLoaded", () => {
    let total = 0
    $(".subtotales").each(function(){
        total += Number($(this).text());
    });
    $("#total").text(total + " Gs")

    fetch('https://dolar.melizeche.com/api/1.0/')
        .then(response => response.json())
        .then(json =>  $("#amount").val(total/((json.dolarpy.cambioschaco.venta+json.dolarpy.cambioschaco.compra)/2))
        .catch(err => console.log('Solicitud fallida', err))
            )

    //$("#amount").val(total/7183)
    // var myHeaders = new Headers();
    // myHeaders.append("apikey", "VuyHKMdNT4YKzpNMI1YJondBp989w3fU");
    
    // var requestOptions = {
    //   method: 'GET',
    //   redirect: 'follow',
    //   headers: myHeaders
    // };
    
    // fetch("https://api.apilayer.com/exchangerates_data/convert?to=USD&from=PYG&amount="+total, requestOptions)
    //   .then(response => response.json())
    //   .then(result => {
    //     $("#amount").val(result["result"])
    //   })
    //   .catch(error => console.log('error', error));
});


function desaparecerboton(){
    var boxMensaje = document.querySelector(".mensaje_flash");
    boxMensaje.remove()
}