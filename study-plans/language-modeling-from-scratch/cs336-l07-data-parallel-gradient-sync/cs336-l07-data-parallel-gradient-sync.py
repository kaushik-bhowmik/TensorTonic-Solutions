
import torch

def data_parallel_gradient_sync(parameter_replicas: list,
                                gradient_replicas: list,
                                learning_rate: float) -> dict:

    R = len(parameter_replicas)
    num_params = len(parameter_replicas[0])

    mean_gradients = []
    updated_replicas = [[] for _ in range(R)]

    for j in range(num_params):

        # Use rank 0's parameter as the reference for dtype, shape and device
        param = parameter_replicas[0][j]

        # Accumulate gradients in float32
        grad_sum = torch.zeros_like(param, dtype=torch.float32)

        for r in range(R):
            grad = gradient_replicas[r][j]

            if grad is not None:
                grad_sum = grad_sum + grad.to(torch.float32)

        # Average across ALL ranks, including missing gradients
        mean_grad = grad_sum / R

        # Store mean gradient in the parameter's original dtype
        mean_grad = mean_grad.to(dtype=param.dtype)

        mean_gradients.append(mean_grad)

        # Apply the update independently to every replica
        for r in range(R):
            replica_param = parameter_replicas[r][j]

            updated = (
                replica_param.to(torch.float32)
                - learning_rate * mean_grad.to(torch.float32)
            ).to(dtype=replica_param.dtype)

            updated_replicas[r].append(updated)

    return {
        "mean_gradients": mean_gradients,
        "updated_replicas": updated_replicas
    }
