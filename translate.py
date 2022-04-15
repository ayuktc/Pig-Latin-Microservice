import re
import nltk

nltk.download('punkt')


def translate_to_piglatin(user_input):
    # To keep track of any non-alphabetic characters we may encounter
    non_alphabetic = re.compile('[^a-zA-Z]')

    # Will append each word to this list as we translate it to piglatin and then join at the end
    translated_word = []

    # The word_tokenize method allows us to separate our words, if we have multiple
    words = nltk.word_tokenize(user_input)

    for word in words:
        # Case 1: The word begins with a vowel, so we just add "ay" to the end. Example: eat => eatay
        if (word[0] in 'aeiouy') or (word[0] in "AEIOUY"):
            translated_word.append(word + "ay")

        # Case 2: We come across non-alphabetic characters
        elif non_alphabetic.match(word):
            translated_word.append(word)

        # Case 3: Consonants and consonant clusters
        else:
            contains_vowel = False
            for count, letter in enumerate(word):
                if (letter in 'aeiouy') or (letter in "AEIOUY"):
                    translated_word.append(word[count:] + word[:count] + "ay")
                    contains_vowel = True
                    break

            # Case 4: No vowels (example not provided in spec). Made the assumption to just add "ay" to the end
            if not contains_vowel:
                translated_word.append(word + "ay")

    # In the case of translating a sentence or phrase, ensuring to join it back together.
    final_translation = ' '.join(translated_word)

    return final_translation
