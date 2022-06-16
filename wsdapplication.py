import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer

bank_sents = ['I went to the bank to deposit my money',
'The river bank was full of dead fishes']

plant_sents = ['The workers at the industrial plant were overworked',
'The plant was no longer bearing flowers']

ps = PorterStemmer()

def lesk(context_sentence, ambiguous_word):
    max_overlaps = 0; lesk_sense = None
    context_sentence = context_sentence.split()
    for ss in wn.synsets(ambiguous_word):

        lesk_dictionary = []

        lesk_dictionary += ss.definition().split()

        lesk_dictionary += ss.lemma_names()  
        for hyponym in ss.hyponyms():
        	lesk_dictionary += hyponym.lemma_names() 
        for hypernym in ss.hypernyms():
        	lesk_dictionary += hypernym.lemma_names() 
        for meronym in ss.part_meronyms():
        	lesk_dictionary += meronym.lemma_names() 
        for meronym in ss.substance_meronyms():
        	lesk_dictionary += meronym.lemma_names() 
        for holonym in ss.member_holonyms():
        	lesk_dictionary += holonym.lemma_names() 
        lesk_dictionary = [ps.stem(i) for i in lesk_dictionary]
        context_sentence = [ps.stem(i) for i in context_sentence] 

        overlaps = set(lesk_dictionary).intersection(context_sentence)

        if len(overlaps) > max_overlaps:
            lesk_sense = ss
            max_overlaps = len(overlaps)
    return lesk_sense

print("Context:", bank_sents[0])
answer = (lesk(bank_sents[0],'bank'))
print("Sense:", answer)
print("Definition:",answer.definition())
print('\n')

print("Context:", bank_sents[1])
answer = lesk(bank_sents[1],'bank')
print("Sense:", answer)
print("Definition:",answer.definition())
print('\n')

print("Context:", plant_sents[0])
answer = lesk(plant_sents[0],'plant')
print("Sense:", answer)
print("Definition:",answer.definition())

user_input_sentence = input("input a sentence!\n")
user_input_word = input("input your ambiguous word!\n")

while user_input_sentence != "quit":
  if user_input_word not in user_input_sentence.split():
    print("word not in sentence!")
    break
  answer = lesk(user_input_sentence, user_input_word)
  print(answer)
  print(answer.definition())
  user_input_sentence = input("input a sentence!\n")
  if user_input_sentence == "quit":
    break
  user_input_word = input("input your ambiguous word!\n")
