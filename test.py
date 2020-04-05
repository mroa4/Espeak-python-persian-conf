import espeak as es

# import numpy as np

roobin_test = es.RESpeak()

roobin_test.voice = "mb-ir1"
DefName = "M_M_"
text = 'سلام من روبین هستم! رباتِ تعاملیِ جذاب'
roobin_test.speed = 90
roobin_test.pitch = 90
# roobin_test.word_gap = 13
# print(roobin_test.voices)
roobin_test.say(text)
# for i in range(80, 351, 10):  # 27
#   for j in range(0, 101, 10):  # 11
#      for k in range(0, 21, 5):  # 5
#         roobin_test.speed = i
#        roobin_test.pitch = j
#       roobin_test.word_gap = k
#      name = DefName + str(i) + '_' + str(j) + '_' + str(k) + ".mp3"
#     roobin_test.save(text, name)
name = DefName + str("def") + '_' + str("dev") + '_' + str("def") + ".mp3"
roobin_test.save(text, name)
# roobin_test.voice = 'fa+f2'
# roobin_test.say(text)
# roobin_test.save(text, 'f.mp3')
