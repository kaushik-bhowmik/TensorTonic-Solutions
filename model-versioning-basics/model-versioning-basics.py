def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    #pass
    ans ="" ; acc= -1 ; latency =float("inf") ; index= float("inf") ; time = "9999999"
    for i, model in enumerate(models):
        if model["accuracy"]>acc:
            acc = model["accuracy"]
            ans = model["name"]
            latency = model["latency"]
            #index =i 
            time = model["timestamp"]
        elif model["accuracy"]==acc and latency >model["latency"]:
            acc = model["accuracy"]
            ans = model["name"]
            latency = model["latency"]
            #index =i
            time = model["timestamp"]
        elif model["accuracy"]==acc and latency ==model["latency"] and model["timestamp"]>time:
            acc=model["accuracy"]
            ans = model["name"]
            #index = i
            time = model["timestamp"]
    #ans = models[index]["name"]
    return ans 
            
        
        
        