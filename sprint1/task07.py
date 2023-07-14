def Cipher_Zeroes(N):
    visible_zero_dict = {0: 1, 1: 0,2: 0,3: 0,4: 0,5: 0, 6: 1,7: 0,8: 2, 9: 1}
    visible_zero = sum([visible_zero_dict.get(int(i)) for i in N])
    if visible_zero%2==0 and visible_zero>0:
        visible_zero -=1
    elif visible_zero%2==1:
        visible_zero +=1

    if visible_zero < 0:
        return 0
    return bin(visible_zero)[2:]

print (Cipher_Zeroes("4"))