#!/bin/bash

echo "Label the node that we can deploy the pod on a selected node"
kubectl label node worker node-role.kubernetes.io/worker=worker
kubectl label node worker id=worker
kubectl label node master id=master

echo "Check helm"
check=$(ls /usr/local/bin | grep helm)
if [ ! -n "$check" ]; then
    echo "install"
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    rm get_helm.sh
fi
echo "deploy device plugin"
cd ~/k3s-application/kv260-k3s
make deploy