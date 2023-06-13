from rest_framework.decorators import api_view
from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework.views import Response
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def StudentView(request):
    qs = Students.objects.filter() 
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def StudentView(request):
    if request.method == 'GET':
        qs = Students.objects.filter()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def StudentDetailView(request, pk):
    qs = get_object_or_404(Students, pk=pk)
    #특정모델(students)에서 특정 id키(pk)에서 조회를 했을때 값이있으면 갖고오고, 없으면 404
    
    if request.method == 'GET': #
        serializer = StudentSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT': #수정
        serializer = StudentSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': #삭제
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#SCORE

@api_view(['GET'])
def score_view(request):
    qs = Score.objects.all() #데이터 전체 조회
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)


#score 리스트 조회 및 추가 
@api_view(['GET','POST'])  #데이터 추가에 대한 모델 
def score_view(request):
    if request.method == 'GET':  #GET인 경우 전체 조회
        qs = Score.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':  #POST인 경우 추가 
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#score 상세조회, 수정, 삭제 
@api_view(['GET','PUT','DELETE'])
def Score_DetailView(request, pk):
    qs = get_object_or_404(Score, pk=pk)
    
    if request.method == 'GET':
        serializer = ScoreSerializer(qs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ScoreSerializer(qs, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
 
#  GET /students/1/score : 1번학생의 모든 점수 데이터 조회
#  POST /students/1/score : 1번학생의 모든 점수 데이터 추가
   
@api_view(['GET','POST'])
def StudentScoreView(request, pk):
    qs = get_object_or_404(Students, pk=pk)
    
    if request.method == 'GET':
        scores = qs.score_set.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
 
    elif request.method == 'POST':
        serializer = ScoreSerializer(data={'student':qs, **request.data})
        if serializer.is_valid():
            serializer.save(student=qs)
            #score = Score(**serializer.data, student=qs) 위와 동일
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)