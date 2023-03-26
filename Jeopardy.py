'''
Created on Mar 25, 2023
@author: c_arm
'''
from _socket import AI_ALL

print('Welcome to Educational Jeopardy! You can select questions from 5 different categories!')
print('Write EN for the Environmental Category, CS for the Computer Science Category')
print('CY for the Cybersecurity Questions, ME for the Mechanical Engineer Questions')
print('and AI for the Artificial Intelligence Questions')

player_1_score = 0
player_2_score = 0
player_3_score = 0
number_of_questions = 25
questions_answered = 0

'''

This is our DATAbase of questions and answers

'''

categories = ['EN', 'CS', 'CY', 'ME', 'AI']
questions_value = [100,200,300,400,500]

env_questions = ['Name the drug associated with the plant source for tea or coffee.', 'Environmental studies is defined \
as the branch that deals with what','Which layer of the atmosphere contains the ozone responsible for the absorption of UV\
 (Ultra - Violet) light?', 'Hepatitis A is a type of what', 'The adaptation of traditional medicine in industrialized countries\
  is termed as CAM, which stands for what']

env_answerOptions_1 = ['Opium Poppu','Thorn Apple','Caffeine','Camphor']
env_answerOptions_2 = ['Design, study, and discovery of new materials','The study of humanities, social, biological and physical science','Incorporate\
the information and physical science','Approach about the natural world and the impact']
env_answerOptions_3 = ['Stratosphere','Throposphere','Mesosphere','None of these']
env_answerOptions_4 = ['Water - borne disease','Air - borne disease','Food Contamination','Both (A) and (C)']
env_answerOptions_5 = ['Cooperative and Alternative Medicine','Complementary and Associative Medicine','Cooperative and Associative\
Medicine','Complementary and Alternative Medicine']

env_answers = [env_answerOptions_1, env_answerOptions_2, env_answerOptions_3, env_answerOptions_4, env_answerOptions_5]

env_answer_1 = 'Caffeine'
env_answer_2 = 'Approach about the natural world and the impact'
env_answer_3 = 'Stratosphere'
env_answer_4 = 'Both (A) abnd (C)'
env_answer_5 = 'Complementary and Alternative Medicine'
env_correct_answers = [env_answer_1,env_answer_2,env_answer_3,env_answer_4,env_answer_5]

env_ansExplanations_1 = 'The tea or coffee contains the drug caffeine that has carious benefits, such as improved brain functioning,\
memory, and etc.'
env_ansExplanations_2 = 'Environmental studies deals with the issues that affect the life of a living organism. \
It can be various factors that relates to the natural world and the human impact on it.'
env_ansExplanations_3 = 'The ozone present absorbs UV light in the stratosphere. It is the most important aspect\
of the atmosphere that makes life possible on earth.'
env_ansExplanations_4 = 'Hepatitis A is generally caused by food and water contamination through chemical waste urban sewage, agricultural waste,etc.'
env_ansExplanations_5 = 'The traditional medicines are inexpensive and easily available.'
env_all_ansExplanations = [env_ansExplanations_1,env_ansExplanations_2,env_ansExplanations_3,env_ansExplanations_4,env_ansExplanations_5]

cs_questions =  ['What is the decimal number for 1100?', 'What is the decimal number for 1101 1111?','The name of the programming\
language that is named after the world’s first \
programmer is?', 'The brain of the computer is referred to as?', 'The analytical engine was designed by who?']

cs_answerOptions_1 = ['3','18','12','8']
cs_answerOptions_2 = ['136','223','220','221']
cs_answerOptions_3 = ['Ada','Swift','Python','Java']
cs_answerOptions_4 = ['RAM','GPU','Motherboard','CPU']
cs_answerOptions_5 = ['Ada Lovelace','Charles Babbage','Tim Berners-Lee','Larry Page']
cs_answers = [cs_answerOptions_1, cs_answerOptions_2, cs_answerOptions_3, cs_answerOptions_4, cs_answerOptions_5]

