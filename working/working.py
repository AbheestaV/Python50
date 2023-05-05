import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s_hour = e_hour = 0
    s_min = e_min = '00'
    if matches := re.search(r"^([0-9][0-9]?):?([0-9][0-9])? ([AP])M to ([0-9][0-9]?):?([0-9][0-9])? ([AP])M$", s):
        if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
            raise ValueError
        s_hour = int(matches.group(1))
        if matches.group(2):
            if int(matches.group(2)) > 59:
                raise ValueError
            s_min = matches.group(2)
        e_hour = int(matches.group(4))
        if matches.group(5):
            if int(matches.group(5)) > 59:
                raise ValueError
            e_min = matches.group(5)
        if matches.group(3) == 'A' and matches.group(1) == '12':
            s_hour = '00'
        if matches.group(6) =='P' and matches.group(4) != '12':
            e_hour += 12
        if matches.group(6) == 'A' and matches.group(4) == '12':
            e_hour = '00'
        if matches.group(3) =='P' and matches.group(1) != '12':
            s_hour += 12
        '''
        print(s_hour)
        print(s_min)
        print(e_hour)
        print(e_min)
        '''
        if len(str(s_hour)) < 2:
            s_hour = "0" + str(s_hour)
        if len(str(e_hour)) < 2:
            e_hour = "0" + str(e_hour)
        return f"{s_hour}:{s_min} to {e_hour}:{e_min}"
    else:
        raise ValueError

...


if __name__ == "__main__":
    main()
