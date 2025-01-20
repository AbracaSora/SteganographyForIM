# 毕业设计

### 1.主要功能

基于潜在扩散模型（LDM）和自编码器（AE）的文本到图像的隐写框架

使中文文本隐写入载体图片中

### 2.安装

终端运行以下指令安装Docker：

```
sudo apt update

sudo apt install docker.io
```

进入Dockerfile所在的根目录，运行以下命令行构建Docker容器：

```
docker build -t docker_name .
```

其中，docker_name为自定义创建镜像的名称，.表示Dockerfile所在的根目录地址。

在终端中运行以下命令以运行Docker容器：

```
docker run -it image_name
```

其中，docker_name是创建建的Docker镜像的名称。

进入项目的根目录，找到所附带的requirements.txt文件，运行以下命令来安装所有的依赖项：

```
conda install --file requirement.txt
```

运行结束后，检查报错情况，并运行以下指令对依赖项进行检查：

```
conda list
```

### 

