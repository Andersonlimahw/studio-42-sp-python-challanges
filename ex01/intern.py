class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

class Intern:
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return Coffee()

# Test Cases
intern1 = Intern()  # Without a name
intern2 = Intern("Mark")  # With the name "Mark"

print("First Intern's Name:", intern1)
print("Second Intern's Name:", intern2)

try:
    print("Asking the second intern to work...")
    intern2.work()
except Exception as e:
    print("Exception:", e)

coffee = intern2.make_coffee()
print("Mark made coffee:", coffee)
