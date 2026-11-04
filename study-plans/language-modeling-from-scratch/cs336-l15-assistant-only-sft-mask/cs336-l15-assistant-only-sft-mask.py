import torch

def assistant_only_sft_mask(
    input_ids: torch.Tensor, role_ids: torch.Tensor,
    attention_mask: torch.Tensor, assistant_role: int = 1,
) -> dict:
    """
    Returns a dict: labels (input token dtype), loss_mask (Boolean tensor).
    """
######
    targets = input_ids[:, 1:]

    target_mask = attention_mask[:, 1:]
    source_mask = attention_mask[:, :-1]
    ass_mask = role_ids[:, 1:] == assistant_role

    mask = target_mask & source_mask & ass_mask

    labels = torch.full_like(input_ids, -100)
    labels[:, :-1] = torch.where(mask, targets, -100)

    loss_mask = torch.zeros_like(input_ids, dtype=torch.bool)
    loss_mask[:, :-1] = mask

    return {"labels": labels, "loss_mask": loss_mask}
    
