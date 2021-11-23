def match_format(ssn):
    ssn=ssn.split("-")
    return ssn[0].isupper() and ssn[1].islower() and ssn[2].isdigit()

ssn_list=input("Input: ").split()

for ssn in ssn_list:
    if match_format(ssn):
        print(ssn,": Valid SSN")
    else:
        print(ssn,": Invalid SSN")
