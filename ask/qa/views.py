from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

def test(request, *args, **kwargs):
    return HttpResponse('OK')
    
@require_GET
def question_all(request):
    questions = Question.objects
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(posts,limit)
    paginator.baseurl = '/ask/?page='
    page = paginator.page(page)
    return render(request,'ask/question_all.html', {
        'questions':  questions.object_list,
        'paginator': paginator,
        'page': page,
        })
    
@require_GET
def question_details(request, question_id):
    question = get_object_or_404(Question, question_id=question_id)
    return render(request, 'ask/question_details.html', {
        'question':     question,
        })
