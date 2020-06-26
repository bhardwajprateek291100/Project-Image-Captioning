from Captions_Cleaning import readTextFile, store_2_txt
import collections
import json

## Load dictionary
def load_data(path):
	descriptions = None
	with open(path,'r') as f:
	    descriptions= f.read()
	json_acceptable_string = descriptions.replace("'","\"")
	descriptions = json.loads(json_acceptable_string)
	return descriptions

#### main
def main():

	## load image_caption dictionary
	dict_path = "../Files/cleaned_image_captions.txt"
	descriptions = load_data(dict_path)

	# Total No of words across all the sentences
	total_words = []
	for key in descriptions.keys():
	    [total_words.append(i) for des in descriptions[key] for i in des.split()]
	print("Total Words %d"%len(total_words))
	## Output 373837

	# Vocab
	vocab = set()
	for key in descriptions.keys():
	    [vocab.update(sentence.split()) for sentence in descriptions[key]]
	print("Vocab Size : %d"% len(vocab))
	## Output 8424

	#### Filter Words from the Vocab according to certain threshold frequncy
	counter = collections.Counter(total_words)
	freq_cnt = dict(counter)

	# Sort this dictionary according to the freq count
	sorted_freq_cnt = sorted(freq_cnt.items(),reverse=True,key=lambda x:x[1])

	# Filter
	threshold = 10
	sorted_freq_cnt  = [x for x in sorted_freq_cnt if x[1]>threshold]
	total_words = [x[0] for x in sorted_freq_cnt]
	print("Total Unique Words:", len(total_words))
	## Output 1845

	## store unique words of frequency > threshold
	path = "../Files/total_unique_words.txt"
	store_2_txt(path, total_words)


if __name__=="__main__": 
    main() 