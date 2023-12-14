Simple test to see if cuda works on your machine.

## Usage
```
pytest . -vs
```

## Notes on what worked for me
- Ubuntu 22.04
- NVIDIA RTX A3000

This roughly follows [this](https://github.com/RocketCityDynamics/Success-with-Nvidia-545-drivers-in-Ubuntu-22.04-LTS).

### Driver
Install NVIDIA driver from apt:
```
sudo apt install nvidia-diver-535
```
Which should include `linux-modules-nvidia-535-generic` which should automatically include (in this case) `linux-objects-nvidia-535-5.15.0-91-generic`.

### Certificates
If there are problems with certificates, try:
```
wget http://www.mellanox.com/downloads/ofed/mlnx_signing_key_pub.der
mokutil --import mlnx_signing_key_pub.der
```

[src](https://docs.nvidia.com/networking/display/mlnxofedv23100540/uefi+secure+boot)

### CUDA
Get cuda _12.1_ from [nvidia](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=runfile_local).
While installing, ignore warnings that driver is already installed.
And also deselct the option to install the driver again.

### Pytorch
Install pytorch from [pytorch](https://pytorch.org/get-started/locally/).
```
pip install torch
```
Which is verion `2.1.1` and includes for example `nvidia-cudnn-cu12`.