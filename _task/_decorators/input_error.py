from functools import wraps
from colorama import Fore, Style



def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{Fore.RED}Invalid command😮 Please provide the name and phone number😊{Style.RESET_ALL}"
        except KeyError as e:
            return f"{Fore.RED}{e.args[0]}.😮 Please provide the name of an existing contact.😊{Style.RESET_ALL}"
        except IndexError:
            return f"{Fore.RED}Invalid command😮 Please provide a valid contact name.😊{Style.RESET_ALL}"

    return inner