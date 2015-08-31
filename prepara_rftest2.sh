#!/bin/bash
#--------------------------------------------------
# objetivo: preparar o ambiente para rodar rftest2
#
#     obs.: deve ser executado ANTES de iniciar o Mininet
#--------------------------------------------------

# --Configuracoes--
ipThisHost="192.168.100.70"
iFace="eth1"

# --begin----

rm -rf /var/lib/mongodb/mongod.lock

echo_yellow() {
	echo -e "\e[33;1m${1}\033[0m"
}

ifconfig $iFace $ipThisHost netmask 255.255.255.0
echo -n "IP em $iFace definido para "
echo_yellow "$ipThisHost" 
echo ""
echo "Caso seja necessario mudar o nome da interface(que atualmente eh $iFace), acesse o arquivo:"
echo "/etc/udev/rules.d/70-persistent-net.rules"
echo ""
echo "Apos esta inicializacao, deixe este terminal aberto."
echo "Para fazer testes, abra outro terminal"
echo -n "Pressione uma tecla para iniciar rftest2"
read
cd /root/RouteFlow/rftest
