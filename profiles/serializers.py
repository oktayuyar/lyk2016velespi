from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField,Field

User=get_user_model()

class  UserSerializer(serializers.ModelSerializer):
    email=EmailField(label="E-Posta Adresi")
    class Meta:
        model = User
        fields = ("id", "username","password","email" )
        extra_kwargs={
            "password" :{
                "write_only" :True}
               }


    def create(self, validated_data):
        username=validated_data["username"]
        password=validated_data["password"]
        email=validated_data["email"]
        user_obj=User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class  UserLoginSerializer(serializers.ModelSerializer):
    id = CharField(label="ıd",allow_blank=True, required=True)
    token=CharField(read_only=True)
    username=CharField(label="Kullanıcı Adı",required=True)
    password = serializers.CharField(label="Parola",required=True,
    style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ("id", "username","password","token")
        extra_kwargs={
            "id":{"write_only" :True},
            "password" :{
                "write_only" :True}
               }

    def validate(self, data):
        id=data["id"]
        username=data.get("username",None)
        password = data["password"]

        if not username :
            raise ValidationError("Kullanıcı adını boş bırakmayınız.")

        user = User.objects.filter(
            Q (username=username)
        ).distinct()

        if user.exists()  and user.count()==1:
            user_obj=user.first()
        else:
            raise ValidationError ("Bu kullanıcı adı ile kayıtlı üye bulunmamaktadır.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Yanlış şifre lüften tekrar deneyiniz.")

        data["id"]=user_obj.id
        data["token"]="asfr435AH.asd2332,"
        return data


