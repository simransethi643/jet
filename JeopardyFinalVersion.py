'''
Created on Mar 25, 2023
@author: c_arm
'''

print('Welcome to Educational Jeopardy! You can select questions from 5 different categories!\nWrite \
EN for the Environmental Questions, CS for the Computer Science Questions, CY for the Cybersecurity Questions\n\
ME for the Mechanical Engineer Questions, and AI for the Artificial Intelligence Questions\n')
print('There are 5 questions in each category worth 100,200,300,400 and 500 points')

'''
This are our global variables.
'''

try:
    num_players = int(input('How many players are playing?: '))
except ValueError:
    num_players = int(input('Type just an integer number please: '))
    

list1= ['EN', 100, 200, 300, 400, 500]
list2 = ['CS', 100, 200, 300, 400, 500]
list3 = ['CY', 100, 200, 300, 400, 500]
list4 = ['ME', 100, 200, 300, 400, 500]
list5 = ['AI', 100, 200, 300, 400, 500]
list_players = []
score_players = []
for i in range(int(num_players)):
    x = str(input(f'Name of player {i+1}: '))
    list_players.append(x)
    score_players.append(0)
turns = 0
number_of_questions = 25
questions_answered = 0

'''
This is our DATAbase of questions, answers, and explanations
'''

categories = ['EN','CS','CY','ME','AI']
questions_value = [100,200,300,400,500]

env_questions = ['What common drug is often found in coffee and tea?', 'What is the concept of Environmental Science?','Which layer of the atmosphere contains the ozone that is responsible for the absorption of UV\
(Ultra - Violet) light?', 'What is Hepatitis A?', 'The adaptation of traditional medicine in industrialized countries\
is termed as CAM, what does that acronym stand for?']

env_answerOptions_1 = ['Opium Poppu','Thorn Apple','Caffeine','Camphor']
env_answerOptions_2 = ['Design, study, and discovery of new materials','The study of humanities, social science, biological science, and physical science','Incorporate\
the information and physical science','Approach about the natural world and the impact']
env_answerOptions_3 = ['Stratosphere','Throposphere','Mesosphere','None of these']
env_answerOptions_4 = ['Water - borne disease','Air - borne disease','Food Contamination','Both (A) and (C)']
env_answerOptions_5 = ['Cooperative and Alternative Medicine','Complementary and Associative Medicine','Cooperative and Associative\
Medicine','Complementary and Alternative Medicine']

env_answers = [env_answerOptions_1, env_answerOptions_2, env_answerOptions_3, env_answerOptions_4, env_answerOptions_5]

env_answer_1 = 'Caffeine'
env_answer_2 = 'Approach about the natural world and the impact'
env_answer_3 = 'Stratosphere'
env_answer_4 = 'Both (A) and (C)'
env_answer_5 = 'Complementary and Alternative Medicine'
env_correct_answers = [env_answer_1,env_answer_2,env_answer_3,env_answer_4,env_answer_5]

env_ansExplanations_1 = 'Caffeine is a drug that stimulates your brain and nervous system.'
env_ansExplanations_2 = 'Environmental studies deals with the issues that affect the life of a living organism. \
It can be various factors that relates to the natural world and the human impact on it.'
env_ansExplanations_3 = 'The ozone absorbs UV light in the stratosphere. It is the most important aspect\
of the atmosphere that makes life possible on earth.'
env_ansExplanations_4 = 'Hepatitis A is generally caused by food and water contamination through chemical waste urban sewage, agricultural waste,etc.'
env_ansExplanations_5 = 'The traditional medicines are usually inexpensive and easily available.'
env_all_ansExplanations = [env_ansExplanations_1,env_ansExplanations_2,env_ansExplanations_3,env_ansExplanations_4,env_ansExplanations_5]

cs_questions =  ['What is the decimal number for 1100?', 'What is the decimal number for 1101 1111?','What is the name of the programming\
language that is named after the world’s first \
programmer?', 'What is the brain of the computer referred to as?', 'Which scientist designed the analytical engine?']

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
cs_explanations_3 = "Ada Lovelace was the world's first computer programmer."
cs_explanations_4 = 'The CPU, the central processing unit, is considered the brain of the computer because it processes and carries out information and instructions.'
cs_explanations_5 = 'The analytical engine (computer) was first invented by Charles Babbage in the early 1800s.'
cs_all_explanations = [cs_explanations_1,cs_explanations_2,cs_explanations_3,cs_explanations_4,cs_explanations_5]

cyber_questions = ['From the selection which one of these duo is a network layer in firewall?', 'Which of the following attacks requires a carrier file to \
self-replicate?','Which of the following uses asymmetric key encryption?', 'Which of the following offers the strongest wireless\
signal encryption', 'Which of the following describes asymmetric key encryption?']

cyber_answerOptions_1 = ['Stateful and Stateless','Dynamic and Static','Anomaly and Signature','Mandatory and discretionary']
cyber_answerOptions_2 = ['Trojan','Virus','Worm','Spam']
cyber_answerOptions_3 = ['AES','RSA','3DES','RC5']
cyber_answerOptions_4 = ['WEP','WAP','WIPS','WPA']
cyber_answerOptions_5 = ['Consists of a private signing key and a public verification key','The sender and receiver must securely\
share a key.','Cannot be used for non-repudiation purposes','Cannot be used for sender authentication']
cy_answers = [cyber_answerOptions_1, cyber_answerOptions_2, cyber_answerOptions_3, cyber_answerOptions_4, cyber_answerOptions_5]

cyber_answer_1 = 'Stateful and Stateless'
cyber_answer_2 = 'Virus'
cyber_answer_3 = 'RSA'
cyber_answer_4 = 'WPA'
cyber_answer_5 = 'Consists of a private signing key and a public verification key.'
cy_correct_answers = [cyber_answer_1, cyber_answer_2, cyber_answer_3, cyber_answer_4, cyber_answer_5]

cyber_explanation_1 = 'A stateless firewall does not keep data about the data streams and connection in the system. So, it evaluates each packet incoming/outgoing the system as a particular and independent element.\
A stateful firewall, however, keeps the information about streams and connections, employing it to evaluate each packet.'
cyber_explanation_2 = "A virus requires a carrier file to spread across a network and replicates by inserting copies into other files. A trojan is defined as an attack that doesn't self - replicate."
cyber_explanation_3 = 'RSA is an algorithm used by modern computers to encrypt and decrypt messages. It is an asymmetric cryptographic algorithm.'
cyber_explanation_4 = 'Wi-Fi Protected Access (WPA), WPA2, and WPA3 encrypt information being transmitted between wireless routers and wireless devices. WPA3 is currently the strongest encryption.'
cyber_explanation_5 = "An asymmetric key algorithm requires two keys: private and public, so no key exchange is needed for communication. Messages are encrypted with tge recipient's public key and decrypted with the recipient's private key."
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

mechENG_explanations_1 = 'Iron is widely used in construction especially the manufacturing of steel. It is widely used in the human body where it is important in oxygen transport in hemoglobin. It is located in Group 8 and it has a melting point of 1538 degree celcius and a boiling point of 2862 degree Celcius being a solid metal at room temperature.'
mechENG_explanations_2 = 'Cast irons are the alloy of iron and carbon that contains 2.1 to 4.3% C, along with other varying amounts of silicon and manganese. This varying carbon range makes them easily castable, asking them to call cast irons.'
mechENG_explanations_3 = 'Binary phase diagrams are based on two-component systems. Here, the two components may be mixed in an infinite number of different proportions, which indicates that composition also becomes a variable, along with pressure and temperature. The iron-carbon phase diagram, Pb-Sn diagram are the best examples of this category.'
mechENG_explanations_4 = 'The eutectic invariant reaction, in general, can be represented as: L---> S1+S2,  L represents the liquid of eutectic composition, and S1 and S2 are two different solids of fixed composition each.'
mechENG_explanations_5 = 'The pudding furnace creates wrought iron (nearly pure iron) from the pig iron. The wrought iron is tougher malleable'
mechENG_all_explanations = [mechENG_explanations_1,mechENG_explanations_2,mechENG_explanations_3,mechENG_explanations_4,mechENG_explanations_5]

ai_questions = ['Who is the "Father of Artificial Intelligence"?', 'On which of the following situations can Blind search can be used?',\
                'In how many category processes is Artificial Intelligence classified?', 'Which of the following\
is a common language for Artificial Intelligence?', 'What is the name of the Artificial Intelligence system that was developed by Daniel Bobrow?']
ai_answerOptions_1 = ['Alan Turning','Charles Babbage','John McCarthy','None of the above']
ai_answerOptions_2 = ['Real - Life Simulation','Small Search Space','Advance Game Theory','None of these']
ai_answerOptions_3 = ['Depends on the input nature','5','2','3']
ai_answerOptions_4 = ['Python','Java','Lisp','PHP']
ai_answerOptions_5 = ['BACON','SIMD','STUDENT','None of these']
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
LISP, significantly influence the design of the language ALGOL, popularized time - sharing, and invented garbage collection.'
ai_explanation_2 = "Blind Search doesn't contain any domain information such as closeness and hence it is best used for a Small Search Space."
ai_explanation_3 = 'AI is classified into three categories processes: Sensing, Reasoning, and Acting'
ai_explanation_4 = "While programming can be done in any language, in today's world Python\
has become the go-to language for AI and ML-related tasks due to its vast and diverse library functionalities."
ai_explanation_5 = 'The name of the Artificial Intelligence system developed by Daniel Bobrow was\
STUDENT, developed in the Lisp Language in 1964.'
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
                    if questions_value.index(int(value)) == j:
                        question_and_answers = [all_questions[i][j],all_answers[i][j]]
                        return question_and_answers
        except ValueError:
            print("Your category or value doesn't exist, categories are: EN, CS, CY, ME and AI. \
Values are: 100, 200, 300, 400 and 500. Try again.\n")
            return False
    return

def answer_explanation_show(categ,value):
    for i in range(0,5):
            if categories.index(categ) == i:
                for j in range(0,5):
                    if questions_value.index(int(value)) == j:
                        answers_and_explanations = [all_correct_answers[i][j],all_explanations[i][j]]
                        return answers_and_explanations
    return

def answers_check(questions_and_answers, answers_and_explanations, answer_check):
    if answer_check == 'A' or answer_check == 'a' or answer_check == '1':
        i = 0
    elif answer_check == 'B' or answer_check == 'b' or answer_check == '2':
        i = 1
    elif answer_check == 'C' or answer_check == 'c' or answer_check == '3':
        i = 2
    elif answer_check == 'D' or answer_check == 'd' or answer_check == '4':
        i = 3
    else:
        answer_check = str(input('Please, just type A, B, C or D: '))
        return(answers_check(questions_and_answers, answers_and_explanations, answer_check))
    if answers_and_explanations[0] == questions_and_answers[1][i]:
        return 1
    else:
        return 0

def winner():
    winner = list_players[score_players.index(max(score_players))]
    print(f'You are the Winner!! {winner}. There might be a chance you tied with someone though, but you are the winner this time!)')
    
def score_change(r_o_w):
    if r_o_w == 1:
        score_players[turns] = score_players[turns] + int(question_value_chosen)
        print('\nThe answer is correct!',answers_and_explanations_to_show[1])
        print(f'\n{list_players[turns]} just won {question_value_chosen} points!\n')
    else:
        score_players[turns] = score_players[turns] - int(question_value_chosen)
        print('\nThe answer is incorrect!',answers_and_explanations_to_show[1])
        print(f'\n{list_players[turns]} just lost {question_value_chosen} points!\n')

def board_first_print():
    print('')
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    
    print('')
    
    for i in range(len(list_players)):
        print(f'{list_players[i]} has {score_players[i]} points')
        
def check_repetition(categ,value):
    try:
        if list1[0] == categ:
            list1[list1.index(int(value))] = 'X'
            return True
        elif list2[0] == categ:
            list2[list2.index(int(value))] = 'X' 
            return True
        elif list3[0] == categ:
            list3[list3.index(int(value))] = 'X' 
            return True
        elif list4[0] == categ:
            list4[list4.index(int(value))] = 'X' 
            return True
        elif list5[0] == categ:
            list5[list5.index(int(value))] = 'X'
            return True
    except ValueError:
        print('You already picked that question in that category!')
        category_chosen = str(input('Choose your category, again: '))
        question_value_chosen = input('Choose your question value again: ')
        return(question_answer_show(category_chosen.upper(),question_value_chosen))

def board_print():
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    print('') 
    
    for i in range(len(list_players)):
        print(f'{list_players[i]} has {score_players[i]} points')

while questions_answered < number_of_questions:
    
    if questions_answered == 0:
        board_first_print()
    
    print('')
    print(f'It is {list_players[turns]} turn!')
    
    category_chosen = str(input('\nChoose your Category (EN,CS,CY,ME,AI): '))
    question_value_chosen = input('A question of what value you want (100,200,300,400,500): ')
    
    question_and_answers_to_show = question_answer_show(category_chosen.upper(),question_value_chosen)
    
    while question_and_answers_to_show == False:
        category_chosen = str(input('Choose your category, again: '))
        question_value_chosen = input('Choose your question value again: ')
        question_and_answers_to_show = question_answer_show(category_chosen.upper(),question_value_chosen)
    
    repetition_value = check_repetition(category_chosen.upper(),question_value_chosen)
    if repetition_value != True:
        rep = True
        question_and_answers_to_show = repetition_value
        
    answers_and_explanations_to_show = answer_explanation_show(category_chosen.upper(),question_value_chosen)
    
    print('\nQuestion:',question_and_answers_to_show[0],'\nPick one of these as your answer!:',question_and_answers_to_show[1],'\n')
    
    user_answer = str(input('What is your answer? Option A, B, C or D?: '))
    
    score_change(answers_check(question_and_answers_to_show, answers_and_explanations_to_show, user_answer))
        
    questions_answered += 1
    turns += 1
    
    board_print()
    
    if turns == num_players:
        turns = 0

    if questions_answered == number_of_questions:
        winner()




