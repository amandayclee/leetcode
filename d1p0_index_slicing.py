def reverse_array(sentence):
    words = sentence.split()
    reverse_words = words[::-1]
    result = ' '.join(reverse_words)
    
    return result

sentence = "Test Okay"
print(reverse_array(sentence))