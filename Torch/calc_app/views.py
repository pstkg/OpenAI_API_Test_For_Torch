from django.shortcuts import render
from django.http import HttpResponse
import os
from jinja2 import Template
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Create your views here.

question_answer = [SystemMessage(content='You are a nice AI bot that answers user question. All the answers pertains to post retirement facilities. Kindly ask the most related question depending upon the previous user responses show him/her options and ask.  ')]

only_question = []
only_answer = []
question_answer1=[]
start = "\033[1m"
end = "\033[0;0m"

def home(request):
    return render(request, 'home.html', {'Welcome_msg':'How can I assit you?'})


def ConAI(request):
    os.environ['OPENAI_API_KEY']='Your API Key'
    llm = ChatOpenAI(temperature=0.7)
    global question_answer, question_answer1,start, end
    
#     i=0
#     print('person how do you plan to your retirement?')
#     while i<5:
    question = request.GET['msg']
    question_answer.append(HumanMessage(content= question))
    question_answer1.append('You:     '+question)
    AI_answer = llm(question_answer).content
#         print(f'\nAI: {AI_answer}')
    question_answer.append(AIMessage(content=AI_answer))
    question_answer1.append('AI Asst: '+AI_answer)
    
#     AI_answer= "render"
    return render (request, 'home.html', {'AI_answer': question_answer1, 'counter': 0})
        
#         i+=1