import torch

# 加载.ckpt文件
checkpoint = torch.load('./models/main_models/final.ckpt')
checkpoint1 = torch.load('./models/first_stage_models/vq-f4/model.ckpt')

# 查看文件内容
epoch = checkpoint['epoch']
global_step = checkpoint['global_step']
optimizer_states = checkpoint['optimizer_states']


print(f'Epoch: {epoch}')
print(f'Global Step: {global_step}')
with open('optimizer_states.txt', 'w') as f:
    f.write(str(optimizer_states))


