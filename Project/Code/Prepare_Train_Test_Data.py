from Captions_Cleaning import readTextFile, store_2_txt
from Building_Vocab import load_data
import json

#### Fuction to prepare train , test dict to store image ---> caption list
def prepare_test_train_description(data, descriptions):
	data_descriptions = {}
	for img_id in data:
	    data_descriptions[img_id] = []
	    for cap in descriptions[img_id]:
	    	## Tweak - Add <s> and <e> token to our training data
	        cap_to_append = "startseq "  + cap + " endseq"
	        data_descriptions[img_id].append(cap_to_append)

	return data_descriptions

#### main
def main():

	## load data
	train_file_data = readTextFile("../Dataset/Flickr8k/Flickr_Data/Flickr_Data/Flickr_TextData/Flickr_8k.trainImages.txt")
	test_file_data = readTextFile("../Dataset/Flickr8k/Flickr_Data/Flickr_Data/Flickr_TextData/Flickr_8k.testImages.txt")

	## load image_caption dictionary
	dict_path = "../Files/cleaned_image_captions.txt"
	descriptions = load_data(dict_path)

	train = [row.split(".")[0] for row in train_file_data.split("\n")[:-1]]
	test = [row.split(".")[0] for row in test_file_data.split("\n")[:-1]]

	# Prepare Description for the Training Data
	train_descriptions = prepare_test_train_description(train, descriptions)

	# Prepare Description for the Testing Data
	test_descriptions = prepare_test_train_description(test, descriptions)

	## store the info.
	train_path = "../Files/train_descriptions.txt"
	test_path = "../Files/test_descriptions.txt"

	store_2_txt(train_path, train_descriptions)
	store_2_txt(test_path, test_descriptions)


if __name__=="__main__": 
    main() 