import json
import numpy as np
from scipy.spatial.distance import cosine
from scipy.spatial.distance import euclidean

# Load the embeddings from the JSON file
print("Loading embeddings from JSON file...")
input_file = "size_words_embeddings.json"
with open(input_file, "r") as f:
    embeddings = json.load(f)

# Convert embeddings to a numpy array
word_list = list(embeddings.keys())
embedding_array = np.array([embeddings[word] for word in word_list])

# Find the pair of words with the maximum distance
max_distance = 0
word_pair = None

for i in range(len(word_list)): # Get the first word from the array
    for j in range(i + 1, len(word_list)): # Loop through the rest of the array for the second word
        # print(f"Calculating distance between '{word_list[i]}' ('{i}'/'{len(word_list)}') and '{word_list[j]}'")
        # Calculate the distance between the two embeddings (Can use cosine or euclidean distance)
        # dist = cosine(embedding_array[i], embedding_array[j])
        dist = euclidean(embedding_array[i], embedding_array[j])
        # If this is the best so far, save it
        if dist > max_distance:
            max_distance = dist
            word_pair = (word_list[i], word_list[j])

# Get the two furthest embeddings
word1, word2 = word_pair
embedding1 = embeddings[word1]
embedding2 = embeddings[word2]

print(f"The two furthest words are '{word1}' and '{word2}' with a cosine distance of {max_distance}")

# Map all other words to a linear scale
mapped_words = {}
for word, embedding in embeddings.items():
    # Project onto the line between the two furthest embeddings
    projection = np.dot(np.array(embedding) - np.array(embedding1), 
                        np.array(embedding2) - np.array(embedding1)) / np.linalg.norm(np.array(embedding2) - np.array(embedding1))
    mapped_words[word] = projection

# Sort words by their mapped projection value
sorted_mapped_words = dict(sorted(mapped_words.items(), key=lambda item: item[1]))

# Print the scaled mapping
print("Words mapped to a linear scale:")
for idx, (word, projection) in enumerate(sorted_mapped_words.items(), start=1):
    print(f"{idx}. {word.capitalize()} Neil")

