def feature_store_lookup(feature_store: dict, requests: list, defaults: dict) -> list:
    """
    Returns a list of feature dictionaries.
    """
    # Write code here
    res =[]
    for user in requests:
        this = {}
        user_id = user["user_id"]
        if user_id in feature_store:
            #this[user_id] = feature_store[user_id]
            this.update(feature_store[user_id])
        else:
            #this[user_id]["avg_spend"] = defaults["avg_spend"]
            this.update(defaults)
        this.update(user["online_features"])
        res.append(this)
    return res 