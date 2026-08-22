import torch
import torch.nn.functional as F

def composite_layer(x, bn_gamma, bn_beta, bn_mean, bn_var, conv_weight, eps=1e-5):

    x = torch.as_tensor(x, dtype=torch.float64)
    bn_gamma = torch.as_tensor(bn_gamma, dtype=torch.float64)
    bn_beta = torch.as_tensor(bn_beta, dtype=torch.float64)
    bn_mean = torch.as_tensor(bn_mean, dtype=torch.float64)
    bn_var = torch.as_tensor(bn_var, dtype=torch.float64)
    conv_weight = torch.as_tensor(conv_weight, dtype=torch.float64)

    gamma = bn_gamma[None, :, None, None]
    beta = bn_beta[None, :, None, None]
    mean = bn_mean[None, :, None, None]
    var = bn_var[None, :, None, None]

    out = gamma * (x - mean) / torch.sqrt(var + eps) + beta
    out = F.relu(out)

    out = F.conv2d(
        out,
        conv_weight,
        bias=None,
        stride=1,
        padding=1
    )

    return out