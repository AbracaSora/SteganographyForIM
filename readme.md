# 毕业设计

### 1.主要功能

基于潜在扩散模型（LDM）和自编码器（AE）的文本到图像的隐写框架

使中文文本隐写入载体图片中

### 2.使用Docker运行本项目

1. 根据[Nvidia Container Toolkit官方文档](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)安装Docker和Nvidia Container Toolkit
2. 在项目根目录下运行以下命令构建镜像

```shell
cd depandency && docker build -t steganography .
```
3. 运行以下命令启动容器

```shell
docker run --gpus all -it steganography
```
4. 进入容器后，使用git clone命令下载本项目

```shell
git clone https://github.com/AbracaSora/SteganographyForIM
```

### 3. 代码结构

- 'Embed_Secret.py': 程序的主要入口，构建一个web页面，可以用来演示整个程序
- 'inference.py': 用于演示推理过程
- 'train.py': 用于训练模型