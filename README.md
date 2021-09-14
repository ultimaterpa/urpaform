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
test_form.add(edit_field, "UltimateRPA")
test_form.complete()
```
Alternatively, you can take advantage of a context manager to complete the form.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element)
with Form("my forms's name") as test_form:
      test_form.add(edit_field, "UltimateRPA")
```

Note, that there are several ways to add one or many fields to your form using the `add()` method.  
You can add fields separately one by one by passing two parameters, where an element is followed by a value.  
Alternatively, you can add multiple fields at once by passing any number of tuples with elements and values for each field.

```python
# adding 1 field
test_form.add(some_edit_field, "some value")

# adding 2 fields as tuples
test_form.add((some_edit_field, "some value"), (another_field, "some value"))
```

If needed, Form can be initialized with custom values for arguments:
* `attempts`: how many times can be completion of the form attempted (default value is 3)
* `delay`: how many second should pass between filling of two fields (default value is 0)

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
test_form.add(combo_field, "Saturday")
test_form.complete()
```

### Maintaining a Password Box

Maintenance of a password box is similar to an edit box. You can even chose
between keyboard input and pasting just like in edit box. However, the filled 
value in a password box cannot be checked. The password itself can be stored in 
Windows Credential Vault and retrieved with `urpa.get_password()`. More details 
in [Vault Tutorial and documentation](https://www.ultimaterpa.com/documentation/_vault.html).  
There is optional argument 'clear_method', which can have values: 
- "keys" - set by default, value will be deleted with the keyboard shortcut "CTRL+A" + "DEL"
- "set_empty_string" - value inside the field will be changed to an empty string
- "no_clearing - nothing will happen, value will remain inside the field

```python
from urpaform import PasswordElement

app = urpa.exec_app("Some_application.exe")
password = urpa.get_password(system, user)
password_element = app.find_first(cf.name("Password").edit())
password_field = PasswordElement(password_element, clear_method="set_empty_string")
test_form = Form("my forms's name")
test_form.add(password_field, password)
test_form.complete()
```

### Setting Specific Behavior of Elements - Edit Elements

When [inspecting](https://www.ultimaterpa.com/documentation/_search_elements.html) an edit element, you may discover, that it has some specific behavior.
- For most, the filled value is placed in value property, but for others in the name property or even the text_value property.
You can control the respective set up with `value_is_in` parameter.
- Some can contain a default value that cannot be removed from the edit box. For example, 
predefined dots for a date. You can use the `default_value` parameter.
- The default `clear_method` is set to `keys` with an option to define your own combination of keys with `clear_keys` to clear the field (in case the default setting fails for your application). 
- Alternatively, you can overwrite `clear_method` with `set_value` to empty the field via MSAA interface.
- There are more ways to fill an edit box with a value. The default `send_method` is `writing` using keyboard input. You can switch to pasting the value into the field from clipboard by setting `send_method` to `pasting` and `paste_keys` at demanded paste shortcut (default CTRL+V).
And finally, you can overwrite the `send_method` with `set_value` to set the value of your object via MSAA interface.

```python

from urpaform import Form, EditElement

app = urpa.exec_app("Some_application.exe")
edit_element = app.find_first(cf.name("Username").edit())
edit_field = EditElement(edit_element, value_is_in="name", default_value="  .  .    ")
test_form = Form("my forms's name")
test_form.add(edit_field, "UltimateRPA")
test_form.complete()
```


### Setting Specific Behavior of Elements - Combo Boxes

Based on specific behavior of the combo box in your form, you can choose the method 
to fill in your desired value. Many would accept the desired value as a text. For others,
you have to change optional argument `set_method`.   
There are 3 options:
- "text" - set by default, value inside the combo box will be filled by writing a given text
- "walk" - value will be choosen by walking through all available values in the 
combo box to find the desired one
- "set_value" - whole text value will be set inside the combo box

It is recommended to use the default method and to use the other method only if the 
default method fails to set the value in your combo box.

```python
from urpaform import Form, ComboElement

app = urpa.exec_app("Some_application.exe")
first_combo_element = app.find_first(cf.name("Usual").combo_box())
first_combo_field = ComboElement(first_combo_element, set_method="walk")
test_form = Form("my forms's name")
test_form.add(first_combo_field, "Tuesday")
second_combo_element = app.find_first(cf.name("Unusual").combo_box())
second_combo_field = ComboElement(second_combo_element, set_method="set_value")
test_form.add(second_combo_field, "Saturday")
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
test_form.add(first_check_field, True)
second_check_element = app.find_first(cf.name("b)").check_box())
second_check_field = CheckElement(second_check_element)
test_form.add(second_check_field, False)
radio_element = app.find_first(cf.name("2").radio_button())
radio_field = RadioElement(radio_element)
test_form.add(radio_field, True)
test_form.complete()
```
