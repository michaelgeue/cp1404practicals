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
        print("{} is {}".format(short_state_code, STATE_DICT[short_state_code]))
    else:
        print("Invalid short state")
    short_state_code = input("Enter short state: ").upper()

for state_name_short, state_name_full in STATE_DICT.items():
    print("{:3} is {}".format(state_name_short, state_name_full))