cs_answer_1 = '12'
cs_answer_2 = '223' 
cs_answer_3 = 'Ada' 
cs_answer_4 = 'CPU'
cs_answer_5 = 'Charles Babbage'
cs_correct_answers = [cs_answer_1,cs_answer_2,cs_answer_3,cs_answer_4,cs_answer_5]

cs_explanations_1 = "In order to calculate the decimal number for 1100, you need to list the power of two from right\
to left below each digit of the binary number. In this case, below the 0 in the one's place, you would write 2^0 which equals 1.\
In the tens place, write 2^1 which equals 2. In the hundreds place, write 2^2 which equals 4. In the thousands place, write 2^3 which equals 8.\
Multiply each power of two by the digit that it is under. In this case, 1*0 = 0, 2*0 = 0, 4*1 = 4, 8*1 = 8. \
Then add all the resulting values which means 0 + 0 + 4 + 8 = 12. The decimal number for 1100 equals 12."
cs_explanations_2 = "In order to calculate the decimal number for 1101 1111, you need to list the power of two from right to left below\
each digit of the binary number. In this case, below the 0 in the one's place, you would write 2^0 which equals 1. In the tens place,\
write 2^1 which equals 2. In the hundreds place, write 2^2 which equals 4. In the thousands place, write 2^3 which equals 8. \
In the ten thousand place, write 2^4 which equals 16. In the hundred thousands place, write 2^5 which equals 32. In the one \
millionth place, write 2^6 which equals 64. In the ten millionth place, write 2^7 which equals 128. Multiply each power \
of two by the digit that it is under. In this case, 1*1 = 1, 2*1 = 2, 4*1 = 4, 8*1 = 8, 16*1 = 16, 32*0 = 0, 64*1 = 64, 128*1 = 128.\
Then add all the resulting values which means 1 + 2 + 4 + 8 +16 + 0 + 64 + 128 = 223. The decimal number for 1101 1111 equals 223."
cs_explanations_3 = 'Ada Lovelace was the world’s first computer programmer.'
cs_explanations_4 = 'The analytical engine (computer) was first invented by Charles Babbage in the early 1800s.'
cs_explanations_5 = 'The analytical engine (computer) was first invented by Charles Babbage in the early 1800s.'
cs_all_explanations = [cs_explanations_1,cs_explanations_2,cs_explanations_3,cs_explanations_4,cs_explanations_5]

cyber_questions = ['What are two types of network layer firewalls?', 'Which of the following attacks requires a carrier file to \
self-replicate?','Which of the following uses asymmetric key encryption?', 'Which of the following offers the strongest wireless\
signal encryption', 'Which of the following descrives asymmetric key encryption?']

cyber_answerOptions_1 = ['Stateful and Stateless','Dynamic and Static','Anomaly and Signature','Mandatory and discretionary']
cyber_answerOptions_2 = ['Trojan','Virus','Worm','Spam']
cyber_answerOptions_3 = ['AES','PGP','3DES','RC5']
cyber_answerOptions_4 = ['WEP','WAP','WIPS','WPA']
cyber_answerOptions_5 = ['Consists of a private signing key and a public verification key','The sender and receiver must securely\
share a key.','Cannot be used for non-repudiation purposes','Cannot be used for sender authentication']
cy_answers = [cyber_answerOptions_1, cyber_answerOptions_2, cyber_answerOptions_3, cyber_answerOptions_4, cyber_answerOptions_5]

cyber_answer_1 = 'Stateful and Stateless'
cyber_answer_2 = 'Virus'
cyber_answer_3 = 'PGP'
cyber_answer_4 = 'WPA'
cyber_answer_5 = 'Consists of a private signing key and a public verification key.'
cy_correct_answers = [cyber_answer_1, cyber_answer_2, cyber_answer_3, cyber_answer_4, cyber_answer_5]

cyber_explanation_1 = 'baba' 
cyber_explanation_2 = 'asdad'
cyber_explanation_3 = 'asdadsada'
cyber_explanation_4 = 'asdadsadadadsada'
cyber_explanation_5 = '2312321313'
cyber_all_explanations = [cyber_explanation_1, cyber_explanation_2, cyber_explanation_3, cyber_explanation_4, cyber_explanation_5]

