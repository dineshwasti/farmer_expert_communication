from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . forms import FarmerQueryForm, ExpertFeedbackForm
from . models import FarmerQuery
from  . models import ExpertReply
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .classify import classify_image

# Create your views here.
########################## Login and register #########################

def index(request):
    return render(request, 'farmer_expert/index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'farmer_expert/register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_farmer:
                login(request, user)
                return redirect('farmer')
            elif user is not None and user.is_expert:
                login(request, user)
                return redirect('expert')   #customer thio paila
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'farmer_expert/login.html', {'form': form, 'msg': msg})


def farmer(request):
    return render(request,'farmer_expert/farmer.html')


def expert(request):
    return render(request,'farmer_expert/expert.html')
    #return render(request,'farmer_expert/farmer_query_list.html')



####################################################################

############################## Farmer Query View ###################################
def farmer_query_submission(request):
    if request.method == 'POST':
        form = FarmerQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Farmer_request_Submitted')
            
    else:
        form = FarmerQueryForm()

    return render(request, 'farmer_expert/farmer_query_form.html', {'form': form})


def Farmer_request_Submitted(request):
    return render(request, 'farmer_expert/thankyoufarmer.html')


def farmer_query_list(request):
    farmer_query = FarmerQuery.objects.all()
    return render(request, 'farmer_expert/farmer_query_list.html', {'farmer_queries': farmer_query})


def farmer_query_details(request,id):
    farmer_query_details = get_object_or_404(FarmerQuery, id = id)
    return render(request, 'farmer_expert/farmer_queries_details.html', {'farmer_query_details': farmer_query_details})


def expert_feedback_recieved(request):
    user_email = request.user.email
    #Expert= ExpertReply.objects.all()
    Expert = ExpertReply.objects.filter(email=user_email)
    
    #Expert = Expert.first_name
    #print(Expert.filter(id=6))
    
    
   
    #farmer_question= get_object_or_404(FarmerQuery, id =id)
    #return render(request, 'farmer_expert/expert_feedbacks.html', {'farmer_question': farmer_question})
    #farmer_query = FarmerQuery.objects.all()
    #expert_feedback = ExpertReply.objects.all()
    return render(request, 'farmer_expert/expert_feedbacks.html', {'Expert': Expert})
    #'expert_feedback':expert_feedback})


############################## Farmer Query View Till Here ###############################

######################################## Expert reply #########################################


def expert_reply(request):
    if request.method == 'POST':
        form = ExpertFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Expert_Reply_Submitted')
            
    else:
        form = ExpertFeedbackForm()

    return render(request, 'farmer_expert/expert_reply_form.html', {'form': form})


def Expert_Reply_Submitted(request):
    return render(request, 'farmer_expert/thankyouexpert.html')




"""

def expert_reply(request):
    farmer_query_details = get_object_or_404(FarmerQuery, id = id)
    form = ExpertFeedbackForm()

    if request.method =='POST':
        form = ExpertFeedbackForm()
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.query = farmer_query_details
            feedback.save()
            return redirect ('Expert_feedback_Thankyou')
    feedbacks = ExpertReply.objects.filter(query = farmer_query_details)

    return render(request, 'farmer_expert/expert_reply.html', {'farmer_query_details': farmer_query_details})



def query_detail(request, query_id):
    query = get_object_or_404(Query, pk=query_id)
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.query = query
            feedback.save()
            return redirect('Expert_feedback_Thankyou')
    

    feedbacks = Feedback.objects.filter(query=query)
    return render(request, 'query_detail.html', {'query': query, 'form': form, 'feedbacks': feedbacks})

def Expert_feedback_Thankyou(request):
    return render(request, 'expert_feedback_thankyou.html')


    """


################## classification part here #############################

def disease(request):
    return render(request, 'farmer_expert/disease.html')


def classify(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filePathName=fs.save(uploaded_image.name,uploaded_image) # new line 
        filePathName=fs.url(filePathName)  # new line

        image_path = os.path.join('media', fs.save(uploaded_image.name, uploaded_image))

        predicted_class, prediction_probs = classify_image(image_path)

        #Green Mold', 'Healthy Mushroom', 'Healthy Mycelium','Yellow Blotch'
        if prob>=90
        if predicted_class=='Green Mold' and prediction_probs[0][0]>0.9:
            return render(request, 'farmer_expert/Green_Mold.html', {'image_path': filePathName, 'predicted_class': predicted_class})
        elif predicted_class=='Healthy Mushroom' and prediction_probs[0][1]>0.9:
            return render(request, 'farmer_expert/Healthy_Mushroom.html', {'image_path': filePathName, 'predicted_class': predicted_class})
        elif predicted_class=='Healthy Mycelium' and prediction_probs[0][2]>0.9:
            return render(request, 'farmer_expert/Healthy_Mycelium.html', {'image_path': filePathName, 'predicted_class': predicted_class})
        elif predicted_class=='Yellow Blotch' and prediction_probs[0][3]>0.9:
            return render(request, 'farmer_expert/Yellow_Blotch.html', {'image_path': filePathName, 'predicted_class': predicted_class})
        else:
            return render(request, 'farmer_expert/disease.html')
    

