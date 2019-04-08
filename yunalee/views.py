from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def result(request):
    text= request.GET['fulltext']
    splitted_text = text.split()
    words_count = len(splitted_text)
    words_Dic= {}
    for x in splitted_text:
        if x in words_Dic:
            words_Dic[x]+=1
        else:
            words_Dic[x] = 1
    return render(request, 'result.html', {
        'text': text,
        'words_Dic' : words_Dic.items(),
        'words_count' : len(splitted_text),
    })
