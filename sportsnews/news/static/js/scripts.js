$(document).ready(function() {
    $('#form-login').submit(function(event) {
        event.preventDefault(); // Previne o comportamento padrão do formulário (recarregar a página)
        
        var username = $('#username').val(); // Obtém o valor do campo username
        var password = $('#password').val(); // Obtém o valor do campo password

        // Verifica se o username e a senha são iguais a 'admin'
        if (username === 'admin' && password === 'admin') {
            // Se as credenciais estiverem corretas
            alert('Login bem-sucedido!');
            $('#loginModal').modal('hide');  // Fecha o modal de login
        } else {
            // Se as credenciais estiverem incorretas
            $('#login-error').show();  // Exibe a mensagem de erro
        }
    });
});
