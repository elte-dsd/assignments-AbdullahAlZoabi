




























#Dummy hash functions
def H1(Char, NumOfAddresses):

    ASCII = ord(Char);

    return (((ASCII*10) + 15)*100)%NumOfAddresses;

def H2(Char, NumOfAddresses):

    ASCII = ord(Char);

    return (((ASCII - 10) + 100)*177)%NumOfAddresses;

def H3(Char, NumOfAddresses):

    ASCII = ord(Char);

    return (((ASCII*2) + 27)*18)%NumOfAddresses;


def H4(Char, NumOfAddresses):

    ASCII = ord(Char);

    return (((ASCII%10) * 1000) - 100)%NumOfAddresses;
