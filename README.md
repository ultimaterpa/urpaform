# urpaform

Extension for filling in forms with [UltimateRPA](https://www.ultimaterpa.com). 
You need to have the [UltimateRPA Tools](https://www.ultimaterpa.com/documentation/_install.html) installed.
Urpaform allows you to 
- distinguish between several forms in your robotization, 
- assign form fields of various types to a specific form,
- maintain the form fields.


## Examples 

### Basic usage - Form with a simple Editbox

The name given to the form appears in logs. A form field type is specified 
as EditElement, added to a form, assigned with the desired value to be filled in 
and finally, the form is completed.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element)
test_form = Form("my forms's name")
test_form.add(edit_field, "UltimateRPA")
test_form.complete()
```


### Options for Logging and Checks.

For several form field types, you can determine whether the filled values 
appear in logs. You can also control whether the check of desired value and truly filled 
in value will be performed. 

```python
from urpaform import Form, ComboElement

app = urpa.exec_app("Some_application.exe")
combo_element = app.find_first(cf.name("Usual").combo_box())
combo_field = ComboElement(combo_element, show_in_log=True, allow_check=False)
test_form = Form("my forms's name")
test_form.add(combo_field, "Saturday")
test_form.complete()
```


### Setting specific behavior of elements - Comboboxes.

Based on specific behavior of the Combobox in your form, you can choose the method 
to fill in your desired value. Many would accept the desired value as a text. For others,
you may need to activate the walk_type to walk through all available values in the 
Combobox to find the desired one.

It is recommended to use the default method and to use the other method only if the 
default method fails to set the value in your Combobox.

```python
from urpaform import Form, ComboElement

app = urpa.exec_app("Some_application.exe")
first_combo_element = app.find_first(cf.name("Usual").combo_box())
first_combo_field = ComboElement(first_combo_element, walk_type=False)
test_form = Form("my forms's name")
test_form.add(usual_combo_field, "Tuesday")
second_combo_element = app.find_first(cf.name("Unusual").combo_box())
second_combo_field = ComboElement(second_combo_element, walk_type=True)
test_form.add(second_combo_field, "Saturday")
test_form.complete()
```


### Maintaining Checkboxes and Radiobuttons.

You can check and uncheck Checkboxes in your forms, as well as activate Radiobuttons.

```python
from urpaform import Form, CheckElement, RadioElement

app = urpa.exec_app("Some_application.exe")
test_form = Form("my forms's name")
first_check_element = app.find_first(cf.name("a)").check_box())
first_check_field = CheckElement(first_check_element)
test_form.add(first_check_field, True)
second_check_element = app.find_first(cf.name("b)").check_box())
second_check_field = CheckElement(second_check_element)
test_form.add(second_check_field, False)
radio_element = app.find_first(cf.name("2").radio_button())
radio_field = RadioElement(radio_element)
test_form.add(radio_field, True)
test_form.complete()
```

## Expected updates for later versions of urpaform

- Solution for adding multiple fields at a time to a form. At the moment, 
only a single field can be added at a time using `add()` method. 