 # K3s Cluster Application
*In this document, We will create two nodes (master and worker).
And User can use some cli to complete our goals. 
Those are what we want do.*
1. Remotely Modify bitstream in the pod.
2. Remotely Complile model and Deploy model.
3. Remotely Run Application.

*In order to finish those problems, we have some prparations to do.*
## what will we do ?
1. Create a k3s cluster with a vm and kv260
2. Deploy nginx ingress to let user can connect to server
3. Deploy k8s-device-plugin that k3s can use kv260's resources.
4. Create deployment that can receive information from user.

## Enviroment
* Master node is Ubuntu20.04 on Proxmox
* Worker node is Ubuntu20.04.3 on Kria-kv260

## Install k3s on Master node and deploy nginx ingress
*Open the command line on Master.
Because we will use nginx, we can disable traefik first.*
```
## Install k3s without traefik
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --bind-address 10.20.0.XXX" K3S_NODE_NAME=master sh -s -

## Deploy nginx
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
```
## Create a Cluster with kv260
*Open Master node command line*
```
## Copy the node-token
sudo cat /var/lib/rancher/k3s/server/node-token
```
*Open Kv260 command line*
```
## Install k3s
curl -sfL https://get.k3s.io | K3S_NODE_NAME=worker K3S_TOKEN=<token> K3S_URL=https://10.20.0.1:6443 sh - 
```
*Go back Master command line*

```
## Label the node that we can deploy the pod on a selected node
kubectl label node worker node-role.kubernetes.io/worker=worker
kubectl label node worker id=worker
kubectl label node master id=master
```
## Device-plugin
*We need to let k3s to know the dev on kv260, so we will use device plugin.
On kv260 command line*
```
## create source number of dev
sudo mkdir /etc/colas
sudo touch /etc/colas/cola1
sudo touch /etc/colas/cola1
```
Back to Master Node
```
## Get resource
cd ~/
git clone https://github.com/JohnsonOUO/k3s-application

## Install helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

## Deploy deivce-plugin
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
cd ~/kv260-k3s
make deploy
```

## Deployment
[](src/1.jpg)
### xmutil
we will deploy xmutil pod on kv260
```
## copy socket file to kv260
scp -r ~/xmutil petalinux@10.20.0.33:/home/petalinux/

## Deploy
kubectl apply -f ~/deployment/xmutil.yaml
```

### vitis-al
we will deploy vitis pod on master
```
## get Vitis-AI
cd ~/k3s-application
git clone https://github.com/Xilinx/Vitis-AI.git

## copy 
cp ~/k3s-application/need/* ~/k3s-application/Vitis-AI

## copy training file
cp ~/k3s-application/ALLFORDEMO ~/k3s-application/Vitis-AI

## copy socket file
cp ~/k3s-application/vitis/vitis-server.py ~/k3s-application/Vitis-AI

## Modify volume path to your ~/
nano ~/deployment/vitis.yaml

## Create some folder for vitis-deployment
mkdir /dev/shm
mkdir /opt/xilinx/overlaybins
mkdir /opt/xilinx/dsa


## Deploy
kubectl apply -f ~/deployment/vitis.yaml
```