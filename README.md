# TheNeilProblem

## The Problem

In The Problem Squared Podcast 093 the hosts discuss the question of someone who knows a Big Neil and a Small Neil and wondered how many Neils there could be with ever decreasing sizes. One of the solutions discussed involved getting all words that mean size in English and rank them from largest to smallest. It was determined that making a survay would be needed but I decided to try Matt's favorite tool of terrible python code (and some AI) to solve this problem.

## Proposed Solution

LLMs use vector encoding to turn words into vectors (see [this Computerphile video](https://youtu.be/gQddtTdmG_8?si=pmEfaaA_C4TAA_t7) for a great explination). My plan is to:

1. Get a list of words from a thesaurus that match or are the opposite of large (like Bec did on the podcast)
2. Use OpenAI to get the embedding of those words
3. Determine the two furthest apart
4. Project the other words onto the line between the extremes to get a ranking

# Code

## Getting Started:

```bash
git clone git@github.com:josh-gc/TheNeilProblem.git
cd TheNeilProblem
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## The words:

[Thesaurus.com](https://www.thesaurus.com/browse/large) was used with the search word large to get a list of words to use. The strongest matches and opposites were used for the 'sizeWords' array in [getVectorEncoding](getVectorEncoding.py). Poor and Populous were removed because they caused unsatisfactory results. Words can be added or removed from this list then rerun to test other words.

The file encodes all the words and then saves them in [size_words_embeddings.json](size_words_embeddings.json).

## Calculating Ranking:

[calculateOrder](calculateOrder.py) takes the embeddings and:

1. Determines the extreme values
2. Projects all the other words on the line between those two words
3. Returns the ordered list of Neils

# The Results

1. Immense Neil
2. Enormous Neil
3. Massive Neil
4. Gigantic Neil
5. Vast Neil
6. Huge Neil
7. Giant Neil
8. Grand Neil
9. Generous Neil
10. Extensive Neil
11. Sizable Neil
12. Spacious Neil
13. Considerable Neil
14. Great Neil
15. Hefty Neil
16. Wide Neil
17. Inconsiderable Neil
18. Insignificant Neil
19. Broad Neil
20. Substantial Neil
21. Empty Neil
22. Full Neil
23. Unimportant Neil
24. Cramped Neil
25. Miniscule Neil
26. Restricted Neil
27. Teeny Neil
28. Limited Neil
29. Dwarf Neil
30. Miniature Neil
31. Narrow Neil
32. Minute Neil
33. Slight Neil
34. Tiny Neil
35. Minor Neil
36. Little Neil
37. Small Neil
38. Short Neil
