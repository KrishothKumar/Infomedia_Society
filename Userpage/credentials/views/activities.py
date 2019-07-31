from django.shortcuts import render, redirect
from credentials.models import Register, CodePost
from django.contrib.auth.models import auth
from django.contrib import messages
from rest_framework.views import APIView


class show_activities(APIView):
    def get(self, request):
        data = []
        values = {}
        try:
            posts = CodePost.objects.all().order_by('ts')
            for post in posts:
                values = {
                    'description': post.description,
                    'user': post.name,
                    'posted_time': post.ts
                }
                data.append(values)
        except Exception as e:
            print(str(e))
            return render(request, 'activity.html')

        return render(request, 'activity.html', {'rendered_data':data})

    def post(self, request):

        try:
            post = CodePost()
            post.description = request.POST['job_description']
            # post.name = str(request.user.first_name) + ' ' + str(request.user.last_name)
            post.name = str('Jayanth') + ' ' + str('Nagaraj')
            post.save()
        except Exception as e:
            print(e)
            return render(request, 'activity.html')

        return redirect('/activities')
