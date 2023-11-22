function buscarResultados() {
    $.get("https://script.google.com/macros/s/SEU_ID_DA_SCRIPT_WEB/exec", function(data) {
        exibirResultados(data);
    });
}

function exibirResultados(resultados) {
    var divResultados = document.getElementById("resultados");
    divResultados.innerHTML = "<h2>Participante - Sorteado</h2>";

    resultados.forEach(function(resultado) {
        var linha = document.createElement("p");
        linha.textContent = resultado.Participante + " - " + resultado.Sorteado;
        divResultados.appendChild(linha);
    });
}