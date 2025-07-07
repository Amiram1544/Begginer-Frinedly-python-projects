#to run this program write the command below in your terminal###
####streamlit run ETE Chatbot.py###












import os
import nltk #pip3 install nltk
import ssl
import streamlit as st #pip3 install streamlit
import random
from sklearn.feature_extraction.text import TfidfVectorizer #pip3 install scikit-learn
from sklearn.linear_model import LogisticRegression



ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')



intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "Salam" , "How are you", "What's up"],
        "responses": ["Hi there", "Hello", "Hey", "Salam" , "I'm fine, thank you", "Nothing much"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Good bye" , "Take care"],
        "responses": ["Goodbye", "See you later", "Take care"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome", "No problem", "Glad I could help"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies.", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment.", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses."]
    },
    {
        "tag": "thank",
        "patterns":["Thats all I needed thanks ","thanks", "thank you", "appreciate it"],
        "responses":["Awesome, glad I could help! Anything else on your mind, or should I let you roll? Have a great day", "you're welcome", "Your welcome", "No problem"]



    },

    {
        "tag": "debt_management",
        "patterns": [
      "How do I pay off debt fast?",
      "What is the snowball method?",
      "What is the avalanche method?",
      "How can I reduce my debt?",
      "How do I manage credit card debt?"
    ],
    "responses":["The snowball method involves paying off your smallest debts first while making minimum payments on the others. This helps build momentum and motivation as you eliminate debts one by one.",
      "The avalanche method focuses on paying off the debt with the highest interest rate first, which saves you money on interest in the long run.",
      "To reduce debt, create a budget, cut unnecessary expenses, and use extra money to pay down your balances. Consider consolidating high-interest debt into a lower-interest loan if possible.",
      "Managing credit card debt requires paying more than the minimum balance, avoiding new charges, and negotiating lower interest rates with your credit card provider."
    ]
  

    },
    
    ]



#vectorizer & classifier

vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0 , max_iter=10000)



#data preprocession

tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent('tag'))
        patterns.append(pattern)


#model training

x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)




def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response



counter = 0

def main():
    global counter
    st.title("Chatbot")
    st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation.")

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
   
    main()