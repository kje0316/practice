from django.db import models

# score 모델을 추가해주세요.
# 학생들은 총 여러번의 시험을 볼 수 있습니다.
# 컬럼을 english, math, science에 대한 점수를 기록할 수 있고, 어떤 학생이 언제 본 시험인지도 기록할 수 있도록 해주세요. 

# Serializer도 추가해주세요.

# score_view 도 GET으로 만들기






class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    
class Score(models.Model):
    english = models.CharField(max_length=3)
    math = models.CharField(max_length=3)
    science = models.CharField(max_length=3)
    exam_date = models.DateTimeField()
        
    student = models.ForeignKey(
        Students, on_delete=models.CASCADE, related_name='score_set')