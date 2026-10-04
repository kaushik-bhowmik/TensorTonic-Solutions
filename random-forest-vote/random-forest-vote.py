from collections import defaultdict

def random_forest_vote(predictions: list) -> list:
    """
    Returns the majority-vote label for every sample.
    """
    n_trees = len(predictions)
    n_samples = len(predictions[0])

    result = []

    for col in range(n_samples):
        votes = defaultdict(int)

        for row in range(n_trees):
            votes[predictions[row][col]] += 1

        best_label = min(
            votes,
            key=lambda label: (-votes[label], label)
        )

        result.append(best_label)

    return result