#I have created this file-ars.com.np
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #dict = {'name':'ananta raj shrestha','age':18}
    #return render(request,'index.html',dict)
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def analyze(request):
    #get the text
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    upper = request.POST.get('upper','off')
    removenewline = request.POST.get('removenewline','off')
    removeextraspace = request.POST.get('removeextraspace','off')
    if upper == "on" and removepunc == "on" and removenewline =="on" and removeextraspace == "on":
        punctuations =''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        result =""
        for i in text:
            if i not in punctuations:
                result = result + i.upper()
        result2 = ""
        for i in result:
            if i != "\n" and i!= "\r":
                result2 = result2 + i
        result3 =""
        for i,char in enumerate(result2):
            if not (result2[i] == " " and result2[i+1] == " "):
                result3 = result3+char
        dic = {'analyze':result3}
            
            
        return render(request,'analyze.html',dic)
    elif upper == "on" and removepunc == "on" and removenewline =="on" :
        punctuations =''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        result =""
        for i in text:
            if i not in punctuations:
                result = result + i.upper()
        result2 = ""
       
        for i in result:
            if i != "\n" and i!= "\r":
                result2 = result2 + i
        
        dic = {'analyze':result2}
            
            
        return render(request,'analyze.html',dic)
    elif upper == "on" and removepunc == "on" :
        punctuations =''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        result =""
        for i in text:
            if i not in punctuations:
                result = result + i.upper()
        

        dic = {'analyze':result}
            
            
        return render(request,'analyze.html',dic)
    elif removenewline == "on":
        result = ""
        for i in text:
            if i != "\n" and i!= "\r":
              result = result + i
        dic = {'analyze':result}
        return render(request,'analyze.html',dic)
    elif removepunc == "on":
        
        punctuations =''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
        result =""
        for i in text:
            if i not in punctuations:
                result = result + i
            
            dic = {'analyze':result}
        return render(request,'analyze.html',dic)
    elif upper == "on":
        result = ""
        for i in text:
            result = result + i.upper()
        dic = {'analyze':result}
        return render(request,'analyze.html',dic)

  
    elif removeextraspace =="on":
        result3 =""
        for i,char in enumerate(text):
            if not( text[i] == " " and text[i+1] == " "):
                result3 = result3+char
        dic = {'analyze':result3}
            
            
        return render(request,'analyze.html',dic)
         
    else:
        return render(request,'error.html')
  
      

#def removenewline(request):
    
    #return HttpResponse(''' RemveNewLine  <br><a href="/" style="text-decoration:none;background:blue;color:white;font-size:20px;">Back</a>''')
#def removespace(request):
    #return HttpResponse("RemveSpace")