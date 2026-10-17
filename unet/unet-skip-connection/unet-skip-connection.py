import numpy as np

def crop_and_concat(encoder_features: np.ndarray,
                    decoder_features: np.ndarray) -> np.ndarray:
    """
    Returns the centered encoder crop concatenated with decoder features.
    """
    x = (encoder_features.shape[1]- decoder_features.shape[1])//2
    y = (encoder_features.shape[2]-decoder_features.shape[2])//2
    enc_crop = encoder_features[:, x:x + decoder_features.shape[1],y:y + decoder_features.shape[2], :]
    out = np.concatenate((enc_crop, decoder_features), axis=3)
    return out 