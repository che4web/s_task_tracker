from django import forms

class TaskSearchForm(forms.Form):
    name = forms.CharField(label="Название таски",required=False)

    employee= forms.CharField(label="Сотрудник",required=False)
    deadlite= forms.DateField(label="data",required=False,
                              input_formats=['%Y-%m-%d','%d.%m.%Y']
                              )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
