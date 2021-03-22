import torch 
from dalle_pytorch import DiscreteVAE 



vae = DiscreteVAE(
    image_size=256,
    num_layers=3,
    num_tokens=8192,
    codebook_dim=512,
    hidden_dim=64,
    num_resnet_blocks=1,
    temperature=0.9,
    straight_through=False,
)



images = torch.randn(4,3,256,256)
idx = vae.get_codebook_indices(images)
print(idx)
print(idx.size())
