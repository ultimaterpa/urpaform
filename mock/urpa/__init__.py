#!/usr/bin/env python
# -*- coding: utf-8 -*-

## @package urpa
# The urpa module can be used for process automation.
#
# Multithreading
# --------------
# Calling from multiple threads is not supported.
#
# Output
# ------
# The print function prints information to the log and the standard output.
#
#

### Default timeout for all searches, see set_default_timeout
default_timeout = 5000

# Default parameters for text input
# see set_default_keyboard_layout
default_kl = "00000409"
# see set_default_text_action
default_text_action = "WM_CHAR"
default_char_delay = 50
default_decomposition_delay = 20

# see set_default_key_action
default_key_action = "Hardware"

# default parameters for mouse input
# see set_default_mouse_action
default_mouse_action = "HW Left"

default_focus_action = "Default"

class ElementNotFoundError(Exception):
    """ Exception raised when the required GUI element could not be found. """
    pass

def set_password(system, user, password):
    """ The "Windows Credential Vault", separate for each user profile, is used to store
    login details.
    Records can be user-managed with Credential Manager, a standard tool where the general
    credential name, the username and then the password are entered. """
    pass

def get_password(system, user):
    """ The "Windows Credential Vault", separate for each user profile, is used to store
    login details.
    Records can be user-managed with Credential Manager, a standard tool where the general
    credential name, the username and then the password are entered. """
    pass

def set_debug_mode(debug_mode, sleep_time=None):
    """ If enabled, it highlights the elements found and also waits for a certain time after an element has been found.

    Kwargs:
        debug_mode: Boolean
            True to enable debug mode, False otherwise

        sleep_time: int [ms]
            Time in ms to wait after an element has been found and highlighted.
    """
    pass

def set_default_timeout(timeout):
    """ Defines the default timeout for all element searches.

    Kwargs:
        timeout: int [ms]
    """
    global default_timeout
    default_timeout = timeout

def set_default_text_action(type, char_delay=None, decomposition_delay=None):
    """ Defines the default text action type and, optionally, the inter-character delay while simulating the text typing. See send_text function notes for more details.

    For *_Scan_Virtual types, the keyboard layout must be configured correctly, see set_default_keyboard_layout.
    For *_Alt_code types, HKEY_CURRENT_USER\\Control Panel\\Input Method needs to have EnableHexNumpad enabled in the registers.

    Kwargs:
        type: String The mode for the simulation of individual keystrokes, represented by a string in the "text" parameter in the send_text function.
            * HW_Alt_code
            * HW_Scan_Virtual
            * Standard_Alt_code
            * Standard_Scan_Virtual
            * WM_CHAR

        char_delay: int [ms]
            Inter-character delay in ms.
        decomposition_delay: int [ms]
            Character delay in ms.
    """
    pass

def set_default_mouse_action(type):
    """ This method defines the default mouse action type.

    Kwargs:
        type: String
            * HW Left
            * HW Right
            * HW Middle
            * HW Move
            * HW Left Down
            * HW Right Down
            * HW Middle Down
            * HW Left Up
            * HW Right Up
            * HW Middle Up
            * Left
            * Right
            * Middle
            * Left Down
            * Right Down
            * Middle Down
            * Left Up
            * Right Up
            * Middle Up
    """
    pass

def set_default_focus_action(type):
    """ Sets the default action type for invoking AppElement.set_focus.
    The setting also affects the send_text and send_key methods, where the set_focus method is invoked automatically before simulating key presses.

    Kwargs:
        type: String
            * Default - when a hidden desktop is used, this method takes a "long" time (2s)
            * Mouse - the element is enabled with a mouse click
            * None - the element will not be enabled
    """
    global default_focus_action
    default_focus_action = type

def set_default_key_action(type):
    """ Sets the default action type for send_key.

    Kwargs:
        type: String The way in which the keystrokes are to be simulated.
            * Hardware
            * Standard
    """
    pass

def set_default_keyboard_layout(kl):
    """ Sets the default keyboard layout for word processing.
    It only affects writing with *_Scan_Virtual types.

    Kwargs:
        kl: String Keyboard layout
            * 00000405 - Czech (Czech, CSY, Czech Republic)
            * 00000409 - English (US, ENU, United States)
            * 0000041B - Slovak (Slovak, SKY, Slovakia)
    """
    pass

def set_default_search_method(method):
    """ Sets the default search type for methods find_first, find_all.
    Kwargs:
        method: String
            * default
            * tree_walk
    """
    pass

def condition_factory():
    """ Auxiliary class for entering more complex search conditions, see ConditionFactory

    Returns:
        ConditionFactory
    """
    return ConditionFactory()

def transformation_factory():
    """ An auxiliary class that defines how images are to be transformed viz TransformationFactory

    Returns:
        TransformationFactory
    """
    return TransformationFactory()

def exec_app(cmd_line, show_window=None):
    """ Runs a general application, see the App class.

    Kwargs:
        cmd_line: String

        show_window: String
            * Minimize
            * Maximize
            * Normal
            * Hide

    Returns:
        App
    """
    return App()

def exec_excel_app(filename=None):
    """ Runs Excel. The path to the binary is detected automatically.

    Kwargs:
        filename: String Optional argument to specify which Excel file to open.

    Returns:
        AppExcel
    """
    return AppExcel()

def exec_ie_app(url=None):
    """ Runs Internet Explorer and goes to the URL passed. The path to the binary is detected automatically.

    Kwargs:
        url: String Optional argument to specify which URL to navigate to.

    Returns:
        AppIE
    """
    return AppIE()

def open_app(pid):
    """ Opens the application with the process ID (PID) entered. Raises an exception
    if the process with the ID passed does not exist or cannot be opened.

    Kwargs:
        pid: int The application process ID.

    Returns:
        App

    Raises:
        ElementNotFoundError:
    """
    return App()

def find_first_app(name, timeout=default_timeout):
    """ Finds the running application according to the name parameter passed.
    Finding already running applications makes it possible to work with applications that are not run via urpa.exec_*.

    Raises the urpa.ElementNotFoundError exception if the application could not be found within the timeout period.

    Kwargs:
        name: String The exact title name of the TP window or the ClassName of the TP window tied to an instance of the class returned.
        timeout: int [ms] The maximum time in which a TP window meeting the name condition must be retrieved. If this parameter is not entered, the default value is used, see urpa.default_timeout.

    Returns:
        App

    Raises:
        ElementNotFoundError: the application required could not be found within the timeout period.

    Examples:
        Open the notepad application. Then after some time, search for application with \"pad\" in the name.".

        app = urpa.exec_app("notepad.exe")
        .
        .
        urpa.find_first_app(cf.regexp("pad"))

    """
    return App()

def find_first_excel_app(timeout=default_timeout):
    """ Finds the already running Excel application.
    Finding an already running Excel application makes it possible to work with Excel that is not run via urpa.exec_excel_app.

    Raises the urpa.ElementNotFoundError exception if the application could not be found within the timeout period.

    Kwargs:
        timeout: int [ms] Maximum time to find Excel application.
        If this parameter is not passed, the default value is applied, see urpa.default_timeout.

    Returns:
        AppExcel

    Raises:
        ElementNotFoundError: the application required could not be found within the timeout period.

    """
    return AppExcel()

def find_first_ie_app():
    """ Finds already running Internet Explorer application.

    Returns:
        AppIE
    """
    return AppIE()

def bring_to_foreground(foreground=True):
    """ Switches the simulation to the foreground/background.

    Kwargs:
        foreground: bool
            True to switch simulation to the foreground or switch to the simulation desktop.
            False to switch simulation back to the background.
    """
    pass

def default_error_processing():
    """ Executes default exception processing: i.e. executes a screenshot and an error log in relation to the last exception raised. """
    pass

def check_screen_resolution(width, height, bits_per_pixel=None):
    """ Executes a resolution and color depth check.

    Kwargs:
        width: int
        height: int
        bits_per_pixel: int

    Raises:
        ValueError: if the resolution/color depth does not match
    """
    pass

def set_screen_resolution(width, height, bits_per_pixel=None):
    """ Sets resolution and color depth of default display device.

    Kwargs:
        width: int
        height: int
        bits_per_pixel: int

    """
    pass

def set_clipboard_text(text):
    """ Inserts the text passed into the Windows clipboard. """
    pass

def clipboard_text():
    """ Returns text stored in the Windows clipboard. """
    pass

def write_sydesk_measure(directory, source_id, value, expiration, description=None):
    """ It writes measurements in msr6 format to the directory passed.
    The start of the measurement is the current time.

    Kwargs:
        directory: String
            The directory to which the data record is to be written.
        source_id: String
            Data source ID in SyDesk.
        value: float or None
            Measure value. None means monitor failure.
        expiration: int
            Measurement validity in seconds.
        description: String
            Optional measurement caption.
    """
    pass

def write_measure(name, status, value=None, unit=None, tolerance=0, description=None, precision=None, id=None):
    """ It writes measurements to the directory passed.
    The start of the measurement is the current time.

    Kwargs:
        name: String
        status: String (SUCCESS|WARNING|ERROR|INFO|NONE)
        value: float
            Measure value.
        unit: String
            Measurement value unit, e.g. %.
        tolerance: float [h]
        description: String
            Optional measurement caption.
        precision: int
        id: String
            Optional measurement ID. If none is entered, this is taken to be the argument name ID.
    """
    pass

def take_screenshot():
    pass

def clear_uia():
    pass

class Config:
    timeout = 5000
    screenshot_format = "bmp"

    kl = "00000409"
    text_action = "WM_CHAR"
    char_delay = 50
    decomposition_delay = 20
    key_action = "Hardware"
    mouse_action = "HW Left"
    focus_action = "Default"

    def set_screenshot_name(self, name, timestamp=True, format="png"):
        pass

default = Config()


