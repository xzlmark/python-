import webbrowser,sys,pyperclip

if len(sys.argv)>1:
    adress=' '.join(sys.argv[1:])
    print(adress)
else:
    adress=pyperclip.paste()
webbrowser.open('http://www.google.cn/maps/place/'+adress)



 


