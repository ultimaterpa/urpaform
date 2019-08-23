# urpaform.

urpaform early alpha version

## Example

```python
from urpaform import Form, EditElement

app = urpa.exec_app("RpaLoginTest.exe")
edit = app.find_first(cf.name("Username").edit())
edit_class = EditElement(edit)
form_app = Form("form app")
form_app.add(edit_class, "UltimateRPA")
form_app.complete()
```
