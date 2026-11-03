import torch

def vision_transformer_patchify(
    images: torch.Tensor, patch_height: int, patch_width: int,
) -> dict:
    """
    Returns a dict: tokens (image dtype), coordinates (int64 tensor).
    """
    B,C,H,W = images.shape
    x = images.reshape(
    B, C,
    H // patch_height, patch_height,
    W // patch_width, patch_width
    )
    x = x.permute(0, 2, 4, 1, 3, 5)
    tokens = x.reshape(
        B,
        (H // patch_height) * (W // patch_width),
        C * patch_height * patch_width
    )
    rows, cols = torch.meshgrid(
        torch.arange(H // patch_height, device=images.device),
        torch.arange(W // patch_width, device=images.device),
        indexing="ij"
    )
    
    coordinates = torch.stack([rows.flatten(), cols.flatten()], dim=1)
    return {
        "tokens": tokens,
        "coordinates": coordinates
    }
