'''
Purpose: This file is used to call openAI's API to get the vector encoding of a list of words.
Use: Update the sizeWords array with words that you find valid and run the script. This will
	 generate a JSON file with the vector encoding of the words for use in other functions.
'''

from openai import OpenAI
import json

# This API Key has a usage limit of $1 which is plenty since these embeddings cost nothing. Don't be the reason we can't have nice things and use it elsewhere.
OPENAI_API_KEY="sk-svcacct-4z0dtrSzbLi1r1HOBl4hRWwFGngZTdRhTaXoqA2lmoCCvGIXpPRZHDRFPnILjwWgL5oIT3BlbkFJO5QW1AEb-CQIm7c3yz6nc01UDZhNqQ3hCv5Dz6w78V56Hl9ZsqvMTruCyDE1amF09V4A"
client = OpenAI(api_key=OPENAI_API_KEY)

# Define the words to use (https://www.thesaurus.com/browse/large)
sizeWords = [
	"broad", 
	"considerable", 
	"enormous",
	"extensive",
	"full",
	"generous",
	"giant", 
	"gigantic", 
	"grand", 
	"great", 
	"hefty", 
	"huge", 
	"immense",
	"massive",
	# "populous", 
	"sizable", 
	"spacious", 
	"substantial", 
	"vast", 
	"wide",
	"cramped", 
	"dwarf", 
	"empty", 
	"inconsiderable", 
	"insignificant", 
	"limited",
	"little", 
	"miniature", 
	"miniscule", 
	"minor", 
	"minute", 
	"narrow", 
	# "poor",
	"restricted", 
	"short", 
	"slight", 
	"small", 
	"teeny", 
	"tiny", 
	"unimportant"
]

# Dictionary to store embeddings
embeddings = {}

for idx, word in enumerate(sizeWords, start=1):
	try:
		print(f"Processing '{word}' ('{idx}/{len(sizeWords)}')")
		response = client.embeddings.create(
			input=word,
			model="text-embedding-3-small"
		)
		embeddings[word] = response.data[0].embedding
	except Exception as e:
		print(f"Error processing word '{word}': {e}")

# Save embeddings to a JSON file
output_file = "size_words_embeddings.json"
with open(output_file, "w") as f:
    json.dump(embeddings, f)

print(f"Embeddings saved to {output_file}")