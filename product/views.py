import datetime
import pytz

from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import get_user

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Product, Question, Auction, Answers
from .serializers import ProductSerializer, CreateAuctionSerializer, AuctionSerializer, QuestionSerializer, AnswerSerializer
from rest_framework import status, authentication, permissions

from django.core.mail import send_mail

# Create your views here.

#User = settings.AUTH_USER_MODEL

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:9]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_slug):
        try:
            global s; 
            s =Product.objects.get(slug=product_slug)
            #print(s.end_date==datetime.datetime.now())
            utc=pytz.UTC
            #enddate = utc.localize(s.end_date)
            currentdatetime = utc.localize(datetime.datetime.now())
            if(s.end_date<currentdatetime):
               s.bid_active = False
           
            return s
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, product_slug, format=None):
        product = self.get_object(product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class MyProductDetail(APIView):
    def get_object(self, product_slug):
        try:
            global s; 
            s =Product.objects.get(slug=product_slug)

            utc=pytz.UTC
            #enddate = utc.localize(s.end_date)
            currentdatetime = utc.localize(datetime.datetime.now())
            if(s.end_date<currentdatetime):
               s.bid_active = False 

            return s
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, product_slug, format=None):
        product = self.get_object(product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def sendmail(self, product_slug):
        s=Product.objects.get(slug=product_slug)
        auction=Auction.objects.filter(product_id = s).values()
        max = 0
        obj = ''
        count = len(auction)
        counter = 0
        while (counter < count):
            if (auction[counter]['bid'] > max):
                max = auction[counter]['bid']
                obj = auction[counter]
            counter = counter + 1
        
        user=User.objects.get(id=obj['user_id_id'])
        
        mail_body = " Your bid is just declared to be the winning bid for this product \nPlease visit our office to purchase this product as soon as possible.\nThank you\nAuction Service\n\nProduct name: " + s.name + "\n Bid amount: " + str(obj['bid'] )

        print(mail_body)
        send_mail(
            "CONGRATULATIONS!!!",
             mail_body,
            settings.EMAIL_HOST_USER,
            ["shaheerahmedfarooqui758@gmail.com"]
        )
      
        return Response(status=status.HTTP_201_CREATED)


       
           
    

        

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def MyAuction(request):
    print(request.user)
    product = Product.objects.filter(user=request.user)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getQuestions(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    questions = Question.objects.filter(product_id=product)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def searchlist(request):
    if request.data.get('query'):
        products = Product.objects.filter(Q(name__icontains=request.data.get('query')) | Q(description__icontains=request.data.get('query')))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
  


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getAnswers(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    questions = Question.objects.filter(product_id=product).values()
    answers = Answers.objects.filter(question_id=questions[0]['id'])
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateAuction(request):
    serializer = CreateAuctionSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateBid(request):
    serializer1 = AuctionSerializer(data=request.data)
    if(serializer1.is_valid()):
        serializer1.save(user_id=request.user, product_id=s)
        return Response(serializer1.data, status=status.HTTP_201_CREATED)
    return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateQuestion(request):
    serializer = QuestionSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save(user_id=request.user, product_id=s)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateAnswer(request):
    serializer = AnswerSerializer(data=request.data)
    q = Question.objects.get(id=request.data.get('question').get('id'))

    if(serializer.is_valid()):
        serializer.save(question_id = q)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

             
