from django.shortcuts import render

from chat_app.models import Group, Chat


def home_page(request):
    return render(request,'chat_app/index.html',{})


def create_group_to_chat_within(request):
    if request.method == "POST":
        group_name = request.POST.get('group_name')  # Get the value from the form
        if group_name:
            Group.objects.create(name=group_name)
            return render(request,'chat_app/create_group.html',{'success':'success'})
    else:
        return render(request,'chat_app/create_group.html',{})


def show_group(request):
    groups = Group.objects.all()
    return render(request,'chat_app/show_group.html',{'groups': groups})


def show_client(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    chat = []
    if group:
        chat = Chat.objects.filter(group=group)
    return render(request, 'chat_app/client.html', {'group_name': group_name, 'chat': chat})