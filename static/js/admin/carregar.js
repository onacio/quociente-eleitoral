function carregar(pedido_id) {
    // Encontrar o pedido correspondente na tabela
    var linhaPedido = document.getElementById('pedido_' + pedido_id);
    
    // Obter os dados do pedido 
    var descricao = linhaPedido.cells[1].innerText;
    var categoria = linhaPedido.cells[2].innerText;
    var quantidade = linhaPedido.cells[3].innerText;
    var unidade_saude = linhaPedido.cells[5].innerText;
    var justificativa = linhaPedido.cells[6].innerText;
    var status = linhaPedido.cells[8].innerText;

    // Preencher os campos da modal com os dados do pedido
    document.getElementById('id_pedido_hidden').value = pedido_id;
    document.getElementById('descricao').value = descricao;
    document.getElementById('categoria').value = categoria;
    document.getElementById('quantidade').value = quantidade;
    document.getElementById('unidade_saude').value = unidade_saude;
    document.getElementById('justificativa').value = justificativa;
    document.getElementById('status').value = status;
    
    // Habilitar os campos que precisam ser editados
    document.getElementById('quantidade_liberada').disabled = false;
}
