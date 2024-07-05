#!/bin/sh
pyversion="3.11.5"
case "$OSTYPE" in
  linux*)   installlinux;;
  msys*)    installwin;;
  cygwin*)  echo "ALSO WINDOWS" ;;
  *)        echo "unknown: $OSTYPE" ;;
esac

function installwin() {
    if [ $? -eq 0 ]; then
        echo "Versão do Python encontrada: $VERSAO_PYTHON"
        python3 -m venv env 
        . env/bin/activate
        python3 -m pip install -r requirements.txt
        python3 manage.py migrate
        python3 manage.py runserver 8000

    elif [ $? -eq 2 ]; then
        echo "Versão do Python encontrada: $VERSAO_PYTHON"
        echo "Versão Invalida do python"
        echo "Instale o python >=$pyversion e inicie novamente o script"

    else
        echo "Versão do Python encontrada: $VERSAO_PYTHON"
        echo "Não foi possível encontrar uma versão do Python instalada."
        echo "Instale-o e inicie novamente o script"
    fi


}

function installlinux(){
    validade=$(verify_version)
    if [ $? -eq 2 ]; then
        python3 -m venv env 
        . env/bin/activate
        python3 -m pip install -r requirements.txt
        python3 manage.py migrate
        python3 manage.py runserver 8000
    else
        break
}



funcion verify_version() {
    VERSAO_PYTHON=$(identificar_versao_python)
    if [ $? -eq 0 ]; then
        echo "Versão do Python encontrada: $VERSAO_PYTHON"
        if [$VERSAO_PYTHON >= $pyversion]; then
            return 2
        elif
            erro '2'
    fi
        
    if [ $? -eq 2 ]; then
        erro '2'
        return 2
    fi
    
    else
        erro '1'
        return 1
    fi
}
function identificar_versao_python() {
    # Tenta identificar a versão do Python 3
    PYTHON_VERSION=$(python3 --version 2>&1)
    if [ $? -eq 0 ]; then
        echo "$PYTHON_VERSION"
        return 0
    fi
    
    # Tenta identificar a versão do Python 2
    PYTHON_VERSION=$(python --version 2>&1)
    if [ $? -eq 0 ]; then
        echo "$PYTHON_VERSION"
        return 2
    fi
    
    # Se nenhum Python foi encontrado
    echo "Python não está instalado."
    return 1
}

funcion erro(){
    local mensagem="$1"
    if [$? -eq 2]; then        
        echo "Versão do Python encontrada: $VERSAO_PYTHON"
        echo "Versão Invalida do python"
        echo "Instale o python >=$pyversion e inicie novamente o script"
    
    if [$? -eq 1]; then
        echo "Não foi possível encontrar uma versão do Python instalada."
        echo "Instale-o e inicie novamente o script"



}