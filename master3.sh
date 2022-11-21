#!/bin/bash

echo "get Vitis-AI"
cd ~/k3s-application
git clone https://github.com/Xilinx/Vitis-AI.git

echo "copy" 
cp ~/k3s-application/need/* ~/k3s-application/Vitis-AI

echo "copy training file"
cp -r ~/k3s-application/ALLFORDEMO ~/k3s-application/Vitis-AI

echo "copy socket file"
cp ~/k3s-application/vitis/vitis-server.py ~/k3s-application/Vitis-AI

echo "mkdir"

mkdir /dev/shm
mkdir /opt/xilinx/overlaybins
mkdir /opt/xilinx/dsa