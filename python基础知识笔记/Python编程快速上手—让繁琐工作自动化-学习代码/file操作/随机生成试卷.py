#随机生成一张试卷，中国省份及省会城市
import random
capitals={'黑龙江':'哈尔滨','吉林':'长春','辽宁':'沈阳','陕西':'西安','山东':'济南','山西':'太原','河北':'石家庄',
          '河南':'郑州','安微':'合肥','江西':'南昌'}
#生成10份文件
for quizNum in range(10):
    #创建试卷和答案文件, %s %基本用法是将值插入到%s占位符的字符串中
    quizFile=open('问题试卷%s.txt' % (quizNum+1),'w')
    #答案
    answerKeyFile =open('答案试卷%s.txt' % (quizNum+1),'w')

    #写入试卷标题和开头
    quizFile.write('姓名：\n\n时间：\n\n班级：\n\n')
    quizFile.write((' '* 20)+'中国省份对应省会城市试卷%s' % (quizNum+1))
    quizFile.write('\n\n')
    #打乱capitals字典
    states=list(capitals.keys())
    random.shuffle(states)

   #循环states,制造10个问题
    for questionNum  in range(10):
        #得到正确和错误的答案
        correctAnswer =capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers=random.sample(wrongAnswers,3)
        answerOptions=wrongAnswers+[correctAnswer]
        random.shuffle(answerOptions)

        #在文件中写入问题
        quizFile.write('%s. %s的省会是?\n' % ((questionNum+1),states[questionNum]))
        for i in range(4):
            quizFile.write(' %s.%s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        #在答案试卷中写入答案
        answerKeyFile.write('%s.%s\n' % (questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
