#%%
import torch
import numpy as np

# %%
checkpoint_path = "./search/Exp/proxyless_jiangrong14/checkpoint/warmup.pth.tar"

# %%
checkpoint = torch.load(checkpoint_path)

# %%
type(checkpoint)

# %%
checkpoint.keys()

# %%
checkpoint['warmup']

# %%
checkpoint['warmup_epoch']

# %%
checkpoint['dataset']

# %%
