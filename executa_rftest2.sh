#!/bin/bash
#-----------------------------------------------------
# objetivo: prepara o ambiente e executa o rftest2
#
#      obs: requer que o RouteFlow ja esteja rodando
#-----------------------------------------------------

# Configuration

ipThisHost="192.168.100.71"
iFace="eth1"

# file of the RouteFlow topology for rftest2
topologyFile="/home/mininet/mininet/custom/topo-4sw-4host.py"
ipRouteFlow="192.168.100.70"

#--begin--

echo_yellow() {
	echo -e "\e[33;1m${1}\033[0m"
}

ifconfig $iFace $ipThisHost netmask 255.255.255.0
echo ""
echo -n "Rede definida para "
echo_yellow "$ipThisHost"
echo "ambiente pronto para iniciar \"rfteste2\""
echo "obs.: ====> requer que o RouteFlow ja esteja rodando. <====="
echo ""
echo -n "Pressione uma tecla para iniciar o rftest2"
read
mn --custom $topologyFile --topo=rftest2 --controller=remote,ip=$ipRouteFlow,port=6633 --pre=/home/mininet/ipconf
