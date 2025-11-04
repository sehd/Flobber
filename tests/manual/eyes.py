from ...src.eyes import Eyes, EyeStates

state = input("Enter eye state (Off, Open, Close, Blinking, Heart): ")

with Eyes() as eyes:
    while state not in EyeStates.__members__:
        eyes.set_state(state)
        state = input("Enter eye state (Off, Open, Close, Blinking, Heart): ")
