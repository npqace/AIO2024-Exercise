import torch
import torch.nn as nn


class Softmax(nn.Module):
    """
    This class implements the Softmax activation function.

    Softmax normalizes a vector of real numbers into a probability distribution.
    Elements of the output sum to 1 and represent probabilities between 0 and 1.
    """

    def __init__(self):
        """
        The constructor for the Softmax class. It does not require any parameter initialization.
        """
        super().__init__()

    def forward(self, input):
        """
        This method performs the forward pass of the Softmax function.

        Args:
            input (torch.Tensor): A 1D tensor of real numbers.

        Returns:
            torch.Tensor: The Softmax of the input tensor, with the same shape as the input.

        Raises:
            ValueError: If the input tensor is not a 1D tensor.
        """
        if input.dim() != 1:
            raise ValueError("Input must be a 1D tensor.")
        return torch.exp(input) / torch.sum(torch.exp(input))


class softmax_stable(nn.Module):
    """
    This class implements the Softmax activation function with numerical stability.

    Similar to Softmax, it normalizes a vector into probabilities, but it subtracts the
    maximum value before exponentiation to avoid potential numerical overflows.
    """

    def __init__(self):
        """
        The constructor for the softmax_stable class. It does not require any parameter initialization.
        """
        super().__init__()

    def forward(self, input):
        """
        This method performs the forward pass of the Softmax function with numerical stability.

        Args:
            input (torch.Tensor): A 1D tensor of real numbers.

        Returns:
            torch.Tensor: The Softmax of the input tensor with improved numerical stability, with the same shape as the input.

        Raises:
            ValueError: If the input tensor is not a 1D tensor.
        """
        if input.dim() != 1:
            raise ValueError("Input must be a 1D tensor.")

        shifted_input = input - input.max()

        return torch.exp(shifted_input) / torch.sum(torch.exp(shifted_input))
