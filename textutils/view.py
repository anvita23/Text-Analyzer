# Anvita
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    dtext=request.POST.get('text','default')
    #Check the checkboxes
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check if checkbox is on
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!',@#$%^&*:`~"_-()/.;[]{}'''
        for char in dtext:
            if char not in punctuations:
                analyzed =analyzed + char
        params={'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        dtext = analyzed
    if upper == 'on':
        analyzed = dtext.upper()
        params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
        dtext = analyzed

    if extraspaceremover == 'on':
        analyzed=""
        for index,char in enumerate(dtext):
            if not(dtext[index] == " " and dtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        dtext = analyzed

    if newlineremover == 'on':
        analyzed=""
        for char in dtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        dtext=analyzed

    if charcount == 'on':
        analyzed= len(dtext)
        params = {'purpose': 'Character count', 'analyzed_text': analyzed}

    if removepunc!='on' and upper!='on' and extraspaceremover!='on' and newlineremover!='on' and charcount!='on':
        return HttpResponse("Please select atleast one option and try again")

    return render(request, 'analyze.html', params)
