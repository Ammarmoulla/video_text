from django.test import TestCase

# Create your tests here.
# from tkinter import *

# questions = ["Q1", "Q2", "Q3", "Q4"]


# choices = {
     
#     "Q1": ["A. java", "B. c++", "C. py", "D. code"],

#     "Q2": ["A. easy", "B. global", "C. non", "D. both AB"],  

#     "Q3": ["A. after year", "B.after six month", "C. noon", "D. fastly "],

#     "Q4": ["A. easy", "B. global","C. someone recommend", "D. yes "],

# }

# def show_question(question):
#     question_label.config(text=question)
#     choices_listbox.delete(0, END)
#     for choice in choices[question]:
#         choices_listbox.insert(END, choice)

# def check_answer():
#     selected_choice = choices_listbox.get(choices_listbox.curselection())
#     if selected_choice == "الخيار الصحيح":
#         current_question_index = questions.index(question_label.cget("text"))
#         if current_question_index < len(questions) - 1:
#             next_question = questions[current_question_index + 1]
#             show_question(next_question)
#     else:
#         # إجابة خاطئة
#         print("إجابة خاطئة")

# # إنشاء نافذة Tkinter
# window = Tk()
# window.title("برنامج الأسئلة")
# window.geometry("400x300")

# # إنشاء عنصر Label لعرض السؤال
# question_label = Label(window, text="",)
# question_label.pack(pady=20)

# # إنشاء عنصر Listbox لعرض الخيارات
# choices_listbox = Listbox(window, width=50, height=4)
# choices_listbox.pack(pady=10)

# # إنشاء زر للتحقق من الإجابة
# check_button = Button(window, text="check", command=check_answer)
# check_button.pack(pady=10)

# # عرض أول سؤال
# show_question(questions[0])

# # تشغيل حلقة الأحداث الرئيسية
# window.mainloop()




# from tkinter import *
# from tkinter.colorchooser import *
# from tkinter.messagebox import *
# from tkinter.constants import * 

# g=Tk()

# n=StringVar()

# q=1

# questions={" 1.which this program? :":"C. py",
# " 2.why you use py? :":"D. both AB",
# " 3.when you will be a programer?:":"D. fastly ",
# #" 4.why you choice py?: ":"A"
# }
# options=[["A. java","B. c++","C. py","D. code"],    
# ["A. easy","B. global","C. non","D. both AB"],    
# ["A. after year","B.after six month","C. noon","D. fastly "],
# #["A. easy","B. global","C. someone recommend","D. yes "]
# ]     

# def cin():
#     q=1
#     for o in questions:
#         print(o)
#         ff=Button(g, text=o)
#         ff.pack()
#         k =(questions.get(o))
#         print()
#         #q =1
#         for i in options[q-1]:
#                print()
#                c = Radiobutton(g, text = i,fg = "black", width = 12, height = 1,variable=n, value=i ,  bd = 2, bg = "white", cursor = "hand2" ,command=cin)
#                c.pack()
#                s = n.get()
#                #q +=1
#                #n=StringVar()
#         #k =(questions.get(o))
#         #s = n.get()
#         q +=1
#         #k =(questions.get(o))
#         if s == k :
#             #break
#             showinfo(title='information',message='hi.. u passed')
#             #return
#             q +=1
#         if s != k :
#                 showerror(title='error',message='hi.. u missed something')

# cin()
# # g.mainloop()



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django_basics',
#         'USER': 'postgres',
#         'PASSWORD': '36271ahmedd',
#         'HOST': 'localhost',
#         'DISABLE_SERVER_SIDE_CURSORS': True   # <------ new
#     }
# }
