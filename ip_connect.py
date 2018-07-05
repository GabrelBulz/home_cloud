import sys

## split data and check
## return -> array: position 0-3:ip, 4-mask
def parse_ip(input):

    data=input.split(".")
    result=[]

    for i in data:
        if('/' in i):
            result.append(int(i.split("/")[0]))
            result.append(int(i.split("/")[1]))
        else:
            result.append(int(i))

    if(len(result) < 5):
        print("bad input")
        return 0

    for i in range(len(result)-1):
        if(result[i]<0 or result[i]>255):
            print("bad input")
            return 0

    if(result[4]<0 or result[4]>30):
        print("bad mask")
        return 0

    return result


def create_mask(msk):

    mask=[0,0,0,0]

    for i in range(4):
        if(msk-8 >= 0):
            mask[i]=8
        else:
            mask[i]=msk
        msk-=8

    return mask


## create the network based on ip, mask
def get_network(ip,msk):

    mask=create_mask(msk)
    actual_mask=[]

    for i in mask:
        actual_mask.append(256 - 2**(8-i))

    result=[]

    for i in range(len(ip)-1):
        result.append(ip[i] & actual_mask[i])

    return result


## create the brodcast based on ip, mask
def get_brodcast(ip,msk):

    mask=create_mask(msk)
    dif_mask=[]
    result=[]

    for i in mask:
        dif_mask.append(2**(8-i) - 1)

    for i in range(len(ip)-1):
        result.append(ip[i] | dif_mask[i])

    return result


def main():

    if(len(sys.argv) < 3):
        print("not enough input")
        return

    usr1=parse_ip(sys.argv[1])
    usr2=parse_ip(sys.argv[2])

    if(usr1 == 0 or usr2 == 0):
        return

    net1=get_network(usr1,usr1[4])
    brodcast1=get_brodcast(usr1,usr1[4])

    for i in range(len(usr1)-1):
        if(usr2[i]<net1[i] or usr2[i]>brodcast1[i]):
            print('Nu mai fii parnaie ca nu merg')
            return

    print('can communicate')

main()