import json
from Building_Vocab import *
from Captions_Cleaning import *
import numpy as np
import pickle

#### Function -> Converting words into vectors Directly - (Embedding Layer Output)
def get_embedding_output(vocab_size, word_to_idx, embedding_index):
    
    emb_dim = 50
    embedding_output = np.zeros((vocab_size,emb_dim))
    
    for word, idx in word_to_idx.items():
        embedding_vector = embedding_index.get(word)
        
        if embedding_vector is not None:
            embedding_output[idx] = embedding_vector
            
    return embedding_output

#### main
def main():

	## load data
	path = "../Files/total_unique_words.txt"
	total_words = load_data(path)

	"""
	word_to_idx is mapping between each unique word in all_vocab to int value 
	and idx_to_word is vice-versa
	"""
	word_to_idx = {}
	idx_to_word = {}

	for i,word in enumerate(total_words):
	    word_to_idx[word] = i+1
	    idx_to_word[i+1] = word

	# Two special words
	idx_to_word[1846] = 'startseq'
	word_to_idx['startseq'] = 1846

	idx_to_word[1847] = 'endseq'
	word_to_idx['endseq'] = 1847

	vocab_size = len(word_to_idx) + 1
	print("Vocab Size",vocab_size)

	## load train_description
	path = "../Files/train_descriptions.txt"
	train_descriptions = load_data(path)

	all_captions_len = []

	for key in train_descriptions.keys():
	    for cap in train_descriptions[key]:
	        all_captions_len.append(len(cap.split()))

	max_len = max(all_captions_len)
	print("max_length :", max_len)

	#### word embedding
	f = open("../Dataset/Glove_6B_50d/glove.6B.50d.txt",encoding='utf8')

	embedding_index = {}
	for line in f:
	    values = line.split()
	    word = values[0]
	    coefs = np.asarray(values[1:], dtype="float")
	    embedding_index[word] = coefs
	f.close()

	embedding_output = get_embedding_output(vocab_size, word_to_idx, embedding_index)
	print("Shape Of Embedding output : ", embedding_output.shape)

	## store info
	path = "../Files/embedding_output.txt"
	np.savetxt(path, embedding_output)

	path = "../Files/variable_caption_processing.txt"
	li = [max_len, vocab_size]
	store_2_txt(path, li)

	path = "../Files/word_to_idx.txt"
	store_2_txt(path, word_to_idx)

	path = "../Files/idx_to_word.pkl"

	with open(path,"wb") as f:
	    pickle.dump(idx_to_word,f)


if __name__=="__main__": 
    main() 