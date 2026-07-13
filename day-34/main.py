# age: int
# name: str
# height: float
# is_human: bool

def police_check(age: int) -> bool:
    if age>18:
        can_drive = True
    else:
        can_drive = False
    # return "They can drive."
    return can_drive


# if police_check("twelve"):
if police_check(19):
    print("You may pass")
else:
    print("Pay a fine.")
    