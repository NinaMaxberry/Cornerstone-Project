from django.text import TestCase


from .models import Rep, Zipcodes, District

# Create your tests here.

class ZipcodesModelTests(TestCase):
    def test_zip_creation(self):
        zip = Zipcodes.objects.create(
            zip = 40216
        )
        self.asser


def zipUser_view(request):
    if request.method == "GET":
        form = EntryForm()

        if form.is_valid():
            zipUser_view = EntryForm.cleaned_data['zipUser_view']

    else:
        zipUser_view = EntryForm()

    return render(request, 'home.html', {'form': form})

