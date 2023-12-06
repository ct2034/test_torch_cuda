import json
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
    n_tests = 5

    durations = {}

    for device in devices:
        durations[device] = []
        for _ in range(n_tests):
            x = torch.randn(10000, 10000, device=device)
            y = torch.randn(10000, 10000, device=device)
            t0 = time.time()
            z = torch.matmul(x, y)
            durations[device].append(time.time() - t0)

    print(json.dumps(durations, indent=2))
    for i in range(n_tests):
        if i == 0:
            continue  # skip first round, since it is usually slower
        assert durations["cuda"][i] < durations["cpu"][i]
