from rest_framework import serializers
from .models import Students, Score

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'address', 'email']
        #fields = '__all__' model다 갖고오겠다.위와 같음

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['english','math','science','exam_date','student']
        
    