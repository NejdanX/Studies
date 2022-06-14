count_treat = int(input())
count_vid = int(input())
o = 0
sh = 0
led = 0
for i in range(count_treat * count_vid):
    string = input()
    if("леденец" in string or "леденцы" in string):
        led += 1
    if("орех" in string):
        o += 1
    if("шоколад" in string):
        sh += 1
if(o > sh and o > led):
    print(o)
    if(sh > led):
        print("орех", "шоколад", "леденец")
    else:
        print("орех", "леденец", "шоколад")
elif(sh > o and sh > led):
    print(sh)
    if(o > led):
        print("шоколад", "орех", "леденец")
    else:
        print("шоколад", "леденец", "орех")
elif(led > sh and led > o):
    print(led)
    if(sh > o):
        print("леденец", "шоколад", "орех")
    else:
        print("леденец", "орех", "шоколад")
elif(sh == o and sh == led):
    print(sh)
    print("леденец", "орех", "шоколад")
    