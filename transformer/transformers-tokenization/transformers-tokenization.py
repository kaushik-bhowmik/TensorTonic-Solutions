import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        #print(texts)
        actual = ["<PAD>", "<UNK>", "<BOS>", "<EOS>" ]
        ltext= []
        
        for each in texts:
            this = each.lower().split()
            ltext.extend(this)
        ltext = set(ltext)
        actual.extend(sorted(ltext))
        #print(actual)
        for i in range(len(actual)):
            self.word_to_id[actual[i]] = i 
            self.id_to_word[i] = actual[i]
        self.vocab_size = len(actual)
        #rec = default
        return None 
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        tl = text.lower().split() ; encode =[]
        for each in tl:
            if each in self.word_to_id:
                encode.append(self.word_to_id[each])
            else:
                encode.append(1)
        return encode 
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        decode =[] 
        for each in ids:
            if each in self.id_to_word:
                decode.append(self.id_to_word[each])
            else:
                decode.append(self.unk_token)
        return " ".join(decode)