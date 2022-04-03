from .models import Category

# if we want to call a function from any template we need to put that function in our
# context processor.
# now this function can be called from anywhere in any template
def header_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)