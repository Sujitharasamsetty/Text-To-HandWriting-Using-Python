import pywhatkit as pwt
fo = open("C:\\Users\\DELL\\Desktop\\question.txt","r")
str=fo.read()
pwt.text_to_handwriting(str,"C:\\Users\\DELL\\Desktop\\result.png",[0,0,255])




