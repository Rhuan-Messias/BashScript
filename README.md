# BashScript
----------------------> html_script.sh <----------------------


----------------------> port_knocking-script.sh <----------------------
Explicação passo a passo:
    Primeiramente 
    #!/bin/bash: Esta linha é conhecida como shebang e indica que o script deve ser interpretado e executado pelo Bash. O caminho para o interpretador Bash está especificado após o "shebang".

    ip="ip_desejado": Aqui, é definida a variável ip que armazena o endereço IP ao qual o comando de port knocking será enviado.

    ports="3000 30000 37 13": Nesta linha, a variável ports é definida para armazenar uma lista de portas que serão utilizadas no processo de port knocking. No exemplo, são utilizadas as portas 3000, 30000, 37 e 13.

    green='\033[0,32m', vermelho="\e[91m" e nc='\033[0m': Aqui, estão sendo definidas sequências de escape ANSI para cores no terminal. \033[0,32m representa a cor verde, \e[91m representa a cor vermelha, e \033[0m é usado para redefinir a cor para a padrão (sem cor).

Essas linhas configuram variáveis e constantes que serão utilizadas mais tarde no script, como o endereço IP, as portas e as sequências de escape ANSI para cores. Elas fornecem informações essenciais para a execução do comando de port knocking e para a formatação visual do feedback ao usuário.

    if [ $? -eq 0 ]; then: Este é um bloco condicional que verifica o valor de saída (exit status) do comando executado imediatamente anterior a ele. O $? é uma variável especial que armazena o valor de saída do comando mais recente. O valor 0 indica que o comando foi executado com sucesso.

    echo -e "${green}Port knocking foi bem sucedido${nc}": Se o valor de saída for 0 (indicando que o comando "knock" foi bem-sucedido), este bloco será executado. Ele imprime a mensagem "Port knocking successful" em verde no terminal.

    else: Se o valor de saída não for 0, este bloco será executado.

    echo "${vermelho}Port Knocking falhou.${nc}": Este comando imprime a mensagem "Port Knocking failed." em vermelho no terminal.

Portanto, essa parte do script é um feedback visual para o usuário indicando se o comando "knock" foi bem-sucedido ou falhou ao realizar o port knocking. O código em verde indica sucesso, enquanto o código em vermelho indica falha.
