from django.shortcuts import render, redirect, get_object_or_404


from .models import Answer,Question
from .forms import AnswerForm,QuestionForm
# Create your views here.


def question_list(request):
    questions = Question.objects.all().order_by('created_at')
    return render(request, "question_list.html",{"questions":questions})


def add_question(request):
    if(request.method =='POST'):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_list")
        
    else:
        form = QuestionForm()

    return render(request,"question_add.html",{'form':form})

def question_detail(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    answers = Answer.objects.filter(question=question).order_by('created_at')

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("question_detail", question_id=question.pk)
    else:
        form = AnswerForm()

    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }   

    return render(request, "question_detail.html", context)

