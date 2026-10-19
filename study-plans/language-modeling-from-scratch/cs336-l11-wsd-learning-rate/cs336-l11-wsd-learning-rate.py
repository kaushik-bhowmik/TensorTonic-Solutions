import torch

def wsd_learning_rate(
    total_steps: int, warmup_steps: int, stable_steps: int,
    peak_learning_rate: int | float, final_ratio: int | float,
) -> torch.Tensor:

    ans = torch.zeros(total_steps, dtype=torch.float64)

    # Warmup
    if warmup_steps > 0:
        warmup = peak_learning_rate / warmup_steps * (
            1 + torch.arange(warmup_steps, dtype=torch.float64)
        )
        ans[:warmup_steps] = warmup

    # Stable
    ans[warmup_steps:warmup_steps + stable_steps] = peak_learning_rate

    # Decay
    d = total_steps - warmup_steps - stable_steps

    if d == 1:
        ans[warmup_steps + stable_steps:] = final_ratio * peak_learning_rate
    else:
        pj = torch.arange(d, dtype=torch.float64) / (d - 1)

        n = peak_learning_rate * (
            final_ratio
            + (1 - final_ratio) * 0.5 * (1 + torch.cos(torch.pi * pj))
        )

        ans[warmup_steps + stable_steps:] = n

    return ans