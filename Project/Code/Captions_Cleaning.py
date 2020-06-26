import re

#### Function for Read Text Captions
def readTextFile(path):
    with open(path) as f:
        captions = f.read()
    return captions

#### function For Cleaning Captions
def clean_text(sentence):
    sentence = sentence.lower()
    sentence = re.sub("[^a-z]+"," ",sentence)
    sentence = sentence.split()
    sentence  = [s for s in sentence if len(s)>1]
    sentence = " ".join(sentence)
    return sentence

#### function to Clean all Captions
def clean_captions(image_captions):
	for key,caption_list in image_captions.items():
	    for i in range(len(caption_list)):
	        caption_list[i] = clean_text(caption_list[i])
	return image_captions

#### function to store file in txt format
def store_2_txt(path, file_name):
	with open(path,"w") as f:
		f.write(str(file_name))

#### dictionary for image --> cation_list
def make_image_caption_dictionary(captions):
	image_captions = {}

	for x in captions:
	    first,second = x.split('\t')
	    img_name = first.split(".")[0]
	    
	    #if the image id is already present or not
	    if image_captions.get(img_name) is None:
	        image_captions[img_name] = []
	    
	    image_captions[img_name].append(second)

	return image_captions

#### main
def main():
	captions  = readTextFile("../Dataset/Flickr8k/Flickr_Data/Flickr_Data/Flickr_TextData/Flickr8k.token.txt")
	captions = captions.split('\n')[:-1]

	print("length of Captions: ", len(captions))
	## output : 40460
	
	#### Dictionary to Map each Image with the list of captions it has
	image_captions = make_image_caption_dictionary(captions)

	#### Clean all Captions
	image_captions = clean_captions(image_captions)

	#### Write the data to text file
	path = "../Files/cleaned_image_captions.txt"
	store_2_txt(path, image_captions)

if __name__=="__main__": 
    main() 