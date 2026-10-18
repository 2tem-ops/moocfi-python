from datetime import datetime, date

def is_it_valid(pic: str):
    control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    date_valid, cent_valid, char_valid, len_valid = True, True, True, True
    
    ddmmyy = pic[0:6]
    dd, mm, yy = int(ddmmyy[0:2]), int(ddmmyy[2:4]), ddmmyy[4:]
    operator = pic[6]
    id = pic[7:10]
    char = pic[-1]
    
    if operator == "+":
        century = "18"
    elif operator == "-":
        century = "19"
    elif operator == "A":
        century = "20"
    else:
        century = ""
        cent_valid = False
        
    try:    
        date(int(century + yy), mm, dd)
    except ValueError:
        date_valid = False
        
    if len(pic) != 11:
        len_valid = False
        
    control_check = int(ddmmyy + id) % 31
    
    if char != control[control_check]:
        char_valid = False
        
    if date_valid and cent_valid and char_valid and len_valid:
        return True
    return False
    
if __name__ == "__main__":
    print(is_it_valid("290200A1239")) #valid
    print(is_it_valid("290200+1239")) #invalid