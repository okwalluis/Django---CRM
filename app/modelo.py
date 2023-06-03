
def generar_forms_py(models_file, forms_file):
    with open(models_file, 'r') as models:
        with open(forms_file, 'w') as forms:
            forms.write("from django import forms\n\n")
            for line in models:
                if "class" in line and "(" in line:
                    model_name = line.split("class")[1].split("(")[0].strip()
                    form_name = model_name + "Form"
                    forms.write(f"class {form_name}(forms.ModelForm):\n")
                    forms.write(f"    class Meta:\n")
                    forms.write(f"        model = {model_name}\n")
                    forms.write(f"        fields = '__all__'\n\n")

models_file = "C://Workspace//python//django//prj-caio//src//users//models.py"
forms_file = "C://Workspace//python//django//prj-caio//src//users//forms2.py"

generar_forms_py(models_file, forms_file)