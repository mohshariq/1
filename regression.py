noise_list=['is','am','are','the']
def remove_noise(input_text):
      text=input_text.split()
      noise_free_text=[word for word in text if word in not noise_list]
      noise_free_sentence=' '.join(noise_free_text)
      return noise_free_sentence
      
      
k=remove_noise("My name is shariq,I am self learner")
print(k)
