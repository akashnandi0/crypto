from rest_framework import serializers
from .models import Student

# Validators
def name_caps(value):
    if value[0] != value[0].upper():
        raise serializers.ValidationError('Start with Capital Letter')
       



class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[name_caps])
    roll = serializers.IntegerField()
    state = serializers.CharField(max_length=100, validators=[name_caps])
    city = serializers.CharField(max_length=100, validators=[name_caps])

    # Create Instance
    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    # Update Instance
    def update(self,instance,validate_data):
        print(instance.name)
        instance.name = validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validate_data.get('roll',instance.roll)
        instance.state = validate_data.get('state',instance.state)
        instance.city = validate_data.get('city',instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi'  :
            raise serializers.ValidationError('City must be ranchi')
        return data  