class App:
    """ A class representing a general application.
    For GUI element searches, the default setting is the UI Automation interface; for a user interaction simulation, HW actions are the default setting.
    GUI element searches encompass all "visible" TP windows tied to the process of the running application using the "full search" method.
    If an application (process) runs another application, you need to create a new instance of the App class to correctly search for GUI elements in the new application, e.g. by using the urpa.find_first_app method.

    Notes:
     * GUI element searches are faster if they are sufficiently identified by an exact match.

    """

    def find_first(self, condition, timeout=default_timeout):
        """ This method returns the application's first GUI element that meets the conditions defined in the condition parameter. This method is most often used to validate the correct GUI status of the controlled application after a previous user interaction  to find a GUI element over which user interaction is to be simulated.

        Technically, GUI element searches take place over two stages. In the first stage, all TP windows over a process tied to the App class are retrieved.
        GUI elements are then searched for in these "visible" windows according to the condition defined in the condition parameter. GUI element searches take place in iterations with a 50 ms delay.  The "depth-first search" method is used to search a GUI element tree. For applications with a large GUI, the processing time per iteration may be in the order of seconds.
        This method is not practical for identifying GUI elements that only "flash" in the GUI of the controlled application.
        When identifying GUI elements over applications that create subprocesses, you must verify the linkage between the process and the TP window, or the correct identification of the (sub)process that is tied to an instance of the App class.

        If the method could not find any matching GUI element, it raises the urpa.ElementNotFoundError exception.
        Otherwise, the method returns the first matching GUI element, even if multiple GUI elements meet the condition defined in the condition parameter.

        Kwargs:
            condition: String or Condition
                GUI element search term.
            timeout: int [ms]
                Maximum time to retrieve a GUI element. If this parameter is not entered, the default value is applied, i.e. urpa.default_timeout.

        Returns:
            Returns an AppElement-type object

        Raises:
            ElementNotFoundError: the GUI element required could not be found within the timeout period.

        Examples:
            The example of opening https://playground.ultimaterpa.com in Internet Explorer, finding an "authentication" GUI element called "Continue".

            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            verify_element = app.find_first("Continue")

        """
        return AppElement()

    def find_all(self, condition, elements=0, timeout=default_timeout):
        """ This method returns a list of all GUI elements meeting the condition parameter.

        The method searches, in iterations with a 50 ms delay, for all GUI elements in all "visible" TP windows tied to an instance of the App class, or to an App class process meeting the condition parameter. In each iteration, the complete GUI element trees created from all TP windows are searched. For applications with a large GUI, the processing time per iteration may be in the order of seconds.
        If the number of GUI elements found during a single iteration is non-zero and at the same time equal to or greater than the value specified in the elements parameter, the method returns a list of the AppElement objects found.
        If the elements parameter is set to 0 and at least one of the required GUI elements is not found by the timeout, the method returns an empty list.
        If the elements parameter is set to greater than 0 and the required number of GUI elements is not found by the timeout, the urpa.ElementNotFoundError exception is raised.
        This method does not work on the "counter" principle, and cannot be used to "dynamically" display GUI elements, or cannot be used if the individual GUI elements searched for are displayed only "temporarily" in sequential order.
        If the elements parameter is set to 0, only one iteration is processed.

        Kwargs:
            condition: String or Condition
                GUI element search term.
            elements: int
                The minimum number of GUI elements that must be found within the period defined in the timeout parameter.
            timeout: int [ms]
                Maximum time to retrieve a GUI element. If this parameter is not entered, the default value is applied, i.e. urpa.default_timeout.

        Returns:
            Returns a list of AppElement-type objects

        Raises:
            ElementNotFoundError: the required number of GUI elements could not be found within the timeout period.

        Examples:
            The example of finding at least two radio_buttons at https://playground.ultimaterpa.com in Internet Explorer within 1,000 ms and listing the attributes of the GUI elements found in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the Continue GUI element
            verify_element = app.find_first("Continue")
            # find at least two radio_button-type GUI elements
            elements = app.find_all(cf.radio_button(), 2, 1000)
            # list attributes of the GUI elements found
            print(elements)
        """
        pass

    def find_first_right_to(self, condition_reference_element, condition_right_element, timeout=default_timeout, height=50, step=30):
        """ This method looks for a GUI element matching the condition_right_element parameter and located to the right of the reference GUI element matching the condition_reference_element parameter.

        Searches for GUI elements (both "reference" and "right") take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The two GUI elements to be found ("reference" and "right") must appear at the same time in the same TP window.
        In the first stage of each iteration, the GUI element is initially searched according to the condition_reference_element term (the App.find_first method is used internally to find this GUI element).
        Once this reference GUI element is found, the TP window tied to it is transferred to the foreground.
        The height and step parameters are then used to calculate, over the TP window, the coordinates of the virtual points in which a GUI element matching the condition_right_element parameter is to be found.
        The virtual points over which a GUI element matching the condition_right_element parameter is to be searched have a horizontal spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window and the step parameter. Specifically, the x-coordinate of each virtual point must be less than the x-coordinate of the right edge of the TP window tied to the GUI elements to be searched for. At the same time, the x-coordinate of each virtual point must be greater than the x-coordinate of the right edge of the reference GUI element. The first virtual point always has an x-coordinate offset by 5 pixels to the right of the right edge of the reference GUI element.
        The vertical (y-) coordinate of all virtual points is set to the center of the reference GUI element (height = 50) by default and is always the same for all virtual points.
        If GUI elements over a large number of virtual points match the condition_right_element parameter at the same time, the GUI element closest to the reference GUI element is returned.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        @image html RightTo.png

        Kwargs:
            condition_reference_element: String or Condition
                Reference GUI element search term.
            condition_right_element: String or Condition
                The search term for the GUI element located to the right of the reference GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition_right_element parameter must be retrieved. If this parameter is not entered, the default value is applied, see urpa.default_timeout.
            height: int [%]
                Expresses, as a percentage, the offset of the vertical coordinate of all virtual points over the TP window from the top edge of the reference GUI element. The height of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the horizontal spacing - over the TP window - of virtual points in which a GUI element matching the condition_right_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.

        Examples:
            The example of finding the nearest text to the right of the "Normal" radio button at https://playground.ultimaterpa.com in Internet Explorer. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - "Normal" radio button and find the closest text to the right of this GUI element
            found_element = app.find_first_right_to(cf.radio_button().name("Normal"),cf.text())
            # list attributes of the GUI element found
            print(found_element)
        """
        return AppElement()

    def find_first_left_to(self, condition_reference_element, condition_left_element, timeout=default_timeout, height=50, step=30):
        """ This method looks for a GUI element matching the condition_left_element parameter and located to the left of the reference GUI element matching the condition_reference_element parameter.

        Searches for GUI elements (both "reference" and "left") take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The two GUI elements to be found ("reference" and "left") must appear at the same time in the same TP window.
        In the first stage of each iteration, the GUI element is initially searched according to the condition_reference_element condition (the App.find_first method is used internally to find this GUI element).
        Once this reference GUI element is found, the TP window tied to it is transferred to the foreground.
        The height and step parameters are then used to calculate, over the TP window, the coordinates of the virtual points in which a GUI element matching the condition_left_element parameter is to be found.
        The virtual points over which a GUI element matching the condition_left_element parameter is to be found have a horizontal spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window and the step parameter. Specifically, the x-coordinate of each virtual point must be greater than the x-coordinate of the left edge of the TP window tied to the GUI elements to be searched for. At the same time, the x-coordinate of each virtual point must be less than the x-coordinate of the left edge of the reference GUI element. The first virtual point always has an x-coordinate offset by 5 pixels to the left of the left edge of the reference GUI element.
        The vertical (y-) coordinate of all virtual points is set to the center of the reference GUI element (height = 50) by default and is always the same for all virtual points.
        If GUI elements over a large number of virtual points meet the condition_left_element parameter at the same time, the GUI element furthest from the reference GUI element is returned, unless a GUI element is found over the first virtual point 5 px away from the left edge of the reference GUI element - see the figure below.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        @image html LeftTo.png

        Kwargs:
            condition_reference_element: String or Condition
                Reference GUI element search term.
            condition_left_element: String or Condition
                The search term for the GUI element located to the left of the reference GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition_left_element parameter must be retrieved. If this parameter is not entered, the default value is applied, see urpa.default_timeout.
            height: int [%]
                Expresses, as a percentage, the offset of the vertical coordinate of all virtual points over the TP window from the top edge of the reference GUI element. The height of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the horizontal spacing - over the TP window - of virtual points in which a GUI element matching the condition_left_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.

        Examples:
            The example of finding a radio button to the left of the "Normal" text at https://playground.ultimaterpa.com in Internet Explorer. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - "normal" text and find a radio button to the left of this GUI element
            found_element = app.find_first_left_to(cf.text().name("Normal"),cf.radio_button())
            # list attributes of the GUI element found
            print(found_element)
        """
        return AppElement()

    def find_first_down_to(self, condition_reference_element, condition_down_element, timeout=default_timeout, width=50, step=30):
        """ This method looks for a GUI element matching the condition_down_element parameter and located down from the reference GUI element matching the condition_reference_element parameter.

        Searches for GUI elements (both "reference" and "down") take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The two GUI elements to be found ("reference" and "down") must appear at the same time in the same TP window.
        In the first stage of each iteration, the GUI element is initially searched according to the condition_reference_element term (the App.find_first method is used internally to find this GUI element).
        Once this reference GUI element is found, the TP window tied to it is transferred to the foreground.
        The width and step parameters are then used to calculate, over the TP window, the coordinates of the virtual points in which a GUI element matching the condition_down_element parameter is to be found.
        The virtual points over which a GUI element matching the condition_down_element parameter is to be found have a vertical spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window and the step parameter. Specifically, the y-coordinate of each virtual point must be less than the y-coordinate of the lower edge of the TP window tied to the GUI elements to be searched for. At the same time, the y-coordinate of each virtual point will be greater than the y-coordinate of the lower edge of the reference GUI element. The first virtual point always has a y-coordinate offset by 5 pixels down from the lower edge of the reference GUI element.
        The horizontal (x-) coordinate of all virtual points is set to the center of the reference GUI element (width = 50) by default and is always the same for all virtual points.
        If GUI elements over a large number of virtual points match the condition_down_element parameter at the same time, the GUI element closest to the reference GUI element is returned - see the figure below containing the order of virtual points.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        @image html DownTo.png

        Kwargs:
            condition_reference_element: String or Condition
                Reference GUI element search term.
            condition_down_element: String or Condition
                The search term for the GUI element located below the reference GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition_down_element parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            width: int [%]
                Expresses, as a percentage, the offset of the horizontal coordinate of all virtual points over the TP window from the left edge of the reference GUI element. The width of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the vertical spacing - over the TP window - of virtual points in which a GUI element matching the condition_down_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.

        Examples:
            The example of finding a button below the "Normal" text at https://playground.ultimaterpa.com in Internet Explorer. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - "Normal" text and find the closest button below this GUI element
            found_element = app.find_first_down_to(cf.text().name("Normal"),cf.button())
            # list attributes of the GUI element found
            print(found_element)
        """
        return AppElement()

    def find_first_up_to(self, condition_reference_element, condition_up_element, timeout=default_timeout, width=50, step=30):
        """ This method looks for a GUI element matching the condition_up_element parameter and located above the reference GUI element matching the condition_reference_element parameter.

        Searches for GUI elements (both "reference" and "up") take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The two GUI elements to be found ("reference" and "up") must appear at the same time in the same TP window.
        In the first stage of each iteration, the GUI element is initially found according to the condition_reference_element term (the App.find_first method is used internally to find this GUI element).
        Once this reference GUI element is found, the TP window tied to it is transferred to the foreground.
        The width and step parameters are then used to calculate, over the TP window, the coordinates of the virtual points in which a GUI element matching the condition_up_element parameter is to be found.
        The virtual points over which a GUI element matching the condition_up_element parameter is to be found have a vertical spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window and the step parameter. Specifically, the y-coordinate of each virtual point must be greater than the y-coordinate of the upper edge of the TP window tied to the GUI elements to be found. At the same time, the y-coordinate of each virtual point will be less than the y-coordinate of the upper edge of the reference GUI element. The first virtual point always has a y-coordinate offset by 5 pixels above the upper edge of the reference GUI element.
        The horizontal (x-) coordinate of all virtual points is set to the center of the reference GUI element (width = 50) by default and is always the same for all virtual points.
        If GUI elements over a large number of virtual points match the condition_up_element parameter at the same time, the GUI element farthest from the reference GUI element is returned, unless a GUI element is found over the first virtual point 5 px away from the upper edge of the reference GUI element - see the figure below.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        @image html UpTo.png

        Kwargs:
            condition_reference_element: String or Condition
                Reference GUI element search term.
            condition_up_element: String or Condition
                The search term for the GUI element located above the reference GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition_up_element parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            width: int [%]
                Expresses, as a percentage, the offset of the horizontal coordinate of all virtual points over the TP window from the left edge of the reference GUI element. The width of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the vertical spacing - over the TP window - of virtual points in which a GUI element matching the condition_up_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.

        Examples:
            The example of finding a text above the "Continue" button at https://playground.ultimaterpa.com in Internet Explorer. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - "Continue" button and find a text from this GUI element
            found_element = app.find_first_up_to(cf.button().name("Continue"),cf.text())
            # list attributes of the GUI element found
            print(found_element)
        """
        return AppElement()

    def find_from_point(self, condition_reference_element, condition, x, y, timeout=default_timeout):
        """ This method looks for a GUI element matching the condition parameter and located in the position of the virtual point defined by offsetting (via the parameters x, y) the upper left corner of a GUI element matching the condition_reference_element parameter.

        Searches for GUI elements take place in iterations with a 50 ms delay over the time specified in the timeout parameter. In the first stage of each iteration, the reference GUI element is initially found according to the condition defined in the condition_reference_element parameter (the App.find_first method is used internally). Once the reference GUI element is found, the TP window tied to it is transferred to the foreground.
        The coordinates of the virtual point over which the GUI element is to be found according to the condition parameter are then calculated by offsetting the absolute coordinates of the reference GUI element by x, y that are passed as parameters. If the GUI element over the virtual point matches the condition parameter, it is returned by this method. The two GUI elements to be found ("reference" and "condition") must appear at the same time in the same TP window.
        If the method could not find any matching GUI element, it raises the urpa.ElementNotFoundError exception.

        @image html FromPoint.png

        Kwargs:
            condition_reference_element: String or Condition
                Reference GUI element search term.
            condition: String or Condition
                Main GUI element search term.
            x: int [px]
                The coordinates specifying the horizontal offset, specifically the coordinates defining the virtual point's relative x-axis position on which the GUI element matching the condition parameter must be located.
            y: int [px]
                The coordinates specifying the vertical offset, specifically the coordinates defining the virtual point's relative y-axis position on which the GUI element matching the condition parameter must be located.
            timeout: int [ms]
                The maximum search time for the main GUI element. If no parameter is passed, the default urpa.default_timeout value is used.

        Returns:
            Returns an AppElement-type object.

        Raises:
            ElementNotFoundError: the GUI element required could not be found within the timeout period.

        Examples:
            The example of finding an image located at https://playground.ultimaterpa.com in Internet Explorer 0 pixels right of and 60 pixels above the upper left corner of the GUI element representing the "Normal" text. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - "Normal" text and find an image - GUI element in the position specified by offsetting (0,-60) the upper left corner of the GUI element - "Normal" text
            found_element = app.find_from_point(cf.text().name("Normal"),cf.image(),0, -60)
            # list attributes of the GUI element found
            print(found_element)
        """
        return AppElement()

    def close(self, timeout=600):
        """ This method closes the application tied to the App class process.

        This method first searches for all TP windows tied to instances of this class, specifically to the process representing the application. The method then sends the system message WM_CLOSE to all of the TP windows found.
        In the second processing stage, the method waits to determine whether the process will end within the time defined in the timeout parameter. If a process does not end within the timeout period, it will be killed.
        When the simulation ends, the method is invoked automatically over all instances of the App class that have the automatic process closure flag set - see the App.set_auto_close method.

        Kwargs:
            timeout: int [ms] Maximum time given for the standard termination of the application tied to the class process.

        Examples:
            The example of finding Internet Explorer already running and forcing its closure.

            appIE = urpa.find_first_ie_app()
            appIE.close()
        """
        pass

    def set_auto_close(self, auto_close):
        """ This method sets the internal App class flag, according to which the automatic (non-)closure of a process tied to an instance of the App class is controlled at the end of the simulation.

        By default, this internal flag value is set to True for App class instances (AppIE, AppExcel) created using the urpa.exec_app, urpa.exec_excel_app, or urpa.exec_ie_app methods, and set to False for App class instances (AppIE, AppExcel) created using the urpa.find_first_app, urpa.find_first_excel_app, or urpa.find_first_ie_app methods.

        Kwargs:
            auto_close: boolean The setting of a new value for the internal class flag that controls the automatic (non-)closure of a process tied to an instance of the class.

        Examples:
            The example of finding Internet Explorer already running and its automatic closure when the script ends.

            appIE = urpa.find_first_ie_app()
            appIE.set_auto_close(True)
        """
        pass

    def resize_tp_window(self, condition, rect, timeout=default_timeout):
        """ This method changes the position and size of a TP window associated with a GUI element matching the condition parameter.

        In the first processing stage, this method searches for a GUI element that matches the condition parameter with the internal use of the method - see App.find_first. The GUI element found is then used to identify the TP window that is tied to it, and to resize it according to the rect parameter.


        Kwargs:
            condition: String or Condition. The condition for finding a TP window, or any GUI element found in a TP window.

            rect: a tuple with 4 int-type elements (left, top, right, bottom). It defines the new absolute position of a TP window found on the current desktop.

            timeout: int [ms]. Maximum possible time to identify a TP window. If this parameter is not passed, the default value is used - see urpa.default_timeout.

        Examples:
            The example of opening Internet Explorer and resizing its TP window.

            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            newPos = (1, 1, 500, 500)
            # wait for the page to load correctly and identify the TP window according to the "Continue" button, resize the TP window found
            app.resize_tp_window("Continue",newPos)
        """
        pass

    def process_id(self):
        """ This method returns the ID of a process tied to an instance of the App class.

        Returns:
            Returns a (int) number containing the ID of a process tied to an instance of the App class.

        Examples:
            The example of finding Internet Explorer already running and listing its process ID.

            appIE = urpa.find_first_ie_app()
            print(appIE.process_id())
        """
        return 9090

    def process_name(self):
        """ This method returns the name of a process tied to an instance of the App class.

        Returns:
            Returns a string containing the name of a process tied to an instance of the App class.

        Examples:
            The example of finding Internet Explorer already running and listing its process name.

            appIE = urpa.find_first_ie_app()
            print(appIE.process_name())
        """
        return "iexplore.exe"

