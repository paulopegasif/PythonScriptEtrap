#!/bin/bash
# configure.sh -- Script de configuração & packaging do PythonEtrap
# IFSul Passo Fundo (c) MIT
# updated: 2023-03-15

usage() {
    echo "Usage: $(basename $0) [ -p | --package ]
                                [ -r | --run CONFIG_MODULE ]
                                [ -l | --list ]
                                [ -h | --help ] [ -v | --verbose ]"
    exit 2
}

help_panel() {
    echo "Help Panel:
            -p/--package        => Constroi o pacote do PythonEtrap
            -r/--run [MOD]      => Roda o módulo de configuração especificado
            -l/--list           => Lista todos os módulos de configuração
            -h/--help           => Mostra esse painel de ajuda
            -v/--verbose        => Modo verbose"
    exit 0
}

BASEDIR=$(dirname $0)
SYSTEM_ARCH=$(uname -m)

CONFIG_MODULES=(
    mambaforge
    mambaforge_env
    opencv
)

PACKAGE=unset
DEFINE=unset
SET=unset
VERBOSE=unset

# Faz o empacotamento de todo o projeto PythonEtrap
make_etrap_pkg() {
    python3 -m pip install --upgrade build
    cd $BASEDIR/PythonEtrap
    python3 -m build
    ls -l ./dist/
}

# Realiza a listagem de todos os módulos de configuração do script
modules_dump() {
    echo "[Config Modules] => {"
    for mod in CONFIG_MODULES; do
        echo -e "\t$mod"
    done
    echo "}"
}

# Roda um módulo de configuração
# @1 string module
run_config_module() {
    case "$1" in
        mambaforge)
            install_mamba
            break;;
        opencv)
            install_opencv
            break;;
        mambaforge_env)
            make_mamba_env
            break;;
    esac
}

#-----------------------------------#
# Módulos de configuração (funções) #
#-----------------------------------#

# Realiza o download e a execução do script de instalação do mambaforge
install_mamba() {
    wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
    bash Mambaforge-$(uname)-$(uname -m).sh
}

# Cria e ativa o ambiente do mambaforge para a utilização do etrap
make_mamba_env() {      # NAO TESTADO
    cd ~
    conda create --name venv_script_etrap_python3.10 python=3.10
    conda activate venv_script_etrap_python3.10
    pip install picamera
}

install_opencv() {
    # ram check
    local tram=$(grep MemTotal /proc/meminfo | awk '{print $2}')
    tram=$(expr $tram / 1024 / 1024)
    if [ $tram > 6.5 ];then
        wget -O - https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-64-bits/raw/main/OpenCV-4-5-5.sh | bash
        sudo dphys-swapfile swapoff
        sudo dphys-swapfile uninstall
    fi
}

#--------------------------------#
# Argumentos de linha de comando #
#--------------------------------#
PARSED_ARGS=$(getopt -a -n configure -o plvh:r: --long package,list,verbose,help:,run: -- "$@")
VALID_ARGS=$?

if [ "$VALID_ARGS" != "0" ]; then
    usage
fi

eval set -- "$PARSED_ARGS"
while :
do
    case "$1" in
        -p | --package) 
            make_etrap_pkg
            break
            ;;
        -r | --run)
            run_config_module $2
            shift 2
            ;;
        -l | --list)
            modules_dump
            break
            ;;
        -h | --help)
            help_panel
            ;;
        -v | --verbose)
            VERBOSE=1
            shift
            ;;
        --)
            shift
            break
            ;;
        # Erro report
        *) 
            echo "Unexpected commandline option: $1"
            usage
            ;;
    esac
done
