"""Compatibility shim for tests.

Tests expect a top-level `conveyor_lane.py`. The implementation lives in
`src/conveyor_lane.py` so re-export the function here.
"""
from src.conveyor_lane import sort_k_sorted

__all__ = ["sort_k_sorted"]

if __name__ == "__main__":
    print(sort_k_sorted([2,6,3,12,56,8], 3))
