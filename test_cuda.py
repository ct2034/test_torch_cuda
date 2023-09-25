import torch
import time


def test_basics():
    assert torch.cuda.is_available()


def test_speed():
    """Make sure GPU is faster than CPU"""
    devices = [
        "cpu",
        "cuda"
    ]
    n_tests = 3

    durations = {}

    for device in devices:
        durations[device] = []
        for _ in range(n_tests):
            x = torch.randn(10000, 10000, device=device)
            y = torch.randn(10000, 10000, device=device)
            t0 = time.time()
            z = torch.matmul(x, y)
            durations[device].append(time.time() - t0)

    print(durations)
    for i in range(n_tests):
        assert durations["cuda"][i] < durations["cpu"][i]