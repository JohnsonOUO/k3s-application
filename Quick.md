## Quick step
### requirements: 
* Curl 
* Git
**clone this repository.**
```
cd ~
git clone https://github.com/JohnsonOUO/k3s-application.git
```
**On Master**
**here is install k3s**
```
# copy the last line to worker
sudo ./master1.sh 10.20.0.109
```
**On worker**
```
# create resource
sudo mkdir /etc/colas
sudo touch /etc/colas/cola1
sudo touch /etc/colas/cola1
```
**Continue on Master**
```
# deploy device-plugin
sudo ./master2.sh ~
# cp the file vitis needs
sudo ./master3.sh ~
```


```
scp -r ~/k3s-application/xmutil petalinux@10.20.0.33:/home/petalinux/

kubectl apply -f ~/k3s-application/deployment/xmutil.yaml

# modify volume in ~/k3s-application/deployment/vitis.yaml
kubectl apply -f ~/k3s-application/deployment/vitis.yaml
```