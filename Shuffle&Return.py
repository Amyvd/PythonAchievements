import random
def randomised():
    original = "Amisha Amy Ishika van Duin"
    randomised = ''.join(random.sample(original, len(original)))
    print(randomised)

for _ in range(3):
    randomised()
