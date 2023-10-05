def div_and_mod(ax,bx):  
    a = ax[-1::-1]
    b= bx[-1::-1]
    dec_a = int(a,2)
    dec_b = int(b,2)
    bin_a = bin(dec_a)[2:]
    bin_b = bin(dec_b)[2:]
    dec_thuong = 0
    while len(bin_a) >= len(bin_b) and (dec_a != 0):
        dec_thuong = dec_thuong+(1<<(len(bin_a)-len(bin_b))) #thương = thương + x^(bậc a(x) - bậc b(x))
        dec_a = dec_a^(dec_b<<(len(bin_a)-len(bin_b))) # a(x) = a(x) - x^(bậc a(x) - bậc b(x))*b(x)
        bin_a = bin(dec_a)[2:] # gán lại giá trị bin_a khi dec_a thay đổi
    return bin(dec_thuong)[2:][-1::-1],bin_a[-1::-1] # trả về thương và dư 

def add(a,b):
    res = ''
    for i in range(min(len(a),len(b))):
        if (a[i]!=b[i]):
            res=res+'1'
        else: 
            res=res+'0'
    for i in range(len(a),len(b)):
        res = res+b[i]
    for i in range(len(b),len(a)):
        res = res+a[i]
    return res
def getW(a):
    count =0
    for i in a:
        if i=='1':
            count+=1
    return count
n = int(input('Nhập vào n:'))
k = int(input('Nhập vào k:'))
g = input('Nhập vào gx: ')
print('Repair nhập 0, Encypt thì nhập 1:')
choice = int(input())
if (choice==0):
    cipher = input('Nhập vào tin thu được: ')
    tmp=div_and_mod(cipher,g)
    if tmp[1]=='0':
        print('Bản sau khi sửa=',cipher)
    else:
        count =1
        cipher = cipher[-1:]+cipher[0:-1]
        tmp = div_and_mod(cipher,g)
        while(getW(tmp[1])>(n-k)//2):
            count +=1
            cipher = cipher[-1:]+cipher[0:-1]
            tmp = div_and_mod(cipher,g)
        res = add(cipher,tmp[1])
        print(res)
        res = res[count:]+res[0:count]
        print('Bản sau khi sửa=',res)
else:
    plain = input('Nhập vào bản rõ: ')
    tmp = div_and_mod('0'*(n-k)+plain,g)
    print('Bản mã = ',add('0'*(n-k)+plain,tmp[1]))
https://drive.google.com/drive/mobile/folders/13T4DcERtfugxdU9tSM4rUJACdLOZfBA8/1RF84HZblWU0V2TSWUR9OU2xcCKBhHncG?usp=sharing&fbclid=IwAR2Aj3YbK-Jk9cbZCT_IX8yf9URAXyHGKeEe8AcDRsbMbd2_X78Nhw5vAo4&sort=13&direction=a
        
