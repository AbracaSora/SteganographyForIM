2025/1/20
- 修改了Dockerfile文件，并且在注释中说明了改动的原因

2025/1/31
- 训练了两次模型，分别设置secret_len长度为100和256，成功运行了web演示程序，长度为100的程序演示结果bit acc接近1.0，但允许输入的密文较短，
而长度256结果bit acc仅为0.5左右，根据[博客](https://blog.csdn.net/qq_40859587/article/details/134670207?spm=1001.2014.3001.5502)
描述可能需要修改编码方式来提高准确率