class AppElement:
    """ This class represents the GUI element in an application.
    An instance of this class can be created by one of the App class methods or by the AppElement.find_first, AppElement.find_all, AppElement.find_from_point, and AppElement.find_first_right_to methods.

    """

    def send_mouse_click(self, action=default_mouse_action, position=None):
        """ This method simulates the mouse action specified in its parameter, on the center of the App GUI element.
        By default, this method makes an HW left mouse click in the center of the GUI element. Delays in sending individual messages that simulate the mouse action are set to 50 ms.

        Kwargs:
            action: String A parameter specifying the type of mouse action that will be simulated over the GUI element. For possible parameter values, see the urpa.set_default_mouse_action method.
            position: An optional tuple with 2 int-type elements (left, top). Specifies the mouse click position in the format left, top.
            The coordinates are relative to the upper left corner of the element.

        Examples:
        The example of opening https://playground.ultimaterpa.com in Internet Explorer, finding an "authentication" GUI element called "Continue" and waiting for 3 seconds, simulating a click on the "Continue" GUI element found, finding the "Success" authentication element.

            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            verify_element = app.find_first("Continue")
            time.sleep(3)
            verify_element.send_mouse_click("Left")
            verify_element_success = app.find_first("Success")
        """
        pass

    def send_text(self, text, action=default_text_action, kl=default_kl, focus_action=default_focus_action):
        """ This method simulates text input - over a GUI element - the pressing and releasing of a key sequence, represented by a string in the "text" parameter.
        Prior to simulating the key press and release, the TP window tied to the GUI element is transferred to the foreground, and the set_focus() method is automatically invoked over the GUI element tied to an instance of that class.
        The actual key press/release simulation is only tied to the TP window handle, i.e. if the GUI element does not gain or loses focus during the simulation, the simulation will not be executed correctly.
        While simulating the key press and release, first the string from the "text" parameter is divided into individual characters. A sequence is then created that represents key press ("down")and key release ("up") according to the characters in the "text" parameter.
        For example, the string "Lev" is broken down into the sequence Shift(Down)+l(Down)+l(Up)+Shift(Up)+e(Down)+e(Up)+v(Down)+v(Up). A 100 ms delay is "processed" following the simulation of the press (Down) / release (Up) of each key.
        If one of the "hw" simulation modes is set in the "type" parameter, the simulation must take place in the foreground. If a simulation is running in the background, when the "type" parameter is set to one of the "hw" values it is automatically transferred to the foreground. When the "type" parameter is set to one of the "standard" values, during a simulation individual characters are converted into virtual-key codes or alt-codes, and the simulation can also run in the background. When the "type" parameter is set to "wm_char", the string from the "text" parameter splits directly into individual characters during the simulation.

        Kwargs:
            text: String Text, the writing of which will be simulated over an application tied to a GUI element represented by an instance of this class.

            action: String The mode for the simulation of individual keystrokes, represented by a string in the "text" parameter.
                * "hw_alt_code" This option uses the classic decomposition of text characters into Alt-code and their sequential simulation. The Windows API keybd_event() function is invoked over an application tied to a GUI element during the simulation.
                * "hw_scan_virtual" This option draws on the decomposition of characters from the "text" parameter using *.xml conversion files from the KeybLayoutTranslate directory. If, for the "kl" parameter, a keyboard layout is set for which there is no KeybLayoutTranslate\00000*.xml file, this file needs to be created for that keyboard layout, otherwise the user activity simulation will not work correctly. The keybd_event() function is invoked when simulating the Windows API over an application tied to a GUI element.
                * "standard_alt_code" This option uses the classic decomposition of text characters into Alt-code and their sequential simulation. Messages with WM_KEYDOWN and WM_KEYUP parameters are sent to an application tied to a GUI element via the Windows API PostMessage() function.
                * "standard_scan_virtual" This option draws on the decomposition of characters from the "text" parameter using *.xml conversion files from the KeybLayoutTranslate directory. If, for the "kl" parameter, a keyboard layout is set for which there is no KeybLayoutTranslate\00000*.xml file, this file needs to be created for that keyboard layout, otherwise the user activity simulation will not work correctly. Messages with WM_KEYDOWN and WM_KEYUP parameters are sent to an application tied to a GUI element via the Windows API PostMessage() function.
                * "wm_char" This option is appropriate when the Keyboard Layout specification is unclear and when characters accessible with different keyboard contexts need to be transferred to an application. Setting this option results only in the direct splitting of the string from the "text" parameter in the simulation. The keyboard layout set in the "kl" parameter is ignored when this simulation mode is used.
            kl: String Represents the keyboard layout that is automatically set for an application tied to a GUI element when simulating text input.

            focus_action: String The way in which control activation is to be simulated.
                See set_default_focus_action for options.
        Raises:
            ValueError: one of the parameters transferred does not have a valid format.

        Examples:
            The example of opening Internet Explorer on the about:blank page, simulating the input of the text https://playground.ultimaterpa.com in the address bar, and going to this page by pressing the Enter key.

            app = urpa.exec_ie_app("about:blank")
            verify_element = app.find_first(cf.value("about:blank"))
            time.sleep(1)
            verify_element.send_text("https://playground.ultimaterpa.com")
            verify_element.send_key("ENTER")
            time.sleep(1)
            ready_element = app.find_first(cf.button().name("Continue"))
        """
        pass

    def send_key(self, text, type=default_key_action, focus_action=default_focus_action):
        """ This method simulates - over a GUI element - the pressing of a specified key combination.
        Prior to simulating the pressing of the specified key combination, the TP window tied to the GUI element is transferred to the foreground, and the set_focus() method is automatically invoked over the GUI element tied to an instance of that class.
        The actual simulation of the pressing of the specified key combination is only tied to the TP window handle, i.e. if the GUI element does not gain or loses focus during the simulation, the simulation will not be executed correctly.
        While simulating the key action,, first the string from the "text" parameter is divided into individual characters. The delimiter between characters is "+".
        A sequence is then created that represents key press ("down") and key release ("up") according to the characters in the "text" parameter. For example, the Ctrl+Shift+s combination is broken down into the sequence Ctrl(Down)+Shift(Down)+s(Down)+s(Up)+Shift(Up)+Ctrl(Up). A 100 ms delay is "processed" following the simulation of the press (Down) / release (Up) of each key.
        If a Hardware simulation mode is set in the "type" parameter, the simulation must take place in the foreground. If a simulation is running in the background, when the "type" parameter is set to Hardware it is automatically transferred to the foreground. When the "type" parameter is set to a Standard value, during a simulation individual characters are converted into virtual-key codes, and the simulation can also run in the background.
        This method is not suitable for direct text input.

        Kwargs:
            text: String A key combination, the pressing of which over a GUI element is to be simulated, e.g. ALT+x.
                * "ALT"
                * "RALT" - right Alt
                * "CTRL"
                * "RCTRL" - right Ctrl
                * "TAB"
                * "ENTER", "RETURN"
                * "BACKSPACE"
                * "ESC", "ESCAPE"
                * "PAUSE"
                * "END"
                * "HOME"
                * "LEFT"
                * "UP"
                * "RIGHT"
                * "DOWN"
                * "INSERT"
                * "DELETE", "DEL"
                * "HELP"
                * "NUMLOCK"
                * "SCROLL"
                * "PGDOWN", "NEXT"
                * "PGUP", "PRIOR"
                * "CLEAR"
                * "SHIFT"
                * "RSHIFT" - right shift
                * "WIN"
                * "RWIN"
                * "APPS"
                * "SPACE"
                * "MULTIPLY"
                * "ADD"
                * "SEPARATOR"
                * "SUBTRACT"
                * "DECIMAL"
                * "DIVIDE"
                * "OEM_MINUS"
                * "OEM_PLUS"
                * "OEM_COMMA"
                * "OEM_PERIOD"

            type: String The way in which the keystrokes are to be simulated.
                * Hardware
                * Standard

            focus_action: String The way in which control activation is to be simulated.
                See set_default_focus_action for options.

        Raises:
            ValueError: the "text" or "type" parameter passed does not have a valid format.

        Examples:
             The example of opening Internet Explorer on the about:blank page, invoking the "Show documents downloaded" dialogue box by simulating the Ctrl+J keyboard shortcut and closing this dialog box by simulating the Alt+Z keyboard shortcut.

            app = urpa.exec_ie_app("about:blank")
            verify_element = app.find_first(cf.value("about:blank"))
            time.sleep(1)
            verify_element.send_key("Ctrl+J")
            time.sleep(1)
            close_element = app.find_first(cf.button().access_key("Alt+Z"))
            time.sleep(1)
            close_element.send_key("Alt+Z")
        """
        pass

    def send_message(self, message, wparam = 0, lparam = 0):
        pass

    def post_message(self, message, wparam = 0, lparam = 0):
        pass

    def set_focus(self, focus_action=default_focus_action):
        """ This method sets the focus on this App GUI element.

        Kwargs:
            focus_action: String The way in which control activation is to be simulated.
                See set_default_focus_action for options.
        """
        pass

    def invoke(self):
        pass

    def set_value(self, value):
        pass

    def add_to_selection(self):
        pass

    def remove_from_selection(self):
        pass

    def select(self):
        pass

    def name(self):
        """ This method returns the value of the "name" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "name" attribute of this App GUI element.
        """
        return "název elementu"

    def value(self):
        """ This method returns the value of the "value" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "value" attribute of this App GUI element.
        """
        return "value elementu"

    def class_name(self):
        """ This method returns the value of the "class name" attribute of this App GUI element.
        Returns:
            Returns a string containing the value of the "class name" attribute of this App GUI element.
        """
        return "class name"

    def localized_control_type(self):
        """ This method returns the value of the "localized control type" attribute of this App GUI element.
        Returns:
            Returns a string containing the value of the "localized control type" attribute of this App GUI element.
        """
        return "tlačítko"

    def control_type(self):
        """ This method returns the value of the "control type" attribute of this App GUI element.
        Returns:
            Returns a string containing the value of the "control type" attribute of this App GUI element.
        """
        return "button"

    def bounding_rectangle(self):
        """ This method returns the absolute coordinates of this GUI element on the desktop in the order left, top, right, bottom.
        Returns:
            Returns a tuple containing the absolute coordinates of this GUI element on the desktop in the order left, top, right, bottom.
        """
        return (0, 0, 0, 0)

    def size(self):
        """ This method returns the size of this App GUI element in the order width, height.
        Returns:
            Returns a tuple containing the size of this App GUI element in the order width, height.
         """
        return (0, 0)

    def access_key(self):
        """ This method returns the value of the "access key" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "access key" attribute of this App GUI element.

        """
        return "Alt+B"

    def automation_id(self):
        """ This method returns the value of the "automation ID" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "automation ID" attribute of this App GUI element.
        """
        return "TitleBar"

    def item_type(self):
        """ This method returns the value of the "item type" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "item type" attribute of this App GUI element.

        """
        return "bunka"

    def toggle_state(self):
        """ This method returns the value of the "toggle state" attribute of this App GUI element.

        The "toggle state" attribute represents the most frequent checkbox check status.

        Returns:
            Returns True if the GUI element is "checked".
            Returns False if the GUI element is not "checked".
            Returns None if the GUI element has an indeterminate status or if it does not support this attribute.
        """
        return False

    def selected(self):
        """ This method returns the value of the "selected" attribute of this App GUI element.

        The "selected" attribute represents, for example, the status of "radio button" or "list item" control.

        Returns:
            Returns True if the GUI element is "selected".
            Returns False if the GUI element is not "selected".
            Returns None if the GUI element does not support this attribute.
        """
        return False

    def enabled(self):
        """ This method returns the value of the "enabled" attribute of this App GUI element.

        Returns:
            Returns True if the GUI element is "enabled".
            Returns False if the GUI element is not "enabled".
        """
        return False

    def visual_data(self, rect=None, format="bmp"):
        """ This method creates an image from this App GUI element.

        Kwargs:
            rect: a tuple with 4 int-type elements (left, top, right, bottom).
                Relative coordinates (relative to the upper left corner of the GUI element) to
                define the clipping. By default, the entire element clipping is used - see bounding_rectangle.
            format: String
                Determines the "bmp" or "png" data format.

        Returns:
            Returns the image in bmp format as a bytearray.

        Examples:
            The example of loading an image using the PIL module (https://python-pillow.org/):

            image_data = element_start.visual_data()
            image = Image.open(io.BytesIO(image_data))
            image.show()

        """
        return bytearray()

    def parent(self):
        """ This method returns the element parent. If there is no parent, it returns None. """
        return AppElement()

    def find_first(self, condition, timeout=default_timeout):
        """ This method returns the first GUI element that matches the condition parameter and is located in a GUI element subtree with a root representing this App GUI element.

        GUI element searches take place in iterations with a 50 ms delay. The "depth-first search" method is used to search a GUI element subtree. For applications with a large GUI, the processing time per iteration, or the search of a GUI element subtree, may be in the order of seconds.
        This method is not practical for identifying GUI elements that only "flash" in the GUI of the controlled application.
        If the method could not find any matching GUI element, it raises the urpa.ElementNotFoundError exception.
        Otherwise, the method returns the first matching GUI element, even if multiple GUI elements meet the condition defined in the condition parameter.

        Kwargs:
            condition: String or Condition
                GUI element search term.
            timeout: int [ms]
                Maximum time to retrieve a GUI element. If this parameter is not passed, the default value is applied, i.e. urpa.default_timeout.

        Returns:
            Returns an AppElement-type object

        Raises:
            ElementNotFoundError: the GUI element required could not be found within the timeout period.

        Examples:

            The example of finding the first radio button located at https://playground.ultimaterpa.com in Internet Explorer under the GUI element - the "UltimateRPA Playground" pane. The attributes of the GUI element found are listed in the output console.
            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - the "UltimateRPA Playground" pane
            root_element = app.find_first(cf.pane().name(cf.regexp("UltimateRPA Playground")))
            # find a radio button in the GUI element subtree
            found_element = root_element.find_first(cf.radio_button())
            print(found_element)
        """
        return AppElement()

    def find_all(self, condition, elements=0, timeout=default_timeout):
        """ This method returns a list of all GUI elements that match the condition parameter and are located in a GUI element subtree with a root representing this App GUI element.

        GUI element subtree searches take place in iterations with a 50 ms delay over the time defined in the timeout parameter. For applications with a large GUI, the processing time per iteration, or the search of a GUI element subtree, may be in the order of seconds.
        If the number of GUI elements found during a single iteration is non-zero and at the same time equal to or greater than the value specified in the elements parameter, the method returns a list of the AppElement objects found.
        If the elements parameter is set greater than 0 and the required number of GUI elements is not found by the timeout, the urpa.ElementNotFoundError exception is raised.
        If the elements parameter is set to 0 and at least one of the required GUI elements is not found by the timeout, the method returns an empty list.
        If the elements parameter is set to 0, only one iteration is processed.

        Kwargs:
            condition: String or Condition
                GUI element search term.
            elements: int
                The minimum number of GUI elements that must be found within the period defined in the timeout parameter.
            timeout: int [ms]
                Maximum time to retrieve a GUI element. If this parameter is not passed, the default value is applied, i.e. urpa.default_timeout.

        Returns:
            Returns a list of AppElement-type objects

        Raises:
            ElementNotFoundError: the required number of GUI elements could not be found within the timeout period.

        Examples:
            The example of finding all radio buttons located at https://playground.ultimaterpa.com in Internet Explorer under the GUI element - the "UltimateRPA Playground" pane. The attributes of the GUI elements found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - the "UltimateRPA Playground" pane
            root_element = app.find_first(cf.pane().name(cf.regexp("UltimateRPA Playground")))
            # find hyperlinks in the GUI element subtree
            found_elements = root_element.find_all(cf.radio_button())
            print(found_elements)
            """
        pass

    def find_from_point(self, x, y, condition=None, timeout=default_timeout):
        """ This method looks for a GUI element matching the condition parameter and located at a virtual point defined by offsetting (via the parameters x, y) the upper left corner of this App GUI element.

        GUI element searches take place in iterations with a 50 ms delay over the time specified in the timeout parameter. Prior to finding the element, the TP window tied to an instance of this class is brought to the foreground.
        The coordinates of the virtual point (over which the GUI element is to be found according to the condition parameter) are then calculated by offsetting the absolute coordinates of this GUI element by x, y that have been passed as parameters. If the GUI element over the virtual point meets the condition parameter, it is returned by this method. The two GUI elements, the reference and the one to be found, must appear at the same time in the same TP window.
        If the condition is None, only the first iteration is executed and the method returns a GUI element on the virtual point position.
        If the method could not find any matching GUI element, it raises the urpa.ElementNotFoundError exception.

        @image html FromPointElement.png

        Kwargs:
            x: int [px]
                The coordinates specifying the horizontal offset, specifically the coordinates defining the virtual point's relative x-axis position on which the GUI element matching the condition parameter must be located.
            y: int [px]
                The coordinates specifying the vertical offset, specifically the coordinates defining the virtual point's relative y-axis position on which the GUI element matching the condition parameter must be located.
            condition: String or Condition
                GUI element search term.
            timeout: int [ms]
                The maximum search time for a GUI element. If no parameter is passed, the default urpa.default_timeout value is used.

        Returns:
            Returns an AppElement-type object.

        Raises:
            ElementNotFoundError: the GUI element required could not be found within the timeout period.

        Examples:
            The example of finding an image located at https://playground.ultimaterpa.com in Internet Explorer 0 pixels right of and 60 pixels up from the upper left corner of the GUI element representing the "Normal" text. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - the "Normal" text
            found_element = app.find_first(cf.text().name("Normal"))
            # find the image - the GUI element in the position specified by offsetting (0,60) the upper left corner of the GUI element - "Normal" text
            point_element = found_element.find_from_point(0, -60, cf.image())
            # list attributes of the GUI element found
            print(point_element)
        """
        return AppElement()

    def find_first_right_to(self, condition, timeout=default_timeout, height=50, step=30):
        """
        This method looks for a GUI element matching the condition parameter and located to the right of this GUI element.

        GUI element searches take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The GUI element to be found must be available in the same TP window as the GUI element tied to an instance of this class.
        Prior to finding the element, the TP window is brought to the foreground.
        The coordinates of the virtual points in which a GUI element matching the condition parameter is to be found are then calculated over the TP window.
        The virtual points over which a GUI element matching the condition parameter is to be found have a horizontal spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window. Specifically, the x-coordinate of each virtual point must be less than the x-coordinate of the right edge of the TP window tied to the GUI element to be found. At the same time, the x-coordinate of each virtual point must be greater than the x-coordinate of the right edge of this GUI element. The first virtual point always has an x-coordinate offset by 5 pixels to the right of the right edge of this GUI element.
        The vertical (y-) coordinate of all virtual points is set to the center of this GUI element and is always the same for all virtual points.
        If GUI elements over a large number of virtual points match the condition parameter at the same time, the GUI element closest to this GUI element is returned.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        @image html RightToElement.png

        Kwargs:
            condition: String or Condition
                The search term for the GUI element located to the right of this App GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element meeting the condition parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            height: int [%]
                Expresses, as a percentage, the offset of the vertical coordinate of all virtual points over the TP window from the top edge of the reference GUI element. The height of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the horizontal spacing - over the TP window - of virtual points in which a GUI element matching the condition parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.

        Examples:
            The example of finding the nearest text to the right of the "Normal" radio button at https://playground.ultimaterpa.com in Internet Explorer. The attributes of the GUI element found are listed in the output console.

            # auxiliary class to create more complex conditions
            cf = urpa.condition_factory()
            # run Internet Explorer
            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            # wait to find the GUI element - the "Normal" radio button
            found_element = app.find_first(cf.radio_button().name("Normal"))
            # find the closest text to the right of the GUI element found_element
            right_element = found_element.find_first_right_to(cf.text())
            # list attributes of the GUI element found
            print(right_element)
        """
        return AppElement()

    def find_first_left_to(self, condition, timeout=default_timeout, height=50, step=30):
        """
        This method looks for a GUI element matching the condition parameter and located to the left of this GUI element.

        GUI element searches take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The GUI element to be found must occur in the same TP window as the GUI element tied to an instance of this class.
        Prior to finding the element, the TP window is brought to the foreground.
        The coordinates of the virtual points in which a GUI element matching the condition parameter is to be found are then calculated over the TP window.
        The virtual points over which a GUI element matching the condition parameter is to be found have a horizontal spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window. Specifically, the x-coordinate of each virtual point must be less than the x-coordinate of the right edge of the TP window tied to the GUI element to be found. At the same time, the x-coordinate of each virtual point must be less than the x-coordinate of the right edge of this GUI element. The first virtual point always has an x-coordinate offset by 5 pixels to the left of the right edge of this GUI element.
        The vertical (y-) coordinate of all virtual points is set to the center of this GUI element and is always the same for all virtual points.
        If GUI elements over a large number of virtual points match the condition parameter at the same time, the GUI element closest to this GUI element is returned.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        Kwargs:
            condition: String or Condition
                The search term for the GUI element located to the left of this App GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            height: int [%]
                Expresses, as a percentage, the offset of the vertical coordinate of all virtual points over the TP window from the top edge of the reference GUI element. The height of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the horizontal spacing - over the TP window - of virtual points in which a GUI element matching the condition parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.
        """
        return AppElement()

    def find_first_down_to(self, condition, timeout=default_timeout, width=50, step=30):
        """
        This method looks for a GUI element matching the condition parameter and located to the bottom of this GUI element.

        GUI element searches take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The GUI element to be found must occur in the same TP window as the GUI element tied to an instance of this class.
        Prior to finding the element, the TP window is transferred to the foreground.
        The coordinates of the virtual points in which a GUI element matching the condition parameter is to be found are then calculated over the TP window.
        The virtual points over which a GUI element matching the condition parameter is to be found have a vertical spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window. Specifically, the y-coordinate of each virtual point must be less than the y-coordinate of the lower edge of the TP window tied to the GUI element to be found. At the same time, the y-coordinate of each virtual point must be less than the y-coordinate of the lower edge of this GUI element. The first virtual point always has an y-coordinate offset by 5 pixels to the bottom of the lower edge of this GUI element.
        The horizontal (x-) coordinate of all virtual points is set to the center of this GUI element and is always the same for all virtual points.
        If GUI elements over a large number of virtual points meet the condition parameter at the same time, the GUI element closest to this GUI element is returned.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception.

        Kwargs:
            condition: String or Condition
                The search term for the GUI element located below this GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            width: int [%]
                Expresses, as a percentage, the offset of the horizontal coordinate of all virtual points over the TP window from the left edge of the reference GUI element. The width of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the vertical spacing - over the TP window - of virtual points in which a GUI element matching the condition_down_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.
        """
        return AppElement()

    def find_first_up_to(self, condition, timeout=default_timeout, width=50, step=30):
        """
        This method looks for a GUI element matching the condition parameter and located above this GUI element.

        GUI element searches take place in iterations with a 50 ms delay over the time specified in the timeout parameter. The GUI element to be found must occur in the same TP window as the GUI element tied to an instance of this class.
        Prior to finding the element, the TP window is brought to the foreground.
        The coordinates of the virtual points in which a GUI element matching the condition parameter is to be found are then calculated over the TP window.
        The virtual points over which a GUI element matching the condition parameter is to be found have a vertical spacing defined by the step parameter (in pixels).
        The number of virtual points is determined by the size of the TP window. Specifically, the y-coordinate of each virtual point must be less than the y-coordinate of the upper edge of the TP window tied to the GUI element to be found. At the same time, the y-coordinate of each virtual point must be greater than the y-coordinate of the upper edge of this GUI element. The first virtual point always has an y-coordinate offset by 5 pixels above the upper edge of this GUI element.
        The horizontal (x-) coordinate of all virtual points is set to the center of this GUI element and is always the same for all virtual points.
        If GUI elements over a large number of virtual points meet the condition parameter at the same time, the GUI element closest to this GUI element is returned.
        If the method could not find the GUI element required, it raises the urpa.ElementNotFoundError exception

        Kwargs:
            condition: String or Condition
                The search term for the GUI element located above this GUI element.
            timeout: int [ms]
                The maximum time in which a GUI element matching the condition parameter must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            width: int [%]
                Expresses, as a percentage, the offset of the horizontal coordinate of all virtual points over the TP window from the left edge of the reference GUI element. The width of the reference GUI element is 100%.
            step : int [px]
                Expresses, in pixels, the vertical spacing - over the TP window - of virtual points in which a GUI element matching the condition_down_element parameter is to be found.
        Returns:
            Returns an AppElement-type object
        Raises:
            ElementNotFoundError: The GUI element required could not be found within the timeout period.
        """
        return AppElement()

    def find_first_visual(self, pattern, region=None, timeout=default_timeout, transformations=None):
        """
        This method looks for a visual GUI element (pattern) in a given region and returns it as a VisualElement object.

        Kwargs:
            pattern: string or bytearray, e.g. "img / pattern.bmp"
                The path to the image in png, bmp format, or the value returned by the visual_data (bytearray) method.
            region: a tuple containing four ints, for example (10, 10, 20, 20) or None. Optional argument, set to None by default. The tuple defines (left, top, right, bottom) the coordinates of the rectangle defining the selected region in px. The coordinates are relative to the upper left corner of the GUI element to which the AppElement class instance is tied. The value None means that the region selected is identical in size to the GUI element to which the AppElement class instance is tied.
            timeout: int [ms]
                The maximum time in which a visual GUI element must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            transformations: a transformation object that may contain several operations modifying the source pattern and the region searched. See TransformationFactory.

        Returns:
            Returns one VisualElement-type object

        Raises:
            ElementNotFoundError: The visual GUI element required could not be found within the timeout period.

        Examples:
            Example

            # First find the AppElement called Red Rectangle.
            element = app.find_first(cf.name("Red Rectangle"))
            # Define the path to the pattern file.
            template_path = "img/template.bmp"
            visual = element.find_first_visual(template_path)
        """
        return VisualElement()

    def find_all_visual(self, pattern, region=None, elements=0, timeout=default_timeout, transformations=None):
        """
        This method looks for visual GUI elements (patterns) in a given region and returns them as a list of objects VisualElement.

        Kwargs:
            pattern: string or bytearray, e.g. "img / pattern.bmp"
                The path to the image in png, bmp format, or the value returned by the visual_data (bytearray) method.
            region: a tuple containing four ints, for example (10, 10, 20, 20) or None. Optional argument, set to None by default. The tuple defines (left, top, right, bottom) the coordinates of the rectangle defining the selected region in px. The coordinates are relative to the upper left corner of the GUI element to which the AppElement class instance is tied. The value None means that the region selected is identical in size to the GUI element to which the AppElement class instance is tied.
            elements: int
                The minimum number of visual GUI elements that must be found within the period defined in the timeout parameter.
            timeout: int [ms]
                The maximum time in which visual GUI elements must be retrieved. If this parameter is not passed, the default value is applied, see urpa.default_timeout.
            transformations: a transformation object that may contain several operations modifying the source pattern and the region searched. See TransformationFactory.

        Returns:
            Returns a list of VisualElement-type objects

        Raises:
            ElementNotFoundError: The visual GUI elements required could not be found within the timeout period.

        Examples:
            Example

            element = app.find_first(cf.name("Red Rectangle"))
            region = (-10, -12, 42, 40)
            # Define how many visual GUI elements you wish to find at minimum.
            elements = 2
            timeout = 60000
            tf = urpa.transformation_factory()
            # Define the execution of color inversion first and then a 50% threshold.
            transformations = tf.colors_inversion().binary_image(0.5)
            visuals = element.find_all_visual("img/template.png", region, elements, timeout, transformations)
            # Simulate a mouse click over the GUI element most recently found.
            visuals[-1].send_mouse_click()

        """
        pass

