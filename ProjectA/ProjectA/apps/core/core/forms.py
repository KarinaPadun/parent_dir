from django import forms
from ..patients.models import Patient
from .forms import PatientForm

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'phone_number')


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'patients/create_patient.html', {'form': form})
