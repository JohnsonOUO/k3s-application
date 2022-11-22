#!/bin/bash

if [ ! -n "$1"  ]; then
    echo "Please put ~ at the end"

echo "get Vitis-AI"
cd $1/k3s-application
git clone https://github.com/Xilinx/Vitis-AI.git

echo "copy necessary file" 
cp $1/k3s-application/need/* ~/k3s-application/Vitis-AI

echo "copy training file"
cp -r $1/k3s-application/ALLFORDEMO ~/k3s-application/Vitis-AI

echo "copy socket file"
cp $1/k3s-application/vitis/vitis-server.py ~/k3s-application/Vitis-AI

echo "mkdir Path for Vitis-AI"

mkdir /dev/shm
mkdir /opt/xilinx/overlaybins
mkdir /opt/xilinx/dsa