# Importing packages
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet as wn

# Exploring synsets
motorcar = wn.synsets('motorcar')
print('synsets that motorcar belongs to: ' + repr(motorcar))
cars = wn.synset('car.n.01')
print('synset of car sense 1: ' + str(cars))

# Lemma names, definition, examples
print('car sense 1 lemma names: ' + repr(cars.lemma_names()))
print('car sense 1 definition: ' + cars.definition())
print('car sense 1 example sentences: ' + repr(cars.examples()))
car_lemmas = cars.lemmas()
print('car sense 1 lemmas: ' + repr(car_lemmas))

# Reversing our logic
automobile = wn.lemma('car.n.01.automobile')
print('synset of automobile (car sense 1): ' + str(automobile.synset()))
print('name of the automobile lemma: ' + automobile.name())

# All synsets
all_noun_synsets = wn.all_synsets('n')
print('number of noun synsets: ' + str(len(list(all_noun_synsets))))

# All synsets that a word belongs to
car_synsets = wn.synsets('car')
print('synsets that car belongs to: ' + repr(car_synsets))
for synset in car_synsets:
	print(str(synset) + ' ' + repr(synset.lemma_names()))

print('synsets in which car is a lemma: ' +  repr(wn.lemmas('car')))

# Hyponyms
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print('types of motorcars: ' + repr(types_of_motorcar))
print('types of motorcars (all words): ' + repr(sorted([lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()])))

# Hypernyms
print('motorcar hypernyms: ' + repr(motorcar.hypernyms()))
print('motorcar root hypernyms: ' + repr(motorcar.root_hypernyms()))
paths = motorcar.hypernym_paths()
print('first possible path from motorcar to a hypernym: ' + repr(paths[0]))
print('second possible path from motorcar to a hypernym:' + repr(paths[1]))

# Part Meronyms
tree = wn.synset('tree.n.01')
tree_parts = tree.part_meronyms()
print('parts of a tree: ' + repr(tree_parts))

# Substance Meronyms
tree_ingredients = tree.substance_meronyms()
print('materials in a tree: ' + repr(tree_ingredients))

# Member Holonyms
tree_groups = tree.member_holonyms()
print('tree holonyms: ' + repr(tree_groups))

# Entailments
walk = wn.synset('walk.v.01')
walk_entail = walk.entailments()
print('what walking entails: ' + repr(walk_entail))

# Antonyms
supply = wn.lemma('supply.n.02.supply')
not_supply = supply.antonyms()
print('antonyms of supply: ' + repr(not_supply))

# Paths
right = wn.synset('right_whale.n.01')
orca = wn.synset('orca.n.01')
minke = wn.synset('minke_whale.n.01')
tortoise = wn.synset('tortoise.n.01')
novel = wn.synset('novel.n.01')

# More Paths
right_minke = right.lowest_common_hypernyms(minke)
print('right & minke are both: ' + repr(right_minke))
right_orca = right.lowest_common_hypernyms(orca)
print('right & orca are both: ' + repr(right_orca))
right_tortoise = right.lowest_common_hypernyms(tortoise)
print('right & tortoise are both: ' + repr(right_tortoise))
right_novel = right.lowest_common_hypernyms(novel)
print('right & novel are both: ' + repr(right_novel))

# Semantic Distance
print('minimum semantic distance from entity to baleen whale: ' + str(right_minke[0].min_depth()))
print('minimum semantic distance from entity to whale: ' + str(right_orca[0].min_depth()))
print('minimum semantic distance from entity to vertebrate: ' + str(right_tortoise[0].min_depth()))
print('minimum semantic distance from entity to entity: ' + str(right_novel[0].min_depth()))

# Semantic Similarity
right_minke_similarity = right.path_similarity(minke)
print('similarity between right and minke: ' + str(right_minke_similarity))
right_orca_similarity = right.path_similarity(orca)
print('similarity between right and orca: ' + str(right_orca_similarity))
right_tortoise_similarity = right.path_similarity(tortoise)
print('similarity between right and tortoise: ' + str(right_tortoise_similarity))
right_novel_similarity = right.path_similarity(novel)
print('similarity between right and novel: ' + str(right_novel_similarity))
