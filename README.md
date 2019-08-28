# urpaform

early alpha version

Extension for filling in forms with [UltimateRPA](https://www.ultimaterpa.com). 
Urpaform allows you to distinguish between several forms in your robotization, 
assign form fields of various types to a specific form and maintain those fields.


## Example - Basic usage - form with a simple Editbox

The name given to the form appears in logs. A form field type is specified 
as EditElement, added to a form, assigned with the desired value to be filled in 
and finally, the form is completed.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("RpaLoginTest.exe")
edit = app.find_first(cf.name("Username").edit())
edit_class = EditElement(edit)
form_app = Form("form app")
form_app.add(edit_class, "UltimateRPA")
form_app.complete()
```


## Example - Options for Logging and Checks.

For several form field types, you can determine whether the filled values 
appear in logs. You can also control whether the check of desired value and truly filled 
in value will be performed. 

```python
from urpaform import Form, ComboElement

def main():
    app = urpa.exec_app("RpaBehaviorTest.exe")
    usual_combo = app.find_first(cf.name("Usual").combo_box())
    usual_combo_class = ComboElement(usual_combo, show_in_log=True, allow_check=False)
    form_app = Form("form app")
    form_app.add(usual_combo_class, "Saturday")
    form_app.complete()
```


## Example - Setting specific behavior of elements - Comboboxes.

Based on specific behavior of the Combobox in your form, you can choose the method 
to fill in your desired value. Many would accept the desired value as a text. For others,
you may need to activate the walk_type to walk through all available values in the 
Combobox to find the desired one.

```python
from urpaform import Form, ComboElement

def main():
    app = urpa.exec_app("RpaBehaviorTest.exe")
    usual_combo = app.find_first(cf.name("Usual").combo_box())
    usual_combo_class = ComboElement(usual_combo, walk_type=False)
    form_app = Form("form app")
    form_app.add(usual_combo_class, "Tuesday")
    unusual_combo = app.find_first(cf.name("Unusual").combo_box())
    unusual_combo_class = ComboElement(unusual_combo, walk_type=True)
    form_app.add(unusual_combo_class, "Saturday")
    form_app.complete()
```


## Example - Maintaining Checkboxes and Radiobuttons.

```python
from urpaform import Form, CheckElement, RadioElement

def main():
    app = urpa.exec_app("RpaSwitchesTest.exe")
    form_app = Form("form app")
    check_a = app.find_first(cf.name("a)").check_box())
    check_a_class = CheckElement(check_a)
    form_app.add(check_a_class, True)
    check_b = app.find_first(cf.name("b)").check_box())
    check_b_class = CheckElement(check_b)
    form_app.add(check_b_class, False)
    radio = app.find_first(cf.name("2").radio_button())
    radio_class = RadioElement(radio)
    form_app.add(radio_class, True)
    form_app.complete()
```

## Expected updates for later versions of urpaform

- Solution for adding multiple fields at a time to a form. At the moment, 
only a single field can be added at a time using `add()` method. 