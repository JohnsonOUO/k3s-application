#!/bin/bash

if [ ! -n "$1"  ]; then
    echo "Please input ip"
else
    echo "Run curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --bind-address $1" K3S_NODE_NAME=master sh -s -"
    curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --bind-address $1" K3S_NODE_NAME=master sh -s -
    echo "export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
    sudo chmod 777 /etc/rancher/k3s/k3s.yaml"
    export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
    chmod 777 /etc/rancher/k3s/k3s.yaml
    echo "deploy nginx"
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
    echo "Find node-token"
    echo "sudo cat /var/lib/rancher/k3s/server/node-token"
    token=$(<config.txt) #/var/lib/rancher/k3s/server/node-token
    echo "Please access remote compute and input the following command:"
    echo "################################# COPY THIS COMMAND #############################################"
    echo "curl -sfL https://get.k3s.io | K3S_NODE_NAME=worker K3S_TOKEN=$token K3S_URL=https://$1:6443 sh - "
    echo "#################################################################################################"
fi 