def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    prob_distributions = np.array(prob_distributions,dtype=float)
    actual_tokens = np.array(actual_tokens)
    t_out = prob_distributions[np.arange(len(actual_tokens)),actual_tokens]
    lt = np.log(t_out)
    H = -np.mean(lt)
    PP = np.exp(H)
    return PP 