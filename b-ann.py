#JANGAN RECOD AJG
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,balln
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install balln")
    time.sleep(1)
    os.system('python2 b-ann.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")
##### LOGO #####
logo = """
    :::     ::::    ::: :::    ::: :::::::::: :::::::::  
  :+: :+:   :+:+:   :+: :+:   :+:  :+:        :+:    :+: 
 +:+   +:+  :+:+:+  +:+ +:+  +:+   +:+        +:+    +:+ 
+#++:++#++: +#+ +:+ +#+ +#++:++    +#++:++#   +#++:++#:  
+#+     +#+ +#+  +#+#+# +#+  +#+   +#+        +#+    +#+ 
#+#     #+# #+#   #+#+# #+#   #+#  #+#        #+#    #+# 
###     ### ###    #### ###    ### ########## ###    ### 

--------------------------------------------------

 Auther   : Anker production
 GitHub   : https://github.com/4NK3R-PRODUCTION
 YouTube  : Anker production
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                """

cusr = "ANKER"
cpwd = "YT"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UC8f7vtzQnb-VBiIiEBMTOaw')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : ANKER (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : ANKER (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UC8f7vtzQnb-VBiIiEBMTOaw')
        p()
    
def z():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : ANKER (correct)")
    print(" TOOL PASSWORD : YT (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    os.system("chmod +x ..... .......")
    time.sleep(1)
    os.system("./....... &")
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
