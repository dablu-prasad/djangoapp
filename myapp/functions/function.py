def handle_uploaded_file(f):
    with open('myapp/static/1.png','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)