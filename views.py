from django.shortcuts import render


def index(request):

	context = {}

	return render(
        request,
        'admin_index.html',
        context
    )