mechENG_questions = ['What is the melting point of iron (in Celcius)', 'Which of the following material has the carbon varying from\
2.1 to 4.3%?','What is the Iron - Carbon phase diagram?', 'The invariant reaction involving a liquid phase decomposing\
into two different solids on cooling is known as__', 'Wrought iron is a product of__']

mechENG_answerOptions_1 = ['1535','1410','910','768']
mechENG_answerOptions_2 = ['Mild steel','Dead steel','Cast iron','Medium carbon steel']
mechENG_answerOptions_3 = ['Unary phase diagram','Binary phase diagram','Tertiary phase diagram','Ternary phase diagram']
mechENG_answerOptions_4 = ['Eutectic point','Eutectoid point','Peritectoid point','Peritectic point']
mechENG_answerOptions_5 = ['Bessemer converter','Cupola','Pudding furnace','Blast furnace']
me_answers = [mechENG_answerOptions_1, mechENG_answerOptions_2, mechENG_answerOptions_3, mechENG_answerOptions_4, mechENG_answerOptions_5]

mechENG_answer_1 = '1535'
mechENG_answer_2 = 'Cast iron'
mechENG_answer_3 = 'Binary phase diagram'
mechENG_answer_4 = 'Eutectic point'
mechENG_answer_5 = 'Pudding furnace'
mechENG_correct_answers = [mechENG_answer_1,mechENG_answer_2,mechENG_answer_3,mechENG_answer_4,mechENG_answer_5]

mechENG_explanations_1 = 'Iron is widely used in construction especially the manufacturing of steel. It is widely used in the human body where it is importan in oxygen transport in hemoglobin. It is located in Group 8 and it has a melting point of 1538 degree celcius and a boiling point of 2862 degree celcius bein a solid metal at room temperature.'
mechENG_explanations_2 = 'Cast irons are the alloy of iron and carbon that contains 2.1 to 4.3% C, along with other varying amounts of silicon and manganese. This varying carbon range makes them easily castable, asking them to call cast irons.'
mechENG_explanations_3 = 'Binary phase diagrams are based on two-component systems. Here, the two components may be mixed in an infinite number of different proportions, which indicates that composition also becomes a variable, along with pressure and temperature. The iron-carbon phase diagram, Pb-Sn diagram are the best examples of this category.'
mechENG_explanations_4 = 'The eutectic invariant reaction, in general, can be represented as: L---> S1+S2,  L represents the liquid of eutectic composition, and S1 and S2 are two different solids of fixed composition each.'
mechENG_explanations_5 = 'The pudding furnace creates wrought iron (nearly pure iron) from the pig iron. The wrought iron is tougher malleable'
mechENG_all_explanations = [mechENG_explanations_1,mechENG_explanations_2,mechENG_explanations_3,mechENG_explanations_4,mechENG_explanations_5]

ai_questions = ['The "Father of Artificial Intelligence" is?', 'Blind search can be used for which of the following \
situations?','In how many category processes is Artificial Intelligence classified in?', 'Which of the following\
is the common language for Artificial Intelligence?', 'The name of the Artificial Intelligence system developed by Daniel Bobrow was?']
ai_answerOptions_1 = ['Alan Turning','Charles Babbage','John McCarthy','None of the above']
ai_answerOptions_2 = ['Real - Life Simulation','Small Search Space','Advance Game Theory','None of the above']
ai_answerOptions_3 = ['Depends on the input nature','5','2','3']
ai_answerOptions_4 = ['Python','Java','Lisp','PHP']
ai_answerOptions_5 = ['BACON','SIMD','STUDENT','None of the above']
ai_answers = [ai_answerOptions_1, ai_answerOptions_2, ai_answerOptions_3, ai_answerOptions_4, ai_answerOptions_5]

ai_answer_1 = 'John McCarthy'
ai_answer_2 = 'Small Search Space'
ai_answer_3 = '3'
ai_answer_4 = 'Python'
ai_answer_5 = 'STUDENT'
ai_correct_answers = [ai_answer_1,ai_answer_2,ai_answer_3,ai_answer_4,ai_answer_5]

