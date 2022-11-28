## Quick Start
We will use less command to run our system.
Before we start it, we need install some tools.
* Curl 
* Git

### clone repository.
We need get our file first.
```
cd ~
git clone https://github.com/JohnsonOUO/k3s-application.git
```
### Install k3s on Master
In this shell script, I will disable traefik and modify our k3s settting.
**Don't forget to work the lastset line on Worker (Kv260)**
```
# copy the last line and work on worker
sudo ./master1.sh 10.20.0.109
```
### Set resource for device-plugin
**On worker**
*If you want more detail, you can see readme.md*
```
# create resource
sudo mkdir /etc/colas
sudo touch /etc/colas/cola1
sudo touch /etc/colas/cola2
```
### Deploy device-plugin and xmutil
```
# deploy device-plugin
sudo ./master2.sh ~
# cp the file vitis needs
sudo ./master3.sh ~
```
### Deploy Vitis-ai
```
scp -r ~/k3s-application/xmutil petalinux@10.20.0.33:/home/petalinux/

kubectl apply -f ~/k3s-application/deployment/xmutil.yaml

# modify volume in ~/k3s-application/deployment/vitis.yaml
kubectl apply -f ~/k3s-application/deployment/vitis.yaml
```