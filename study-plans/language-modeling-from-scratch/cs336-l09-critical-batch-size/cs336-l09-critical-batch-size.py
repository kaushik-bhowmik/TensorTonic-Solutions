import torch

def critical_batch_size(
    batch_sizes: torch.Tensor,
    steps_to_target: torch.Tensor,
    reached_mask: torch.Tensor
) -> dict:
    # Convert before multiplication to avoid int64 overflow.
    examples_tensor = batch_sizes.to(torch.float64) * steps_to_target.to(torch.float64)

    reached_examples = examples_tensor[reached_mask]
    reached_steps = steps_to_target[reached_mask].to(torch.float64)

    min_steps = reached_steps.min()
    min_examples = reached_examples.min()

    critical = min_examples / min_steps

    examples = [
        e.item() if m.item() else None
        for e, m in zip(examples_tensor, reached_mask)
    ]

    return {
        "examples": examples,
        "min_steps": min_steps.item(),
        "min_examples": min_examples.item(),
        "critical_batch_size": critical.item(),
    }