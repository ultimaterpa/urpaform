# urpaform

Extension for filling in forms with [UltimateRPA](https://www.ultimaterpa.com).  
You need to have the [UltimateRPA Tools installed](https://www.ultimaterpa.com/documentation/_install.html).  
Urpaform allows you to   
- distinguish between several forms in your robotization, 
- assign form fields of various types to a specific form,
- maintain the form fields.


## Examples 

### Basic Usage - Form with a Simple Edit Box

The name given to the form appears in logs. A form field type is specified 
as EditElement, added to a form, assigned with the desired value to be filled in 
and finally, the form is completed.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element)
test_form = Form("my forms's name")
test_form.add_individual(edit_field, "UltimateRPA")
test_form.complete()
```
Alternatively, you can take advantage of a context manager to complete the form.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element)
with Form("my forms's name") as test_form:
      test_form.add_individual(edit_field, "UltimateRPA")
```

### Adding Multiple Fields

You can add multiple fields to your form one by one with the `add_individual()` method. Or you can also 
use the `add_multiple()` method. This time, pass a tuple of tuples with element and value for each of the 
elements you wish to add.

```python

from urpaform import Form, EditElement

def main():
    app = urpa.exec_app("Some_application.exe")
    first_edit_element = app.find_first(cf.name("Name").edit())
    first_edit_field = EditElement(first_edit_element)
    second_edit_element = app.find_first(cf.name("Surname").edit())
    second_edit_field = EditElement(second_edit_element)
    with Form("my forms's name") as test_form:
        test_form.add_multiple(
            (
                (first_edit_field, "John"),
                (second_edit_field, "Smith"),
            )
        )
```

### Options for Logging and Checks

For several form field types, you can determine whether the filled values 
appear in logs. You can also control whether the check of desired value and truly filled 
value will be performed. 

```python
from urpaform import Form, ComboElement

app = urpa.exec_app("Some_application.exe")
combo_element = app.find_first(cf.name("Usual").combo_box())
combo_field = ComboElement(combo_element, show_in_log=True, allow_check=False)
test_form = Form("my forms's name")
test_form.add_individual(combo_field, "Saturday")
test_form.complete()
```

### Maintaining a Password Box

Maintenance of a password box is similar to an edit box. However, the filled 
value in a password box cannot be checked. The password itself can be stored in 
Windows Credential Vault and retrieved with `urpa.get_password()`. More details 
in [Vault Tutorial and documentation](https://www.ultimaterpa.com/documentation/_vault.html).

```python
from urpaform import PasswordElement

app = urpa.exec_app("Some_application.exe")
password = urpa.get_password(system, user)
password_element = app.find_first(cf.name("Password").edit())
password_field = PasswordElement(password_element)
test_form = Form("my forms's name")
test_form.add_individual(password_field, password)
test_form.complete()
```

### Setting Specific Behavior of Elements - Edit Elements

When [inspecting](https://www.ultimaterpa.com/documentation/_search_elements.html) an edit element, you may discover, that it has some specific behavior.
- For some, the filled value is placed in value attribute, but for others in the name attribute.
You can control the respective set up with `value_in_name` parameter.
- Some can contain a default value that cannot be removed from the edit box. For example, 
predefined dots for a date. You can use the `default_value` parameter.
- Finally, you have an option to define your own combination of keys with `clear_keys` to clear 
the field, in case the default setting fails for your application.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element, value_in_name=True, default_value="  .  .    ")
test_form = Form("my forms's name")
test_form.add_individual(edit_field, "UltimateRPA")
test_form.complete()
```


### Setting Specific Behavior of Elements - Combo Boxes

Based on specific behavior of the combo box in your form, you can choose the method 
to fill in your desired value. Many would accept the desired value as a text. For others,
you may need to activate the `walk_type` to walk through all available values in the 
combo box to find the desired one.

It is recommended to use the default method and to use the other method only if the 
default method fails to set the value in your combo box.

```python
from urpaform import Form, ComboElement

app = urpa.exec_app("Some_application.exe")
first_combo_element = app.find_first(cf.name("Usual").combo_box())
first_combo_field = ComboElement(first_combo_element, walk_type=False)
test_form = Form("my forms's name")
test_form.add_individual(first_combo_field, "Tuesday")
second_combo_element = app.find_first(cf.name("Unusual").combo_box())
second_combo_field = ComboElement(second_combo_element, walk_type=True)
test_form.add_individual(second_combo_field, "Saturday")
test_form.complete()
```


###  Maintaining Check Boxes and Radio Buttons

You can check and uncheck check boxes in your forms, as well as activate radio buttons.

```python
from urpaform import Form, CheckElement, RadioElement

app = urpa.exec_app("Some_application.exe")
test_form = Form("my forms's name")
first_check_element = app.find_first(cf.name("a)").check_box())
first_check_field = CheckElement(first_check_element)
test_form.add_individual(first_check_field, True)
second_check_element = app.find_first(cf.name("b)").check_box())
second_check_field = CheckElement(second_check_element)
test_form.add_individual(second_check_field, False)
radio_element = app.find_first(cf.name("2").radio_button())
radio_field = RadioElement(radio_element)
test_form.add_individual(radio_field, True)
test_form.complete()
```

## Expected Updates for Later Versions of Urpaform

