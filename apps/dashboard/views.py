from django.shortcuts import render, redirect
from apps.dashboard.models import *
from django.contrib import messages


def index(request):

    # get all the shows from the DB and pass it back into the HTML template
    context = {
        'shows': Show.objects.all(),

    }

    return render(request, 'dashboard/listShows.html', context)


def createPg(request):
    return render(request, 'dashboard/createShow.html')


def showDetails(request, show_id):

    print('*************inside the showDetials function***************')

    context = {
        'show': Show.objects.get(id=show_id)
    }

    return render(request, 'dashboard/showDetails.html', context)


def createShow(request, methods="POST"):
    print('****************inside the createShow function**********')

    print('this is what is in POST from the submission form', request.POST)

    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message

        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors

        return redirect('/shows/createPG')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the show to be created and save

        Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                            releaseDate=request.POST['date'], desc=request.POST['desc'])

        newestShow = Show.objects.last()
        show_id = newestShow.id

        print('*'*40)
        return redirect(f'/shows/{show_id}')


def deleteShow(request, show_id):

    print('************inside the deleteShow function')

    # manipulating the DB

    show = Show.objects.get(id=show_id)
    show.delete()

    # now redirect to the home page without the passed in show_id

    print('*'*40)
    return redirect('/shows')


def editShow(request, show_id):

    context = {
        'show': Show.objects.get(id=show_id)
    }

    # this route displays the edit pg
    return render(request, 'dashboard/editShow.html', context)


def updateShow(request, show_id, methods='POST'):
    # this route actually updates the show after the button is clicked
    print('*-'*15)

    print('this is the updated information that is getting passed to us by the form post')

    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message

        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors

        return redirect(f'/shows/{show_id}/edit')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the show to be created and save
        changeShow = Show.objects.get(id=show_id)

        changeShow.title = request.POST['title']
        changeShow.desc = request.POST['desc']
        changeShow.network = request.POST['network']

        # changeShow.updated_at = DateTimeField(auto_now=True)
        changeShow.save()

        return redirect(f'/shows/{show_id}')


# def update(request, id):

#     # pass the post data to the method we wrote and save the response in a variable
#     # called errors
#     errors = Blog.objects.basic_validator(request.POST)
#         # check if the errors dictionary has anything in it
#     if len(errors) > 0:
#         # if the errors dictionary contains anything, loop through each
#         # key-value pair and make a flash message
#         for key, value in errors.items():
#             messages.error(request, value)
#         # redirect the user back to the form to fix the errors
#         return redirect('/blog/edit/'+id)
#     else:
#         # if the errors object is empty, that means there were no errors!
#         # retrieve the blog to be updated, make the changes, and save
#         blog = Blog.objects.get(id = id)
#         blog.name = request.POST['name']
#         blog.desc = request.POST['desc']
#         blog.save()
#         messages.success(request, "Blog successfully updated")
#         # redirect to a success route
#         return redirect('/blogs')
