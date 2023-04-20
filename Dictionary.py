#!/usr/bin/env python
# coding: utf-8

# In[6]:


dictionary = {
  "hello": "xin chào",
  "goodbye": "tạm biệt",
  "thank you": "cảm ơn bạn",
  "please": "làm ơn",
  "yes": "vâng",
  "no": "không",
  "sorry": "xin lỗi",
  "excuse me": "xin lỗi",
  "how are you?": "bạn khỏe không?",
  "I'm fine": "tôi khỏe",
  "what's your name?": "bạn tên gì?",
  "my name is": "tên tôi là",
  "nice to meet you": "rất vui được gặp bạn",
  "where is the nearest restroom?": "nhà vệ sinh gần nhất ở đâu?",
  "how much does it cost?": "nó giá bao nhiêu?",
  "can you help me?": "bạn có thể giúp tôi không?",
  "I don't understand": "tôi không hiểu",
  "please repeat": "làm ơn lặp lại",
  "sorry, I don't know": "xin lỗi, tôi không biết",
  "yes, of course": "có, chắc chắn",
  "no problem": "không vấn đề gì",
  "I love you": "tôi yêu bạn",
  "happy": "hạnh phúc",
  "sad": "buồn",
  "angry": "tức giận",
  "hungry": "đói",
  "thirsty": "khát",
  "tired": "mệt",
  "hot": "nóng",
  "cold": "lạnh",
  "beautiful": "xinh đẹp",
  "handsome": "đẹp trai",
  "ugly": "xấu",
  "funny": "vui nhộn",
  "serious": "nghiêm túc",
  "friendly": "thân thiện",
  "kind": "tốt bụng",
  "generous": "hào phóng",
  "honest": "trung thực",
  "brave": "dũng cảm",
  "smart": "thông minh",
  "stupid": "ngu ngốc",
  "patient": "kiên nhẫn",
  "impatient": "nóng vội",
  "polite": "lịch sự",
  "rude": "vô lễ",
  "excited": "hào hứng",
  "bored": "chán",
  "surprised": "ngạc nhiên",
  "afraid": "sợ",
  "happy birthday": "chúc mừng sinh nhật",
  "congratulations": "chúc mừng",
  "good luck": "chúc may mắn",
  "get well soon": "chúc mau khỏe",
  "sorry for your loss": "xin chia buồn"}

#print(Dictionary["good luck"])
def get_words(dic,word):
    if word in dic.keys():
        return dic[word]
    return None
input_word = input("Enter the word: ")
translated_word = get_words(dictionary,input_word)
if translated_word != None:
    print(translated_word)
else:
    print("The word is not in the Dictionary")


# In[ ]:





# In[ ]:




