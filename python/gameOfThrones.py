class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompt = [
        "What is the name of Joffery's first sword? \na) Ice \nb) Needle \nc) Lion's Tooth \nd) Oathkeeper\n",
        "Who poisoned Jon Arryn? \na) Robert Beratheon \nb) Lysa Arryn \nc) Cersei Lannister \nd) Jamie Lannister\n",
        "Who first learned about Rhaeger's marriage to Lyanna? \na) Bran Stark \nb) Samwell Tarley \nc) Gilly \nd) Catelyn Stark\n",
        "Which of these characters has never been told the prophecy about her children? \na) Daenerys \nb) Sansa \nc) Cersei \n",
        "How many times was Beric Dondarrion brought back to life?  \na) 4 \nb) 5 \nc) 6 \nd) 7\n",
        "Who fathered red lady's demon shadow child?  \na) Stannis \nb) Renly \nc) Davos\n",
        "How is Ser Jorah of Mormont related to Lyanna Mormont?  \na) Uncle \nb) Second cousins \nc) First Cousin \nd) Siblings\n",
        "Who was not killed in the Great Sept of Baelor?  \na) Margaery Tyrell \nb) Tommen Baratheon \nc) The high sparrow \nd) Loras Tyrell\n",
        "Who was not killed in the battle of bastards?  \na) Rickon Stark \nb) Ramsay Bolton\nc) Shaggy dog \nd) Jon Snow\n",
        "Which of these languages does Daenerys not speak? \na) High Valyrian \nb) Dothrki \nc) Westerosi/Common \nd) Ghiscari\n",
        "What is the name of Cersei Lannister's handmaid? \na) Missandei \nb) Bernadette \nc) Bernise \nd) Shea\n",
        "Who is not on Arya Stark's kill list? \na) Jamie Lannister \nb) Cersei Lannister \nc) Berie Dondarrion \nd) Melisandre\n",
        "Which Stark family direwolf was the first to meet its tragic end? \na) Lady \nb) Ghost \nc) Grey wind \nd) Nymeria\n",
        "What is Lannister family motto? \na) A lannister always pays his debt \nb) Hear me roar \nc) Everything's better with some wine in the belly \nd) A vial of poison a day keeps the enemy away\n",
        "Which of these is not Daenerys title? \na) The Unburnt \nb) First of her name \nc) Queen of Andes \nd) Mother of dragons\n"
        ]

ques = [
        Questions(question_prompt[0], "c"),
        Questions(question_prompt[1], "b"),
        Questions(question_prompt[2], "c"),
        Questions(question_prompt[3], "b"),
        Questions(question_prompt[4], "c"),
        Questions(question_prompt[5], "a"),
        Questions(question_prompt[6], "c"),
        Questions(question_prompt[7], "b"),
        Questions(question_prompt[8], "d"),
        Questions(question_prompt[9], "d"),
        Questions(question_prompt[10], "b"),
        Questions(question_prompt[11], "a"),
        Questions(question_prompt[12], "a"),
        Questions(question_prompt[13], "b"),
        Questions(question_prompt[14], "c")
        ]
def runTest(ques):
    score = 0   
    for item in ques:
        answer = input(item.prompt) 
        if answer == item.answer:
            score += 1
    print("\nHey! You got " +str(score) + " / " +str(len(ques)) + " correct")
    if score == len(ques):
        print("\n\nYou are the Grand Maester!!!!")
    else:
        print("\n\nIts ok! Better luck next time :)")


runTest(ques)
