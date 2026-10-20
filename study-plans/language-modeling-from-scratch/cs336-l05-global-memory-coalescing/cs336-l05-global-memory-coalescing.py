import numpy as np

def coalescing_analysis(byte_addresses: np.ndarray, access_width_bytes: int = 4, cache_line_bytes: int = 128) -> dict:
    """
    Returns a dict: line_ids (int64 array), transaction_count (int), useful_byte_fraction (float).
    """
    unique_bytes = set()
    unique_line_ids = set()

    for start_addr in byte_addresses:
        end_addr = start_addr + access_width_bytes - 1

        # Collect distinct requested byte addresses
        unique_bytes.update(range(start_addr, end_addr + 1))

        # Collect distinct cache-line IDs
        first_line = start_addr // cache_line_bytes
        last_line = end_addr // cache_line_bytes

        unique_line_ids.update(range(first_line, last_line + 1))

    line_ids = np.array(sorted(unique_line_ids), dtype=np.int64)
    transaction_count = len(line_ids)

    unique_byte_count = len(unique_bytes)
    useful_byte_fraction = (
        unique_byte_count / (transaction_count * cache_line_bytes)
        if transaction_count > 0 else 0.0
    )

    return {
        "line_ids": line_ids,
        "transaction_count": int(transaction_count),
        "useful_byte_fraction": float(useful_byte_fraction),
    }
