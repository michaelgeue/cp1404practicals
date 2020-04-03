"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
STATE_DICT = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
              "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_DICT)
short_state_code = input("Enter short state: ").upper()

while short_state_code != "":
    if short_state_code in STATE_DICT:
        print(short_state_code, "is", STATE_DICT[short_state_code])
    else:
        print("Invalid short state")
    short_state_code = input("Enter short state: ").upper()

for state in STATE_DICT:
    print("{:3} is {}".format(state, STATE_DICT[state]))
