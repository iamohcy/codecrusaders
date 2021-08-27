# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from main.forms import *

from random import choice
from string import ascii_letters, digits
from datetime import datetime
from PIL import ImageOps, Image

import json

def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def login_knights(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/knights/home/')
        else:
            # Return a 'disabled account' error message
            context = {}
            return render(request, 'main/index.html', context)
    else:
        # Return an 'invalid login' error message.
        context = {'login_error': "true"}
        return render(request, 'main/index.html', context)

def home(request):
    context = {}
    return render(request, 'main/index.html', context)

# def forgot_password(request):
#     context = {}
#     return render(request, 'main/forgot_password.html', context)

# def register(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     full_name = request.POST['full_name']
#     email = request.POST['email']
#     dob = request.POST['dob']
#     print dob
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password'],
#             email=form.cleaned_data['email'],
#             first_name=form.cleaned_data['full_name']
#         )
#         veri_code = \
#             ''.join(choice(ascii_letters + digits) for x in xrange(50))
#         profile = Profile(contact_email=form.cleaned_data['email'],
#                           user=user,verification_code=veri_code)
#         profile.save()
#         user.profile = profile
#         # Set as inactive first, need email to set as active.
#         user.is_active = False

#         user.save()
#         base_veri_url = request.build_absolute_uri(reverse('verify'))
#         verification_url = base_veri_url + "?username=" + username + \
#                                            "&verification_code=" + veri_code
#         email_message = \
#             ("Hi %s,\n\n" % user.first_name) + \
#             "You are receiving this email because someone with the " + \
#             ("email address %s has requested a knights " % user.email) + \
#             ("account with the username %s.\n\nPlease " % user.username)+ \
#             "verify your email address and activate your account by " + \
#             ("visiting: %s.\n\nIf you didn't request " % verification_url) + \
#             "such an account, please ignore this email.\n\nPending account " + \
#             "registrations only remain valid for one hour. " +\
#             "If you don't verify your account within this time, the " + \
#             "registration will be reset and you will have to register " + \
#             "again.\n\nThanks,\n- The knights Team."
#         send_mail('knights Support', email_message, "support@knights.com", \
#                   [user.email], fail_silently=False)

#         registration_msg = "A verification email has been sent to the email specified. Kindly follow the instructions in it to finish registering your knights account."
#         context = {"registration_msg": registration_msg}
#         return render(request, 'main/index.html', context)
#     else:
#         context = {'register_form': form}
#         return render(request, 'main/index.html', context)

# def verify(request):
#     if request.method == 'GET':
#         if 'username' in request.GET and 'verification_code' in request.GET:
#             username = request.GET['username']
#             verification_code = request.GET['verification_code']
#             user = User.objects.filter(username=username)[0]
#             if (user.is_active == False and \
#                 user.profile.verification_code == verification_code):
#                 user.is_active = True
#                 user.save()
#                 user.backend='django.contrib.auth.backends.ModelBackend'
#                 login(request, user)
#                 return redirect('/knights/profile/')
#         context = {}
#         return render(request, 'main/index.html', context)
#     else:
#         return HttpResponseForbidden('allowed only via GET')

# def send_password_reset(request):
#     if request.method == 'GET' and 'username' in request.GET:
#         username = request.GET['username'];
#         if (username != None and username != ""):
#             users = User.objects.filter(username=username)
#             # Make sure that this user exists.
#             if (len(users) == 1):
#                 user = users[0]
#                 if (not user.is_active):
#                     context = {'error': "This account has not been activated. Kindly follow the instructions given in the activation email sent to your email."}
#                     return render(request, 'main/forgot_password.html', context)
#                 else:
#                     verification_code = ''.join(choice(ascii_letters + digits) for x in xrange(50))
#                     user.profile.verification_code = verification_code
#                     user.profile.save()
#                     base_veri_url = request.build_absolute_uri(reverse('reset_password_page'))
#                     verification_url = base_veri_url + "?username=" + username + \
#                                                        "&verification_code=" + verification_code
#                     email_message = \
#                         ("Hi %s,\n\n" % user.first_name) + \
#                         "You are receiving this email because someone has attempted " + \
#                         "to reset your password. If you do indeed wish to do so, proceed by " +\
#                         ("visiting the following link:\n\n %s.\n\nIf you didn't request " % verification_url) + \
#                         "a password reset, you can safely ignore this email.\n\n" + \
#                         "Thanks,\n- The knights Team."
#                     send_mail('knights Support', email_message, "support@knights.com", \
#                               [user.email], fail_silently=False)
#                     url = reverse('index')
#                     return redirect(url)
#             else:
#                 context = {'error': "This username does not exist."}
#                 return render(request, 'main/forgot_password.html', context)
#     context = {'error': "Kindly enter in a username."}
#     return render(request, 'main/forgot_password.html', context)

# def reset_password_page(request):
#     if request.method == 'GET':
#         if 'username' in request.GET and 'verification_code' in request.GET:
#             username = request.GET['username']
#             verification_code = request.GET['verification_code']
#             context = {'username': username, 'verification_code': verification_code}
#             return render(request, 'main/change_password.html', context)
#         context = {}
#         return render(request, 'main/index.html', context)
#     else:
#         return HttpResponseForbidden('allowed only via GET')

# def reset_password(request):
#     if request.method == 'POST':
#         if 'username' in request.POST and 'verification_code' in request.POST and \
#            'new_password' in request.POST and 'new_password2' in request.POST:
#             username = request.POST['username'];
#             verification_code = request.POST['verification_code'];
#             new_pw = request.POST["new_password"];
#             new_pw2 = request.POST["new_password2"];
#             if (new_pw == new_pw2):
#                 if (username != None and verification_code != None):
#                     users = User.objects.filter(username=username)
#                     # Make sure that this user exists.
#                     print username
#                     print len(users)
#                     if len(users) == 1:
#                         user = users[0]
#                         if (user.is_active and user.profile.verification_code == verification_code):
#                             user.set_password(new_pw);
#                             user.save()
#                             url = reverse('index')
#                             return redirect(url)
#                     else:
#                         context = {'error': "This user does not exist."}
#                         return render(request, 'main/change_password.html', context)
#             else:
#                 context = {'error': "The passwords do not match."}
#                 return render(request, 'main/change_password.html', context)
#         context = {'error': "Unknown error. Please try again."}
#         return render(request, 'main/change_password.html', context)
#     else:
#         return HttpResponseForbidden('allowed only via POST')


# @login_required(login_url='/knights/')
# def change_password(request):
#     if request.method == 'POST':
#         old_pw = request.POST["old_password"];
#         new_pw = request.POST["new_password"];
#         new_pw2 = request.POST["new_password2"];
#         # Check that new_password and new_password2 match
#         if new_pw != new_pw2:
#             url = reverse('self_profile')
#             return redirect(url)
#         # Check that old password is correct.
#         if request.user.check_password(old_pw):
#             # Change the password!
#             request.user.set_password(new_pw);
#             request.user.save()
#             url = reverse('self_profile')
#             return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def logout_knights(request):
#     logout(request)
#     return redirect('/knights/')

# # Go to your own profile
# @login_required(login_url='/knights/')
# def self_profile(request):
#     return profile(request, request.user.username)

# @login_required(login_url='/knights/')
# def profile(request, username):
#     grumbs_hidden = {"hidden":"hidden", "active":""}
#     followers_hidden = {"hidden":"hidden", "active":""}
#     profile_hidden = {"hidden":"hidden", "active":""}
#     images_hidden = {"hidden":"hidden", "active":""}
#     search_hidden = {"hidden":"hidden", "active":""}
#     # Check whether tab is provided in the context for, then check if it's
#     # provided in the query string. Otherwise use default "grumbs" tab
#     tab = None
#     if ('tab' in request.GET):
#         tab = request.GET["tab"]
#     if (tab != None):
#         tab = request.GET.get("tab")
#     if (tab != None):
#         if tab == "profile":
#             profile_hidden = {"hidden":"", "active":"active"}
#         elif tab == "followers":
#             followers_hidden = {"hidden":"", "active":"active"}
#         elif tab == "images":
#             images_hidden = {"hidden":"", "active":"active"}
#         elif tab == "search":
#             search_hidden = {"hidden":"", "active":"active"}
#         else:
#             grumbs_hidden = {"hidden":"", "active":"active"}
#     else:
#         # Default tab.
#         grumbs_hidden = {"hidden":"", "active":"active"}

#     # Get user grumbs.
#     user = User.objects.filter(username=username)[0]
#     user_grumbs = Grumb.objects.filter(user=user)
#     user_grumbs = user_grumbs.order_by('-datetime')

#     # Get status of profile to logged in user.
#     blocked = user in request.user.profile.blocked_user.all()
#     followed = user in request.user.profile.followed_user.all()

#     # Get follower grumbs.
#     follower_grumbs = Grumb.objects.filter(user__in=user.profile.followed_user.all())
#     follower_grumbs = follower_grumbs.exclude(user=request.user).order_by('-datetime')
#     follower_grumbs = follower_grumbs.exclude(user__in=user.blocked_user_set.all())

#     # Get search results, if any.
#     search_res = None
#     search_text = None
#     if 'search_text' in request.GET:
#         search_text = request.GET['search_text']
#         if search_text != None:
#             search_res = Grumb.objects.filter(text__contains=search_text)
#             search_res = search_res.exclude(user__in=user.blocked_user_set.all())
#             search_res = search_res.order_by('-datetime')

#     context = {'self_profile' : request.user.username == user.username,
#                'other_profile' : request.user.username != user.username,
#                'blocked' : blocked,
#                'followed' : followed,
#                'current_user': request.user,
#                'user': user,
#                'user_grumbs': user_grumbs,
#                'follower_grumbs': follower_grumbs,
#                'user_links': user.profile.links.all(),
#                'grumbs_hidden': grumbs_hidden,
#                'followers_hidden': followers_hidden,
#                'profile_hidden': profile_hidden,
#                'search_hidden': search_hidden,
#                'images_hidden': images_hidden,
#                'search_res': search_res,
#                'contact_form': ProfileContactsForm()}
#     return render(request, 'main/profile.html', context)


# @login_required(login_url='/knights/')
# def update_profile(request, section):
#     if request.method == 'POST':
#         if (section == "about_me"):
#             form = ProfileAboutMeForm(request.POST)
#             if form.is_valid():
#                 aboutme_text = form.cleaned_data['text']
#                 request.user.profile.about_me = aboutme_text
#                 request.user.profile.save()
#         elif (section == "contacts"):
#             form = ProfileContactsForm(request.POST)
#             if form.is_valid():
#                 # print "ABOUTME FORM VALID!"
#                 prof = request.user.profile
#                 prof.contact_phone = form.cleaned_data['phone']
#                 prof.contact_email = form.cleaned_data['email']
#                 prof.contact_address = form.cleaned_data['address']
#                 prof.contact_website = form.cleaned_data['website']
#                 prof.contact_facebook = form.cleaned_data['facebook']
#                 prof.save()
#             else:
#                 # TODO: Pop up saying which field is not valid.
#                 print "Please enter a valid field."
#         elif (section == "links"):
#             form = ProfileLinksForm(request.POST)
#             if form.is_valid():
#                 print "LINKS FORM VALID!"
#                 text = form.cleaned_data['text'].splitlines()
#                 prof = request.user.profile
#                 prof.links.all().delete()
#                 val = URLValidator()
#                 for line in text:
#                     if (line[0:4] == "www."):
#                         line = "http://" + line
#                     # Check that url is really a url.
#                     try:
#                         val(line)
#                         link = Link(url=line)
#                         link.save()
#                         prof.links.add(link)
#                     except ValidationError, e:
#                         print e
#                 prof.save()
#             else:
#                 # TODO: Pop up saying which field is not valid.
#                 print "Please enter a valid field."
#         elif (section == "image"):
#             form = ImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 request.user.profile.profile_pic = form.cleaned_data['image']
#                 request.user.profile.save()

#                 # Auto crop image to square dimensions
#                 image_path = request.user.profile.profile_pic.path
#                 image = Image.open(image_path)
#                 max_width = 500
#                 max_height = 500
#                 image = ImageOps.fit(image, (max_width, max_height,), method=Image.ANTIALIAS)
#                 image.save(image_path)
#             url = reverse('self_profile')
#             return redirect(url)
#         url = reverse('self_profile') + "?tab=profile"
#         return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def post_grumb(request):
#     if request.method == 'POST':
#         form = NewGrumbForm(request.POST, request.FILES)
#         if form.is_valid():
#             grumb = Grumb(user=request.user,
#                           text=form.cleaned_data['text'],
#                           image=form.cleaned_data['image'],
#                           datetime=datetime.now(),
#                           datetime_str=datetime.now().strftime('%d %b'))
#             grumb.save()

#             # Auto crop image to square dimensions
#             if (form.cleaned_data['image'] != None):
#                 image_path = grumb.image.path
#                 image = Image.open(image_path)
#                 (curr_width,curr_height) = image.size
#                 max_width = 900
#                 max_height = 900
#                 if (curr_width >= curr_height):
#                     if (curr_width > max_width):
#                         new_width = max_width
#                         new_height = int((float(max_width)/curr_width) * curr_height)
#                     else:
#                         new_width = curr_width
#                         new_height = curr_height
#                 else:
#                     if (curr_height > max_height):
#                         new_height = max_height
#                         new_width = int((float(max_height)/curr_height) * curr_width)
#                     else:
#                         new_height = curr_height
#                         new_width = curr_width

#                 image = ImageOps.fit(image, (new_width, new_height,), method=Image.ANTIALIAS)
#                 image.save(image_path)

#             url = reverse('self_profile') + "?tab=grumbs"
#             return redirect(url)
#         else:
#             # NEEDS TO HANDLE NO TEXT GRUMBS!
#             print "BAD GRUMB BAD!!"
#             url = reverse('self_profile')
#             return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def post_comment(request):
#     if request.method == 'POST':
#         form = NewCommentForm(request.POST)
#         if form.is_valid():
#             grumb_id = form.cleaned_data['grumb_id']
#             grumb = Grumb.objects.filter(id=grumb_id)[0]
#             if (grumb != None):
#                 comment = Comment(grumb=grumb,
#                                   user=request.user,
#                                   text=form.cleaned_data['text'],
#                                   image=form.cleaned_data['image'],
#                                   datetime=datetime.now(),
#                                   datetime_str=datetime.now().strftime('%d %b'))
#                 comment.save()
#                 # Render the html and send it to javascript callback for
#                 # immediate rendering
#                 html = render_to_string('main/comment.html',{'comment':comment, 'csrf_token_value': request.COOKIES['csrftoken']})
#                 res = {'html': html, 'grumb_id': grumb.id}
#                 return HttpResponse(json.dumps(res),mimetype='application/json')
#             print "Posting to non-existent grumb!"
#             url = reverse('self_profile') + "?tab=grumbs"
#             return redirect(url)
#         else:
#             print "INVALID COMMENT FORM"
#             url = reverse('self_profile') + "?tab=grumbs"
#             return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def update_follower_grumbs(request):
#     if request.method == 'GET':
#         firstGrumbId = request.GET['first_grumb_id']
#         if (len(Grumb.objects.filter(id=firstGrumbId)) != 0):
#             last_visible_grumb = Grumb.objects.filter(id=firstGrumbId)[0]
#             last_update_time = last_visible_grumb.datetime
#             newer_grumbs = Grumb.objects.filter(datetime__gt=last_update_time)
#             new_follower_grumbs = newer_grumbs.filter(user__in=request.user.profile.followed_user.all())
#             new_follower_grumbs = new_follower_grumbs.exclude(user=request.user).order_by('-datetime')
#             new_follower_grumbs = new_follower_grumbs.exclude(user__in=request.user.blocked_user_set.all())

#             if (new_follower_grumbs != None):
#                 # Render the html and send it to javascript callback for
#                 # immediate rendering
#                 html = render_to_string('main/grumbs.html',{'grumbs':new_follower_grumbs, 'csrf_token_value': request.COOKIES['csrftoken']})
#                 res = {'html': html}
#                 return HttpResponse(json.dumps(res),mimetype='application/json')
#             else:
#                 res = {'html': ""}
#                 return HttpResponse(json.dumps(res),mimetype='application/json')
#         else:
#             res = {'html': ""}
#             return HttpResponse(json.dumps(res),mimetype='application/json')
#     else:
#         url = reverse('self_profile')
#         return redirect(url)

# @login_required(login_url='/knights/')
# def dislike(request, source):
#     if request.method == 'POST':
#         source_id = request.POST['source_id']
#         disliked_obj = None
#         if (source=='grumb'):
#             disliked_obj = Grumb.objects.filter(id=source_id)
#         elif (source=='comment'):
#             disliked_obj = Comment.objects.filter(id=source_id)
#         if (disliked_obj != None):
#             disliked_obj[0].dislikes.add(request.user)
#             print list(disliked_obj)
#             dislike_data = serializers.serialize('json', list(disliked_obj) + list(disliked_obj[0].dislikes.all()))
#             return HttpResponse(dislike_data, mimetype='application/json')
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def undislike(request, source):
#     if request.method == 'POST':
#         source_id = request.POST['source_id']
#         undisliked_obj = None
#         if (source=='grumb'):
#             undisliked_obj = Grumb.objects.filter(id=source_id)
#         elif (source=='comment'):
#             undisliked_obj = Comment.objects.filter(id=source_id)
#         if (undisliked_obj != None):
#             undisliked_obj[0].dislikes.remove(request.user)
#             undislike_data = serializers.serialize('json', list(undisliked_obj) + list(undisliked_obj[0].dislikes.all()))
#             return HttpResponse(undislike_data, mimetype='application/json')
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def follow(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         user = User.objects.filter(id=user_id)[0]
#         request.user.profile.followed_user.add(user)
#         url = reverse('profile',args=[user.username])
#         return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def block(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         user = User.objects.filter(id=user_id)[0]
#         request.user.profile.blocked_user.add(user)
#         url = reverse('profile',args=[user.username])
#         return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def unfollow(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         user = User.objects.filter(id=user_id)[0]
#         request.user.profile.followed_user.remove(user)
#         url = reverse('profile',args=[user.username])
#         return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def unblock(request):
#     if request.method == 'POST':
#         user_id = request.POST['user_id']
#         user = User.objects.filter(id=user_id)[0]
#         request.user.profile.blocked_user.remove(user)
#         url = reverse('profile',args=[user.username])
#         return redirect(url)
#     else:
#         return HttpResponseForbidden('allowed only via POST')

# @login_required(login_url='/knights/')
# def search_grumb(request):
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         search_text = form.cleaned_data['text']
#         url = reverse('self_profile') + "?tab=search&search_text=" + search_text
#         return redirect(url)
#     else:
#         # TODO: NEEDS TO HANDLE NO TEXT GRUMBS!
#         print "BAD SEARCH BAD!!"
#         url = reverse('self_profile')
#         return redirect(url)


