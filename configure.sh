#!/bin/bash
# configure.sh -- Script de configuração & packaging do PythonEtrap
# IFSul Passo Fundo (c) MIT
# updated: 2023-03-15

usage() {
    echo "Usage: $(basename $0) [ -p | --package ] 
                                [ -d | --define VARIABLE ]
                                [ -r | --run CONFIG_MODULE ]
                                [ -l | --list ]
                                [ -h | --help ] [ -v | --verbose ]"
    exit 2
}

help_panel() {
    echo "Help Panel:
            -p/--package        => Constroi o pacote do PythonEtrap
            -d/--define [VAR]   => Definição de variáveis específicas (yaml)
            -r/--run [MOD]      => Roda o módulo de configuração especificado
            -h/--help           => Mostra esse painel de ajuda
            -v/--verbose        => Modo verbose"
    exit 0
}

BASEDIR=$(dirname $0)

PACKAGE=unset
DEFINE=unset
SET=unset
VERBOSE=unset

define_var() {

}

make_etrap_pkg() {
    python3 -m pip install --upgrade build
    cd $BASEDIR/PythonEtrap
    python3 -m build
    ls -l ./dist/
}

run_config_module() {
    case "$1" in
        anaconda | conda)
            install_anaconda
            break;;
    esac
}

#---------------------------------#
# Configuration modules functions #
#---------------------------------#
install_anaconda() {

}

#-------------------------------#
# Parsing Commandline arguments #
#-------------------------------#
PARSED_ARGS=$(getopt -a -n configure -o plvh:r:d: --long package,list,verbose,help:,run:,define -- "$@")
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
        -d | --define)  
            define_var $2
            shift 2
            ;;
        -r | --run)
            run_config_module $2
            shift 2
            ;;
        -l | --list)
            module_list_dump
            break
            ;;
        -h | --help)
            help_panel
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
