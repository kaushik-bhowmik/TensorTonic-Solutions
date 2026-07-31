import numpy as np

class GAN:
    def __init__(self, G_W, D_W):
        """
        Initialize GAN with concrete weights.
        """
        self.G_W = np.array(G_W, dtype=float)
        self.D_W = np.array(D_W, dtype=float)
    
    def generate(self, z):
        """
        Generate fake samples from noise z using tanh(z @ G_W).
        Returns list of lists, rounded to 4 decimals.
        """
        # Your implementation here
        z= np.asarray(z,dtype=float)
        res = np.tanh(z@self.G_W)
        #res.tolist()
        return  np.round(res, 4).tolist()
    def discriminate(self, x):
        """
        Classify samples using sigmoid(x @ D_W).
        Returns list of lists, rounded to 4 decimals.
        """
        # Your implementation here
        x= np.asarray(x,dtype=float)
        this = x@self.D_W
        res= 1 / (1 + np.exp(-this))
        return np.round(res, 4).tolist()
    def train_step(self, real_data, z):
        """
        Compute d_loss and g_loss for one training step.
        Returns dict with "d_loss" and "g_loss", rounded to 4 decimals.
        """
        # Your implementation here

        #####
        real_probs = np.asarray(self.discriminate(real_data), dtype=float)
        fake_samples = self.generate(z)
        fake_probs = np.asarray(self.discriminate(fake_samples), dtype=float)
        eps = 1e-8
        rp = np.clip(real_probs, eps, 1-eps) ; fp = np.clip(fake_probs,eps,1-eps)
        term = np.log(rp) + np.log(1-fp)
        dloss = -np.mean(term)
        ####
        fp = np.clip(fake_probs,eps,1-eps)
        term = np.log(fp)
        gloss = -np.mean(term)
        return {"d_loss":dloss, "g_loss":gloss}