class VisualElement:
    """ This class represents a visual GUI element in an application.
    An instance of this class can be created by one of the AppElement class methods, such as AppElement.find_first_visual, AppElement.find_all_visual.
    """

    def send_mouse_click(self, action=default_mouse_action, position=None):
        """ This method simulates the mouse action specified in the action parameter. The mouse action is performed over the center of this visual GUI element. By default, this method makes an HW left mouse click in the center of the visual GUI element. Delays in sending individual messages that simulate the mouse action are set to 50 ms.

        Kwargs:
            action: String
                A parameter specifying the type of mouse action that will be simulated over the visual GUI element. For possible parameter values, see the urpa.set_default_mouse_action method.
            position: a tuple with 2 int-type elements (left, top).
                Specifies the mouse click position in the format left, top.
                The coordinates are relative to the upper left corner of the visual GUI element.

        Examples:
            The example of opening https://playground.ultimaterpa.com in Internet Explorer, finding an "authentication" visual GUI element called "Continue", waiting for 3 seconds, simulating a click on the "Continue" visual GUI element found, finding the "Success" authentication element.

            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            verify_element = app.find_first_visual("img/continue.bmp")
            time.sleep(3)
            verify_element.send_mouse_click("Left")
            verify_element_success = app.find_first("Success")

        """
        pass

    def send_text(self, text, action=default_text_action, kl=default_kl, focus_action=default_focus_action):
        """ This method simulates the pressing and releasing of a key sequence, over a visual GUI element, represented by a string in the "text" parameter. Prior to the simulation of the key press and release, the TP window tied to the visual GUI element is transferred to the foreground. The actual key press/release simulation is only tied to the TP window handle, i.e. if the GUI element does not gain or loses focus during the simulation, the simulation will not be executed correctly.
        While processing the key simultation, first the string from the "text" parameter is divided into individual characters. A sequence is then created that represents key press ("down") and key release ("up") according to the characters in the "text" parameter. For example, the string "Lev" is broken down into the sequence Shift(Down)+l(Down)+l(Up)+Shift(Up)+e(Down)+e(Up)+v(Down)+v(Up). A 100 ms delay is "processed" following the simulation of the press (Down) / release (Up) of each key. If one of the "hw" simulation modes is set in the "type" parameter, the simulation must take place in the foreground. If a simulation is running in the background, when the "type" parameter is set to one of the "hw" values it is automatically transferred to the foreground. When the "type" parameter is set to one of the "standard" values, during a simulation individual characters are converted into virtual-key codes or alt-codes, and then the simulation can also run in the background. When the "type" parameter is set to "wm_char", the string from the "text" parameter splits directly into individual characters in the simulation.

        Kwargs:
            text: String
                Text, the writing of which will be simulated over an application tied to a visual GUI element represented by an instance of this class.
            action: String
                The mode for the simulation of individual keystrokes, represented by a string in the "text" parameter.
                * "hw_alt_code" This option uses the classic disassembly of text characters into Alt-code and their sequential simulation. The Windows API keybd_event() function is invoked over an application tied to a visual GUI element during the simulation.
                * "hw_scan_virtual" This option draws on the decomposition of characters from the "text" parameter using *.xml conversion files from the KeybLayoutTranslate directory. If, for the "kl" parameter, a keyboard layout is set for which there is no KeybLayoutTranslate\00000*.xml file, this file needs to be created for that keyboard layout, otherwise the user activity simulation will not work correctly. The Windows API keybd_event() function is invoked over an application tied to a visual GUI element during the simulation.
                * "standard_alt_code" This option uses the classic decomposition of text characters into Alt-code and their sequential simulation. Messages with WM_KEYDOWN and WM_KEYUP parameters are sent to an application tied to a visual GUI element via the Windows API PostMessage() function.
                * "standard_scan_virtual" This option draws on the decomposition of characters from the "text" parameter using *.xml conversion files from the KeybLayoutTranslate directory. If, for the "kl" parameter, a keyboard layout is set for which there is no KeybLayoutTranslate\00000*.xml file, this file needs to be created for that keyboard layout, otherwise the user activity simulation will not work correctly.
                Messages with WM_KEYDOWN and WM_KEYUP parameters are sent to an application tied to a visual GUI element via the Windows API PostMessage() function.
                * "wm_char" This option is appropriate when the Keyboard Layout specification is unclear and when characters accessible with different keyboard contexts need to be transferred to an application. Setting this option results only in the direct splitting of the string from the "text" parameter in the simulation. The keyboard layout set in the "kl" parameter is ignored when this simulation mode is used.
            kl: String
                Represents the keyboard layout that is automatically set for an application tied to a visual GUI element when simulating text input.

            focus_action: String
                The way in which control activation is to be simulated.
                See set_default_focus_action for options.

        Raises:
            ValueError: one of the parameters passed does not have a valid format.

        Examples:
            The example of opening Internet Explorer on the about:blank page, simulating the input of the text https://playground.ultimaterpa.com in the address bar, and going to this page by pressing the Enter key.

            app = urpa.exec_ie_app("about:blank")
            verify_element = app.find_first(cf.value("about:blank"))
            time.sleep(1)
            verify_element.send_text("https://playground.ultimaterpa.com")
            verify_element.send_key("ENTER")
            time.sleep(1)
            ready_element = app.find_first(cf.button().name("Continue"))

        """
        pass

    def send_key(self, text, type=default_key_action, focus_action=default_focus_action):
        """ This method simulates - over a visual GUI element - the pressing of a specified key combination.
        Prior to the simulation of the pressing of the specified key combination, the TP window tied to the visual GUI element is transferred to the foreground. The actual simulation of the pressing of the specified key combination is only tied to the TP window handle, i.e. if the GUI element does not gain or loses focus during the simulation, the simulation will not be executed correctly. While simulating the key press, first the string from the "text" parameter is divided into individual characters. The delimiter between characters is "+".
        A sequence is then created that represents key press ("down") and key release ("up") according to the characters in the "text" parameter. For example, the Ctrl+Shift+s combination is broken down into the sequence Ctrl(Down)+Shift(Down)+s(Down)+s(Up)+Shift(Up)+Ctrl(Up). A 100 ms delay is "processed" following the simulation of the press (Down) / release (Up) of each key. If a Hardware simulation mode is set in the "type" parameter, the simulation must take place in the foreground. If a simulation is running in the background, when the "type" parameter is set to Hardware it is automatically transferred to the foreground. When the "type" parameter is set to a Standard value, during a simulation individual characters are converted into virtual-key codes, and the simulation can also run in the background.
        This method is not suitable for direct text input.

        Kwargs:
            text: String
                * "ALT"
                * "RALT" - right Alt
                * "CTRL"
                * "RCTRL" - right Ctrl
                * "TAB"
                * "ENTER", "RETURN"
                * "BACKSPACE"
                * "ESC", "ESCAPE"
                * "END"
                * "HOME"
                * "LEFT"
                * "UP"
                * "RIGHT"
                * "DOWN"
                * "INSERT"
                * "DELETE", "DEL"
                * "HELP"
                * "NUMLOCK"
                * "SCROLL"
                * "PGDOWN", "NEXT"
                * "PGUP", "PRIOR"
                * "CLEAR"
                * "SHIFT"
                * "RSHIFT" - right shift
                * "WIN"
                * "RWIN"
                * "APPS"
                * "SPACE"
                * or a key combination, e.g. "ALT+x"

            type: String
                The way in which the keystrokes are to be simulated.
                * Hardware
                * Standard

            focus_action: String
                The way in which control activation is to be simulated.
                See set_default_focus_action for options.

        Raises:
            ValueError: the "text" or "type" parameters passed does not have a valid format.

        Examples:
            The example of opening Internet Explorer on the about:blank page, invoking the "Show documents downloaded" dialogue box by simulating the pressing of the Ctrl+J keyboard shortcut and closing this dialogue box by simulating the Alt+Z keyboard shortcut.

            app = urpa.exec_ie_app("about:blank")
            verify_element = app.find_first(cf.value("about:blank"))
            time.sleep(1)
            verify_element.send_key("Ctrl+J")
            time.sleep(1)
            close_element = app.find_first(cf.button().access_key("Alt+Z"))
            time.sleep(1)
            close_element.send_key("Alt+Z")
        """
        pass

    def bounding_rectangle(self):
        """ This method returns the absolute coordinates of this visual GUI element on the desktop in the order left, top, right, bottom.

        Returns:
            Returns a tuple containing the absolute coordinates of this visual GUI element on the desktop in the order left, top, right, bottom.
        """
        return (0, 0, 0, 0)

    def size(self):
        """ This method returns the size of this visual GUI element in the order width, height.
        Returns:
            Returns a tuple containing the size of this visual GUI element in the order width, height.
         """
        return (0, 0)

