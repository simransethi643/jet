'''
Created on Mar 25, 2023
@author: c_arm
'''

player_1_score = 0
player_2_score = 0
player_3_score = 0

#This is an array of the categories

categories = ['EN', 'CS', 'CY', 'ME', 'AI']
questions_value = [100,200,300,400,500]

#This are the arrays for the questions
env_questions = ['Name the drug associated with the plant source for tea or coffee.', 'Environmental studies is defined \
as the branch that deals with what','Which layer of the atmosphere contains the ozone responsible for the absorption of UV\
 (Ultra - Violet) light?', 'Hepatitis A is a type of what', 'The adaptation of traditional medicine in industrialized countries\
  is termed as CAM, which stands for what']

env_answer_1 = ['Opium Poppu','Thorn Apple','Caffeine','Camphor']
env_answer_2 = ['option1','option2','option3','option4']
env_answer_3 = ['option1','option2','option3','option4']
env_answer_4 = ['option1','option2','option3','option4']
env_answer_5 = ['option1','option2','option3','option4']
env_answers = [env_answer_1, env_answer_2, env_answer_3, env_answer_4, env_answer_5]

cs_questions = ['cs1', 'cs2','cs3', 'cs4', 'cs5']
cs_answer_1 = ['option1','option2','option3','option4']
cs_answer_2 = ['option1','option2','option3','option4']
cs_answer_3 = ['option1','option2','option3','option4']
cs_answer_4 = ['option1','option2','option3','option4']
cs_answer_5 = ['option1','option2','option3','option4']
cs_answers = [cs_answer_1, cs_answer_2, cs_answer_3, cs_answer_4, cs_answer_5]

cyber_questions = ['cy1', 'cy2','cy3', 'cy4', 'cy5']
cy_answer_1 = ['option1','option2','option3','option4']
cy_answer_2 = ['option1','option2','option3','option4']
cy_answer_3 = ['option1','option2','option3','option4']
cy_answer_4 = ['option1','option2','option3','option4']
cy_answer_5 = ['option1','option2','option3','option4']
cy_answers = [cy_answer_1, cy_answer_2, cy_answer_3, cy_answer_4, cy_answer_5]

me_questions = ['me1', 'me2', 'me3', 'me4', 'me5']
me_answer_1 = ['option1','option2','option3','option4']
me_answer_2 = ['option1','option2','option3','option4']
me_answer_3 = ['option1','option2','option3','option4']
me_answer_4 = ['option1','option2','option3','option4']
me_answer_5 = ['option1','option2','option3','option4']
me_answers = [me_answer_1, me_answer_2, me_answer_3, me_answer_4, me_answer_5]

ai_questions = ['ai1', 'ai2', 'ai3', 'ai4', 'ai5']
ai_answer_1 = ['option1','option2','option3','option4']
ai_answer_2 = ['option1','option2','option3','option4']
ai_answer_3 = ['option1','option2','option3','option4']
ai_answer_4 = ['option1','option2','option3','option4']
ai_answer_5 = ['option1','option2','option3','option4']
ai_answers = [ai_answer_1, ai_answer_2, ai_answer_3, ai_answer_4, ai_answer_5]

all_answers = [env_answers, cs_answers, cy_answers, me_answers, ai_answers]

all_questions = [env_questions, cs_questions, cyber_questions, me_questions, ai_questions]

#functions

def question_chosen(categ,value):
    for i in range(0,5):
        try:
            if categories.index(categ) == i:
                for j in range(0,5):
                    if questions_value.index(value) == j:
                        question_and_answers = [all_questions[i][j],all_answers[i][j]]
                        return question_and_answers
        except ValueError:
            return "Your category or value doesn't exist"
    return


print('Welcome to Educational Jeopardy! You can select questions from 5 different categories!')
print('Write ENV for the Environmental Category, CS for the Computer Science Category, CY for the Cybersecurity Questions,\
ME for the Mechanical Engineer Questions and AI for the Artificial Intelligence Questions')

category_chosen = input('Choose your Category: ')
question_value_chosen = int(input('The value of the questions are 100, 200, 300, 400 and 500. What value would you like to choose for this category?:'))

question_to_show = question_chosen(category_chosen,question_value_chosen)

print(question_to_show[0],'\nChoose one of these:',question_to_show[1])



