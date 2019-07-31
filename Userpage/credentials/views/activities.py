from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from rest_framework.views import APIView
from credentials.models import Register, CodePost, Comments


class show_activities(APIView):
    def get(self, request):
        data = []
        try:
            posts = CodePost.objects.all().order_by('-ts')
            for post in posts:
                comments_list = []
                coms = Comments.objects.filter(post_id = post.slno)
                for com in coms:
                    values = {
                        'user': com.user,
                        'comments': com.comments,
                        'posted_time': com.ts,
                        'updated_time': com.ets,
                    }
                    comments_list.append(values)
                values = {
                    'slno': post.slno,
                    'description': post.description,
                    'user': post.user,
                    'posted_time': post.ts,
                    'updated_time': post.ets,
                    'like_count': post.like_count,
                    'share_count': post.share_count,
                    'comments': comments_list
                }

                data.append(values)
        except Exception as e:
            print(str(e))
            return render(request, 'activity.html')

        return render(request, 'activity.html', {'rendered_data':data})

    def post(self, request):
        print(request.POST['post_id'])
        if request.POST['post_id'] == '':
            print("I run now")
            try:
                post = CodePost()
                post.user = str('Jayanth') + ' ' + str('Nagaraj')
                post.description = request.POST['description']
                # post.name = str(request.user.first_name) + ' ' + str(request.user.last_name)
                post.save()
            except Exception as e:
                print(e)

        elif request.POST['post_id']:
            try:
                comment = Comments()
                comment.post_id = CodePost.objects.get(slno=request.POST['post_id'])
                comment.user = str('Jayanth') + ' ' + str('Nagaraj')
                comment.save()
            except Exception as e:
                print(e)

        return redirect('/activities')