class AppJavaElement(AppElement):

    def description(self):
        """ This method returns the value of the "description" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "description" attribute of this App GUI element.
        """
        return ""

    def text_value(self):
        """ This method returns the value of the "text" attribute of this App GUI element.

        Returns:
            Returns a string containing the value of the "text" attribute of this App GUI element.
        """
        return ""

    def actions(self):
        """ This method returns the value of the "actions" attribute of this App GUI element.

        Returns:
            Returns a list of strings containing the values of the "actions" attribute of this App GUI element.
        """
        return ["click"]

    def icons(self):
        """ This method returns the value of the "icons" attribute of this App GUI element.

        Returns:
            Returns a list of string containing the values of the "icons" attribute of this App GUI element.
        """
        return [""]

    def states(self):
        """ This method returns the value of the "states" attribute of this App GUI element.

        Returns:
            Returns a list of strings containing the values of the "states" attribute of this App GUI element.
        """
        return ["enabled", "focusable", "visible"]

class WindowCondition:

    def size(self, x, y):
        """ This method returns a WindowCondition-type object that has validation set to parameters x and y for the internal
        attribute Size. Only GUI elements that are exactly equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def min_size(self, x, y):
        """ This method returns a WindowCondition-type object that has validation set to parameters x and y for the internal
        attribute Size. Only GUI elements that are greater than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the minimum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the minimum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def max_size(self, x, y):
        """ This method returns a WindowCondition-type object that has validation set to parameters x and y for the
        internal attribute Size. Only GUI elements that are less than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the maximum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the maximum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def name(self, val):
        """ This method returns a WindowCondition-type object that has validation set to the val parameter for the internal attribute Name.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from this parameter is set for the Name
                internal attribute of this object. If this is a WindowCondition-type parameter, validation from the object passed
                through this parameter is set for the Name internal attribute of this object.

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def class_name(self, val):
        """ This method returns a WindowCondition-type object that has validation set to the val parameter for the internal attribute Class Name.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Class Name internal attribute of this object. If this is a WindowCondition-type parameter, validation from the object passed by the val parameter is set for the Class Name internal attribute of this object.

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def enabled(self, val):
        """ This method returns a WindowCondition-type object that has validation set to the val parameter for the internal attribute Enabled.

        Kwargs:
            val: bool

        Returns:
            Returns a WindowCondition-type object
        """
        return WindowCondition()

    def max_depth(sef, max_depth):
        return WindowCondition()

class JavaCondition:
    """ This class is used to define conditions for GUI element searches. An instance of this class is used as a parameter
    in the App and AppElement methods. An instance of this class is created using the ConditionFactory class - see urpa.condition_factory().
    Each instance of this class contains the internal variables Name, Value, Control type, Access key, Size, Description,
    Actions, States, Icons, and Text value. For the internal variables Name, Value, Item Type, Access Key, Automation ID, and Class Name,
    the validation mode may be set to an exact match or to a match with a regular expression using the methods
        *	name()
        *	value()
        *	access_key()
        *	description()
        *	text_value()

    For the internal variables Size and Control Type, the validation mode may only be set to an exact match. For the internal variable
    Control Type, the value may only be set "directly" by invoking one of these methods
        *	alert()
        *	column_header()
        *	canvas()
        *	combo_box()
        *	desktop_icon()
        *	internal_frame()
        *	desktop_pane()
        *	option_pane()
        *	window()
        *	frame()
        *	dialog()
        *	color_chooser()
        *	directory_pane()
        *	file_chooser()
        *	filler()
        *	hyperlink()
        *	icon()
        *	label()
        *	root_pane()
        *	glass_pane()
        *	layered_pane()
        *	list()
        *	list_item()
        *	menu_bar()
        *	popup_menu()
        *	menu()
        *	menu_item()
        *	separator()
        *	page_tab_list()
        *	page_tab()
        *	panel()
        *	progress_bar()
        *	password_text()
        *	push_button()
        *	toggle_button()
        *	check_box()
        *	radio_button()
        *	row_header()
        *	scroll_pane()
        *	scroll_bar()
        *	viewport()
        *	slider()
        *	split_pane()
        *	table()
        *	text()
        *	tree()
        *	tool_bar()
        *	tool_tip()
        *	awt_component()
        *	swing_component()
        *	unknown()
        *	status_bar()
        *	date_editor()
        *	spin_box()
        *	font_chooser()
        *	group_box()
        *	header()
        *	footer()
        *	paragraph()
        *	ruler()
        *	editbar()
        *	progress_monitor()

    For the internal variable Size, the value may be set by invoking one of these methods
        *	size()
        *	max_size()
        *	min_size()

    """

    def size(self, x, y):
        """ This method returns a JavaCondition-type object that has validation set to parameters x and y for the internal
        attribute Size. Only GUI elements that are exactly equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def min_size(self, x, y):
        """ This method returns a JavaCondition-type object that has validation set to parameters x and y for the internal
        attribute Size. Only GUI elements that are greater than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the minimum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the minimum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def max_size(self, x, y):
        """ This method returns a JavaCondition-type object that has validation set to parameters x and y for the
        internal attribute Size. Only GUI elements that are less than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the maximum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the maximum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def name(self, val):
        """ This method returns a JavaCondition-type object that has validation set to the val parameter for the internal attribute Name.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from this parameter is set for the Name
                internal attribute of this object. If this is a Condition-type parameter, validation from the object passed
                through this parameter is set for the Name internal attribute of this object.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def value(self, val):
        """ This method returns a JavaCondition-type object that has validation set to the val parameter
        for the internal attribute Value.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Value
                internal attribute of this object. If this is a Condition-type parameter, validation from the object passed
                through the val parameter is set for the Value internal attribute of this object.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def access_key(self, val):
        """ This method returns a JavaCondition-type object that has validation set to the val parameter for the internal attribute Access Key.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Access Key
                internal attribute of this object. If this is a Condition-type parameter, validation from the object passed
                by the val parameter is set for the Access Key internal attribute of this object.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def description(self, val):
        """ This method returns a JavaCondition-type object that has validation set to the val parameter for the internal
        attribute Description.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the
                Description internal attribute of this object. If this is a Condition-type parameter, validation from
                the object passed by the val parameter is set for the Description internal attribute of this object.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def text_value(self, val):
        """ This method returns a JavaCondition-type object that has validation set to the val parameter for the internal
        attribute Text.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Text value
                internal attribute of this object. If this is a Condition-type parameter, validation from the object
                passed by the val parameter is set for the Text value internal attribute of this object.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def actions(items, compare="partial"):
        """ This method returns a JavaCondition-type object that has validation set to the items parameter for the
        internal attribute Action, with the compare comparison type.

        Kwargs:
            items: list/tuple of String
                A list of String-type values that the elements searched for in the "actions" attribute must contain.

            compare: String ("partial" or "exact")
                Type of comparison used. With "exact", only elements that contain all values from items and no others
                in the "actions" attribute will satisfy the resulting condition. With "partial", it is enough for the "actions"
                attribute to contain all the values from items, but it may also contain other values.
                With both types of comparison, the order of values is irrelevant.
        """
        return self

    def states(items, compare="partial"):
        """ This method returns a JavaCondition-type object that has validation set to the items parameter for the
        internal attribute States, with the compare comparison type.

        Kwargs:
            items: list/tuple of String
                A list of String-type values that the elements searched for in the "states" attribute must contain.

            compare: String ("partial" or "exact")
                Type of comparison used. With "exact", only elements that contain all values from items and no others
                in the "states" attribute will satisfy the resulting condition. With "partial", it is enough for the "states"
                attribute to contain all the values from items, but it may also contain other values.
                With both types of comparison, the order of values is irrelevant.
        """
        return self

    def icons(items, compare="partial"):
        """ This method returns a JavaCondition-type object that has validation set to the items parameter for the
        internal attribute Icons, with the compare comparison type.

        Kwargs:
            items: list/tuple of String
                A list of String-type values that the elements searched for in the "icons" attribute must contain.

            compare: String ("partial" or "exact")
                Type of comparison used. With "exact", only elements that contain all values from items and no others
                in the "icons" attribute will satisfy the resulting condition. With "partial", it is enough for the "icons"
                attribute to contain all the values from items, but it may also contain other values.
                With both types of comparison, the order of values is irrelevant.
        """

    def alert(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "alert" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def column_header(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "column_header" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def canvas(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "canvas" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def combo_box(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "combo_box" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def desktop_icon(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "desktop_icon" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def internal_frame(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "internal_frame" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def desktop_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "desktop_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def option_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "option_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def window(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "window" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def frame(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "frame" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def dialog(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "dialog" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def color_chooser(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "color_chooser" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def directory_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "directory_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def file_chooser(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "file_chooser" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def filler(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "filler" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def hyperlink(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "hyperlink" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def icon(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "icon" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def label(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "label" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def root_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "root_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def glass_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "glass_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def layered_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "layered_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def list(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "list" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def list_item(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "list_item" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def menu_bar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "menu_bar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def popup_menu(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "popup_menu" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def menu(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "menu" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def menu_item(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "menu_item" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def separator(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "separator" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def page_tab_list(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "page_tab_list" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def page_tab(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "page_tab" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def panel(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "panel" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def progress_bar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "progress_bar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def password_text(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "password_text" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def push_button(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "push_button" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def toggle_button(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "toggle_button" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def check_box(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "check_box" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def radio_button(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "radio_button" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def row_header(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "row_header" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def scroll_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "scroll_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def scroll_bar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "scroll_bar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def viewport(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "viewport" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def slider(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "slider" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def split_pane(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "split_pane" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def table(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "table" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def text(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "text" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def tree(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "tree" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def tool_bar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "tool_bar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def tool_tip(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "tool_tip" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def awt_component(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "awt_component" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def swing_component(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "swing_component" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def unknown(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "unknown" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def status_bar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "status_bar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def date_editor(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "date_editor" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def spin_box(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "spin_box" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def font_chooser(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "font_chooser" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def group_box(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "group_box" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def header(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "header" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def footer(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "footer" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def paragraph(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "paragraph" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def ruler(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "ruler" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def editbar(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "editbar" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

    def progress_monitor(self, val=None):
        """ This method returns a JavaCondition-type object that has the Control Type attribute set to "progress_monitor" and
        the Name, Value, and Text attributes set to val.

        Kwargs:
            val: String or JavaCondition
                If this is a String-type parameter, the string represents the value of the Name, Value, and
                Text attribute in an object tied to an instance of this class. If this is a Condition-type parameter,
                validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a JavaCondition-type object
        """
        return JavaCondition()

class TransformationFactory:
    """ An auxiliary class that defines how images are to be transformed. """
    def	change_colors(self, from_colors, to_color):
        """
        This method prepares the transformation of the color list to a specific color.

        Kwargs:
            from_colors: a color list where the components are a tuple, the elements of which comprise three integers with a value from 0 to 255, for example [(255, 255, 255), (128, 128, 128)]
            to_color: a tuple, the elements of which comprise three integers with a value from 0 to 255, for example (0, 0, 0)

        Returns:
            Returns a Transformation-type object

        Examples:
            Example

            element = app.find_first(cf.name("Red Rectangle"))
            timeout = 30000
            # Create transformation factory.
            tf = urpa.transformation_factory()
            # Define the list of colors to be converted.
            from_colors = [(0, 255, 0), (0, 254, 0)]
            # Define the color to which colors from the list are to be changed.
            to_color = (255, 255, 255)
            # Define transformation factory.
            transformation = tf.change_color(from_colors, to_color)
            visual = element.find_first_visual("img/template.bmp", (20, 30, 45, 50), timeout, transformation)
        """
        return Transformation()

    def colors_inversion(self):
        """
        This method prepares the transformation of colors to their inverse value.

        Returns:
            Returns a Transformation-type object

        Examples:
            Example

            element = app.find_first(cf.name("Red Rectangle"))
            timeout = 30000
            # Create transformation factory.
            tf = urpa.transformation_factory()
            # Define transformation factory.
            transformation = tf.colors_inversion()
            visual = element.find_first_visual("img/template.bmp", (20, 30, 45, 50), timeout, transformation)
        """
        return Transformation()

    def threshold(self, threshold):
        """
        The method prepares for bitmap transformation to a bitmap (black and white only).

        Kwargs:
            threshold: float, e.g. 0.5
                A value from 0 to 1, indicating at what ratio the range between 0 and 255 is to be divided into two groups.

        Returns:
            Returns a Transformation-type object

        Examples:
            Example

            element = app.find_first(cf.name("Red Rectangle"))
            timeout = 30000
            # Create transformation factory.
            tf = urpa.transformation_factory()
            # Define transformation factory.
            transformation = tf.threshold(0.4)
            visual = element.find_first_visual("img/template.bmp", (20, 30, 45, 50), timeout, transformation)
        """
        return Transformation()

class Transformation(TransformationFactory):
    """ An auxiliary class that defines how images are to be transformed. """
    pass

class ConditionFactory:
    """ This class is used to create an instance of a Condition-type object and to define the conditions for searching for GUI elements in this instance of the object."""

    def java(self, value=None):
        return JavaCondition()

    def regexp(self, re):
        """ This method returns a Condition-type object that has the condition of the regular expression redeclared for the internal attributes Name, Value, Automation ID, and Class Name.

        Kwargs:
            re: String
                A regular expression is created and evaluated according to the following rules
                *	[abc]	corresponds to a or b or c
                *	[a-z]	corresponds to one character from a to z
                *	[^abc]	corresponds to all except a, b or c
                *	[^a-z]	corresponds to all except a character from a to z
                *	.		corresponds to any one character
                *	x+		corresponds to n characters x, n>0
                *	x*		corresponds to n characters x, n>=0
                *	z?		corresponds to the character z or blank
                *	abc|cba	corresponds to the abc or cba string
                *	^		start of text
                *	$		end of text
                *	\\t		TAB
                *	\\		escape character
                *	1(2-3)	corresponds to 12 and 13

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def exact(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attributes Name, Value, Automation ID, and Class Name.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, an exact match with a string from this parameter is set for the Name, Value, Automation ID, and Class Name internal attributes of this object.
                If this is a Condition-type parameter, validation from the Condition object passed by this parameter is set for the Name, Value, Automation ID, and Class Name internal attributes of this object.

        Returns:
            Returns a Condition-type object

        """
        return Condition()

    def size(self, x, y):
        """ This method returns a Condition-type object that has validation set to parameters x and y for the internal attribute Size. Only GUI elements that are exactly equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def min_size(self, x, y):
        """ This method returns a Condition-type object that has validation set to parameters x and y for the internal attribute Size. Only GUI elements that are greater than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the minimum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the minimum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def max_size(self, x, y):
        """ This method returns a Condition-type object that has validation set to parameters x and y for the internal attribute Size. Only GUI elements that are less than or equal to (x, y) in size match the resulting condition.

        Kwargs:
            x: int
                Represents the maximum horizontal value of the Size internal attribute in an object tied to an instance of this class.
            y: int
                Represents the maximum vertical value of the Size internal attribute in an object tied to an instance of this class.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def name(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Name.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from this parameter is set for the Name internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by this parameter is set for the Name internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def max_depth(self, max_depth):
        return Condition()

    def value(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter
        for the internal attribute Value.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Value internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by the val parameter is set for the Value internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def item_type(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Item Type.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Item Type internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by the val parameter is set for the Item Type internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def access_key(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Access Key.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Access Key internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by the val parameter is set for the Access Key internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def automation_id(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Automation ID.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Automation ID internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by the val parameter is set for the Automation ID internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def class_name(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Class Name.

        Kwargs:
            val: String or object The condition created using the regexp() method.
                If this is a String-type parameter, an exact match with a string from the val parameter is set for the Class Name internal attribute of this object. If this is a Condition-type parameter, validation from the object passed by the val parameter is set for the Class Name internal attribute of this object.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def enabled(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Enabled.

        Kwargs:
            val: bool

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def selected(self, val):
        """ This method returns a Condition-type object that has validation set to the val parameter for the internal attribute Selected.

        Kwargs:
            val: bool

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # button
    def button(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Button" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def calendar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Control" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # checkbox
    def check_box(self, val = None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "CheckBox" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def combo_box(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ComboBox" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # edit
    def edit(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Edit" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def hyperlink(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Hyperlink" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def image(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Image" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # list item
    def list_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ListItem" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # list
    def list(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "List" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # menu
    def menu(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Menu" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # menu bar
    def menu_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "MenBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # menu item
    def menu_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "MenuItem" and the Name, Value, Automation ID, and Class Name attributes set to val. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def progress_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ProgressBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # radio button
    def radio_button(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "RadioButton" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def scroll_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ScrollBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def slider(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Slider" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def spinner(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Spinner" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def status_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "StatusBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # tab
    def tab(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Tab" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # tab item
    def tab_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "TabItem" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def text(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Text" and the Name, Value, Automation ID, and Class Name attributes set to val.
¨
        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # toolbar
    def tool_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ToolBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def tool_tip(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "ToolTip" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def tree(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Tree" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def tree_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "TreeItem" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def custom(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Custom" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def group(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Group" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def thumb(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Thumb" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def data_grid(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "DataGrid" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def data_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "DataItem" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def document(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Document" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def split_button(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "SplitButton" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def window(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Window" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # pane
    def pane(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Pane" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def header(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Header" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def header_item(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "HeaderItem" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def table(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Table" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    # title bar
    def title_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "TitleBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def separator(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "Separator" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def semantic_zoom(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "SemanticZoom" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

    def app_bar(self, val=None):
        """ This method returns a Condition-type object that has the Control Type attribute set to "AppBar" and the Name, Value, Automation ID, and Class Name attributes set to val.

        Kwargs:
            val: String or Condition
                If this is a String-type parameter, the string represents the value of the Name, Value, Automation ID, and Class Name attribute in an object tied to an instance of this class. If this is a Condition-type parameter, validation from the active attributes of the object passed by the val parameter is set.

        Returns:
            Returns a Condition-type object
        """
        return Condition()

class Condition(ConditionFactory):
    """ This class is used to define conditions for GUI element searches. An instance of this class is used as a parameter
    in the App and AppElement methods. An instance of this class is created using the ConditionFactory class - see urpa.condition_factory().
    Each instance of this class contains the internal variables Name, Value, Control Type, Item Type, Access Key, Automation ID, Class Name, and Size.
    For the internal variables Name, Value, Item Type, Access Key, Automation ID, and Class Name, the validation mode may be set to an exact match or
    to a match with a regular expression using the methods
        *	name()
        *	value()
        *	item_type()
        *	access_key()
        *	automation_id()
        *	class_name()

    For the internal variables Size and Control Type, the validation mode may only be set to an exact match. For the internal variable
    Control Type, the value may only be set "directly" by invoking one of these methods
        *	button()
        *	calendar()
        *	check_box()
        *	combo_box()
        *	edit()
        *	hyperlink()
        *	image()
        *	list_item()
        *	list()
        *	menu()
        *	menu_bar()
        *	menu_item()
        *	progress_bar()
        *	radio_button()
        *	scroll_bar()
        *	slider()
        *	spinner()
        *	status_bar()
        *	tab()
        *	tab_item()
        *	text()
        *	tool_bar()
        *	tool_tip()
        *	tree()
        *	tree_item()
        *	custom()
        *	group()
        *	thumb()
        *	data_grid()
        *	data_item()
        *	document()
        *	split_button()
        *	window()
        *	pane()
        *	header()
        *	header_item()
        *	table()
        *	title_bar()
        *	separator()
        *	semantic_zoom()
        *	app_bar()

    For the internal variable Size, the value may be set by invoking one of these methods
        *	size()
        *	max_size()
        *	min_size()

    """
    pass

class AppExcel(App):
    """ A class representing MS Excel.
    This class contains methods that allow you to manage workbooks and their components in an MS Excel application.
    """

    def __init__(self):
        self.display_alerts = True

    def active_workbook(self):
        """ This method returns an active workbook in an MS Excel application.

        Returns:
            Returns an ExcelWorkbook-type object; if no active workbook exists, it returns None.
        """
        return ExcelWorkbook()

    def active_worksheet(self):
        """ This method returns an active sheet in an MS Excel application.

        Returns:
            Returns an ExcelWorksheet-type object; if no active sheet exists, it returns None.
        """
        return ExcelWorksheet()

    def workbooks(self):
        """ This method returns a list of all open workbooks in an MS Excel application.

        Returns:
            Returns a list of ExcelWorkbook-type objects.
        """
        pass

    def add_workbook(self):
        """ This method adds a new workbook to an MS Excel application.

        Returns:
            Returns an ExcelWorkbook-type object tied to a newly created MS Excel workbook.
        """
        return ExcelWorkbook()

    def open(self, filename, update_links = None):
        """ This method opens the MS Excel workbook with the name passed.

        Kwargs:
            filename: String
                The path and title for the MS Excel workbook to be opened (need not contain a suffix).

            update_links: bool

        Returns:
            Returns an ExcelWorkbook-type object tied to a newly opened MS Excel workbook.
        """
        return ExcelWorkbook()

class ExcelWorkbook:
    """ This class represents a workbook in MS Excel. """

    def __getitem__(self, name):
        """ Returns a sheet with the given name.

        Returns:
            Returns a sheet with the given name. Returns None if there is no sheet with the given name.
        """
        return self.sheet_by_name[key]

    def active_worksheet(self):
        """ This method returns an active sheet of an MS Excel workbook.

        Returns:
            Returns an ExcelWorksheet-type object; if no active workbook exists, it returns None.
        """
        return ExcelWorksheet()

    def sheet_by_name(self, name):
        """ Returns a sheet with the given name.

        Returns:
            Returns a sheet with the given name. Returns None if there is no sheet with the given name.
        """
        return ExcelWorksheet()

    def sheets(self):
        """ This method returns a list of all sheets in an MS Excel workbook.

        Returns:
            Returns a list of ExcelWorksheet-type objects.
        """
        pass

    def full_name(self):
        """ This method returns a path and name for an MS Excel workbook.

        Returns:
            Returns a string containing the path and name of an MS Excel workbook (including the suffix).
        """
        return "full name"

    def activate(self):
        """ This method activates (transfers to the foreground) a window tied to an MS Excel workbook. """
        pass

    def save(self):
        """ This method saves an MS Excel workbook. """
        pass

    def save_as(self, filename, format=None):
        """ This method saves an MS Excel workbook into a file with the passed name.

        Kwargs:
            filename: str
            format: str or int
                * "XLSX" - Open XML Workbook
                * "XLS" - Excel 97-2003 Workbook
                * "CSV" - CSV
                * For an existing file, the default format is the last file format specified; for a new file, the default is the format of the version of Excel being used.
        """
        pass

    def add_worksheet(self):
        """ This method adds a new worksheet to an MS Excel workbook.
        Returns:
            Returns an ExcelWorkbook-type object tied to a newly created worksheet of an MS Excel workbook.
        """
        return ExcelWorksheet()

    def close(self):
        """ This method closes an MS Excel workbook. """
        pass

class ExcelWorksheet:
    """ This class represents one sheet in an MS Excel workbook. """

    def name(self):
        """ This method returns the name of a sheet of an MS Excel workbook.

        Returns:
            Returns a string containing the name of a sheet in an MS Excel workbook.
        """
        return "List"

    def cells(self):
        """ This method returns all the cells of a sheet in an MS Excel workbook.

        Returns:
            Returns an ExcelCells-type object, representing all the cells of a sheet in an MS Excel workbook.
        """
        return ExcelCells()

    def used_range(self):
        """ This method returns a block or area of used cells of a sheet in an MS Excel workbook.

        Returns:
            Returns an ExcelCells-type object, representing a block or area of used cells, i.e. used and empty cells.
        """
        return ExcelCells()

    def cell(self, col, row):
        """ This method returns the cell of a sheet of an MS Excel workbook in a position specified by its col and row parameters.
         The col and row indices are numbered from 1 in the MS Excel workbook sheet.

        Kwargs:
            col: integer
                The index of the column in which the required cell of the MS Excel workbook sheet is located.
            row: integer
                The index of the row in which the required cell of the MS Excel workbook sheet is located.

        Returns:
            Returns an ExcelCells-type object, representing one cell.
        """
        return ExcelCells()

    def activate(self):
        """ This method activates a sheet of an MS Excel workbook, and brings the workbook to the foreground."""
        pass

    def visibility(self):
        """ Returns a value that determines whether the sheet is visible.

        Returns:
            * 0 - xlSheetHidden,
            * 2 - xlSheetVeryHidden,
            * -1 - xlSheetVisible

        """
        return -1

    def set_visibility(self, visibility):
        """ Sets a value that determines whether the sheet is visible.

        Kwargs:
            visibility: int
             * 0 - xlSheetHidden,
             * 2 - xlSheetVeryHidden
             * -1 - xlSheetVisible
        """
        pass

    def protected(self):
        return False

class ExcelCells:
    """ This method represents one cell, one row, a column or a block of cells in an MS Excel workbook sheet."""

    def column(self):
        """ This method returns the minimum index of a column in a sheet of an MS Excel workbook tied to a set of cells in an instance of this class. The indices are numbered from 1.

        Returns:
            Returns an integer representing the index of the column found.
        """
        return 1

    def row(self):
        """ This method returns the minimum index of a row in a sheet of an MS Excel workbook tied to a set of cells in an instance of this class. The indices are numbered from 1.

        Returns:
            Returns an integer representing the index of the row found.
        """
        return 1

    def item(self, col, row):
        """ This method returns the cell of a sheet of an MS Excel workbook in a col and row position.
        The indices are numbered from 1.

        Kwargs:
            col: integer
                The index of the column in which the required cell of the MS Excel workbook sheet is located.
            row: integer
                The index of the row in which the required cell of the MS Excel workbook sheet is located.

        Returns:
            Returns an ExcelCells-type object, representing one cell.
        """
        return ExcelCells()

    def value(self, formatted=True):
        """ This method returns the value of a cell in a sheet of an MS Excel workbook.
        If an instance of this class represents more than one cell, the invocation of this method is not supported.

        Kwargs:
            formatted: bool

        Returns:
            Returns a string containing a cell value.
        """
        return "value"

    def set_value(self, value):
        """ This method sets a value for cells in a sheet of an MS Excel workbook. If an instance of this class represents an entire sheet in an MS Excel workbook, the invocation of this method is not supported.

        Kwargs:
            value: String
                The value to be set for cells.

        """
        pass

    def activate(self):
        """ This method activates cells in an MS Excel workbook sheet. Only one cell in an MS Excel workbook sheet may be active - see the MSDN documentation.
        """
        pass

    def select(self):
        """ This method selects cells in an MS Excel workbook sheet."""
        pass

    def rows_count(self):
        """ This method returns the number of rows in an MS Excel workbook sheet.

        Returns:
            Returns an integer representing the number of rows in an MS Excel workbook sheet.
        """
        return 1

    def columns_count(self):
        """ This method returns the number of columns in an MS Excel workbook sheet.

        Returns:
            Returns an integer representing the number of columns in an MS Excel workbook sheet.
         """
        return 1

    def copy(self):
        """ This method copies the content of MS Excel workbook sheet cells to Windows clipboard."""
        return 1

class AppIE(App):
    """ This class is used to manage the Internet Explorer browser window."""

    def navigate(self, url):
        """ This method loads the URL specified in the url parameter into the Internet Explorer browser window.

        Kwargs:
            url: String
                The URL to be navigated to.

        """
        pass

    def go_back(self):
        """ This method navigates back one item in the browsing history list in the Internet Explorer browser window."""
        pass

    def go_forward(self):
        """ This method navigates forward one item in the browsing history list in the Internet Explorer browser window."""
        pass

    def go_home(self):
        """ This method navigates to the homepage in the Internet Explorer browser window."""
        pass

    def is_busy(self):
        """ This method returns a True value if navigation or downloading is performed in the Internet Explorer browser window.

        Returns:
            Returns a bool-type value.
        """
        return True

    def ready_state(self):
        """ This method retrieves, in the return value, the status of the Internet Explorer browser window.
        Possible return values are
        * READYSTATE_UNINITIALIZED = 0
        * READYSTATE_LOADING = 1
        * READYSTATE_LOADED = 2,
        * READYSTATE_INTERACTIVE = 3,
        * READYSTATE_COMPLETE = 4

        Returns:
            Returns an integer-type value.
        """
        return 4

    def html(self):
        """ This method returns the source code of an HTML page in the Internet Explorer browser window.

        Returns:
            Returns a string containing the source code of an HTML page in the Internet Explorer browser window.
        """
        return str

    def wait_for_complete(self, timeout = default_timeout):
        """ Waits for a page to load in Internet Explorer.
        This method validates the status of the Internet Explorer client area and waits for the "complete" status.
        The maximum time over which the status of the Internet Explorer client area is validated is defined in the method timeout parameter in milliseconds.
        In the first stage in the processing of this method, a change in the status of the Internet Explorer client area from "complete" to another status is indicated.
        The initial status change indication always takes place in a maximum of twenty iterations with a 50 ms delay.
        In the second stage in the processing of this method, i.e. after a status other than "complete" is indicated, over the remainder of the timeout period the wait for "complete" status is in iterations with a 50 ms delay.
        If, in the second stage of the processing of this method, the "complete" status is not achieved within the timeout period, the processing ends with an error.

        If, in the first stage, there is a change in status from "complete" to another status and a return to "complete" status in a time faster than 50 ms, the page status change need not be registered by this method and the invocation of this method is successfully completed in the first stage.
        This method may not work correctly on pages using Java, Ajax, Flex, Flash, Javascript, etc., or if the "complete" page status is blocked by any script/technology despite its "visual correctness".

        Kwargs:
            timeout: int [ms]
                Time in ms waited for a page to load.

        Examples:
            The example of opening https://playground.ultimaterpa.com in Internet Explorer, and activating the "Continue" button after the first page has finished loading.
            The waiting for the second page to load is limited by the time set in the urpa.default_timeout variable (5,000 ms by default).
            If the pages are not loaded during the defined timeouts, the command processing ends in an error.

            app = urpa.exec_ie_app("https://playground.ultimaterpa.com")
            app.wait_for_complete(30000)
            app.find_first(cf.button().name("Continue")).send_mouse_click()
            app.wait_for_complete()
        """
        pass