ai_explanation_1= 'John McCarthy was an American Computer Scientist and cognitive scientist.\
He was one of the funders of the discipline of artificial intelligence.He co-authored the document\
that coined the term "artificial intelligence: (AI), developed the programming language family \
LISP, significantly influence the design of the language ALGOL, popularized time -  sharing, and invented garbage collection.'
ai_explanation_2 = "Blind Search doesn't contain any domain information such as closeness and hence it is best used for a Small Search Space."
ai_explanation_3 = 'AI is classified into three categories processes: Sensing, Reasoning, and Acting'
ai_explanation_4 = "While programming can be done in any language, in today's world Python\
has become the go-to language for AI and ML-related tasks due to its vast and diverse library functionalities."
ai_explanation_5 = 'The name of the Artificial Intelligence system developed by Daniel Bobrow was\
STUDENT developed in the Lisp Language in 1964.'
ai_all_explanations = [ai_explanation_1,ai_explanation_2,ai_explanation_3,ai_explanation_4,ai_explanation_5]
'''

DATAbase ends here

'''

all_answers = [env_answers, cs_answers, cy_answers, me_answers, ai_answers]

all_questions = [env_questions, cs_questions, cyber_questions, mechENG_questions, ai_questions]

all_correct_answers = [env_correct_answers,cs_correct_answers,cy_correct_answers,mechENG_correct_answers,ai_correct_answers]

all_explanations = [env_all_ansExplanations,cs_all_explanations,cyber_all_explanations,mechENG_all_explanations,ai_all_explanations]

'''


FUNCTIONS

'''

def question_answer_show(categ,value):
    for i in range(0,5):
        try:
            if categories.index(categ) == i:
                for j in range(0,5):
                    if questions_value.index(value) == j:
                        question_and_answers = [all_questions[i][j],all_answers[i][j]]
                        return question_and_answers
        except ValueError:
            print("Your category or value doesn't exist, categories are: EN, CS, CY, ME and AI. Values are: 100, 200, 300, 400 and 500. Try again.")
            return False
    return

def answer_explanation_show(categ,value):
    for i in range(0,5):
        try:
            if categories.index(categ) == i:
                for j in range(0,5):
                    if questions_value.index(value) == j:
                        answers_and_explanations = [all_correct_answers[i][j],all_explanations[i][j]]
                        return answers_and_explanations
        except ValueError:
            print("Your category or value doesn't exist, categories are: EN, CS, CY, ME and AI. Values are: 100, 200, 300, 400 and 500. Try again.")
            return False
    return

while questions_answered < number_of_questions:
    category_chosen = str(input('Choose your Category: '))
    question_value_chosen = int(input('The value of the questions are 100, 200, 300, 400 and 500.\
What value would you like to choose for this category?:'))
    
    question_and_answers_to_show = question_answer_show(category_chosen,question_value_chosen)
    
    while question_and_answers_to_show == False:
        category_chosen = str(input('Choose your Category, again: '))
        question_value_chosen = int(input('Choose your question value again: '))
        question_and_answers_to_show = question_answer_show(category_chosen,question_value_chosen)
        
    answers_and_explanations_to_show = answer_explanation_show(category_chosen,question_value_chosen)
    
    while question_and_answers_to_show == False:
        category_chosen = str(input('Choose your Category, again: '))
        question_value_chosen = int(input('Choose your question value again: '))
        question_and_answers_to_show = question_answer_show(category_chosen,question_value_chosen)
    
    print(question_and_answers_to_show[0],'\nChoose one of these:',question_and_answers_to_show[1])
    print(answers_and_explanations_to_show[0],'\nExplanation:',answers_and_explanations_to_show[1])
    
    team_answer = input('What is your answer? Option A, B, C or D?: ')
    questions_answered += 1

'''
print(question_and_answers_to_show[0],'\nChoose one of these:',question_and_answers_to_show[1])

team_answer = input('Which is your answer? Option A, B, C or D?: ')

'''    




