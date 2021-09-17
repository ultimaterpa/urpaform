# minimal fake urpa used for monkeypatching


def condition_factory():
    pass


class App:
    pass


class Condition:
    pass


class AppElement:

    def value(self):
        pass

    def name(self):
        pass

    def text_value(self):
        pass

    def set_focus(self):
        pass

    def send_text(self, text):
        pass

    def send_key(self, text):
        pass

    def toggle_state(self):
        pass

    def send_mouse_click(self):
        pass

    def selected(self):
        return False
