const select = document.querySelector("#categoria");
select.addEventListener('change', function(){
    const categoria = select.value;
    getDados(categoria);
});

var item = document.querySelector("#item");

async function getDados(categoria){
    const response = await fetch(`/coab/pedidos/listar/${categoria}`);
    const dados = await response.json();

    console.log(dados); 

    item.innerHTML = '';
    
    // for(const i in dados){
    //     const option = document.createElement('option');
    //     option.value = dados[i]; // Defina o valor da opção como a chave do objeto
    //     option.text = dados[i]; // Defina o texto da opção como o valor do objeto
    //     item.appendChild(option);
    // } 

    dados.map((dado)=>{
        const option = document.createElement('option');
        if(dado[3] == 1){
            option.value = dado[1]; // Defina o valor da opção como a chave do objeto
            option.text = dado[1]; // Defina o texto da opção como o valor do objeto
        }
        item.appendChild(option);
    });
}


function mensagem(msg){
    alert(msg)
}

function abrirPDF(url) {
    const pdfUrl = url;
    window.open(pdfUrl, '_blank');
}
    