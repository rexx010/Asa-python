def display_asteriks(func):
    def wrapper(*args, **kwargs):
        print("**********")
        result = func(*args, **kwargs)
        print("**********")
        return result
    return wrapper

@display_asteriks
def display_name(name):
    print(name)

display_name("Oluwadamilare")

"**********"
"Oluwadamilare"
"**********"