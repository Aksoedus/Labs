# # m=int(input())
# # print(f"\x1b[48;2;255;255;255m{m*" "}\x1b[0m\n\x1b[48;2;255;255;255m{m*" "}\x1b[0m \n\x1b[48;2;255;0;0m{m*" "}\x1b[0m \n\x1b[48;2;255;0;0m{m*" "}\x1b[0m")
# # 
# # m=int(input())
# # n=int(input())
# # print(f"\x1b[48;2;255;255;255m{m*" "}\x1b[0m")
# # print(f"\x1b[48;2;255;255;255m{m*" "}\x1b[0m")
# # for i in range(n):
# #     for x in range(0,8):
# #         tab1="\t"*4
# #         tab2="\t"*2
# #         if x==2 or x==3 or x==6 or x==7:
# #             print(f"\x1b[48;2;255;255;255m{m*" "}\x1b[0m")
# #         elif x==0 or x==1:
# #             print(f"{tab1}\x1b[48;2;255;255;255m   \x1b[0m"*(m//16))
# #         else:
# #             print(f"\t\t\x1b[48;2;255;255;255m   \x1b[0m"+f"{tab1}\x1b[48;2;255;255;255m   \x1b[0m"*(m//16))


# import time
# import os


# print("Введите размер:")

# rad=int(input())
# h = 2 * rad + 1

# def col(rad):
#     colors=[]
#     for i in range(0,255,255//5):
#         color=f"\033[48;2;255;{i};{i}m"
#         colors.append(color)
#     return colors

# def figura(rad,v):
#     result=[]
#     for i in range(-rad,rad):
#         line=""
#         for j in range(-rad,rad):
#             if (i*2.6)**2+j**2 <= rad**2-1 :
#                 line+=f"{v} \033[0m"
#             else:
#                 line+=" "
#         result.append(line)
#     return "\n".join(result)

# colors = col(rad)
# os.system("cls")

# while True:
#     for v in colors:
#         print("\x1b[H", end="")   
#         print(figura(rad, v), flush=True)
#         time.sleep(0.05)

# with open(r"C:\Users\Alex\Documents\Labs\sequence.txt", "r") as f:
#     spisok=[abs(float(x)) for x in f.read().split()]

# sr_znach1=round(sum((spisok)[0:125])/len((spisok)[0:125]),5)
# sr_znach2=sum((spisok)[125:250])/len((spisok)[125:250])
# summ=round(sr_znach2+sr_znach1,6)


# procent2=round((sr_znach2*100)/summ)
# procent1=100-procent2

# def bar(procent1,procent2):
#     red=f"\x1b[48;2;255;0;0m{' '*procent1}\x1b[0m"
#     blue=f"\x1b[48;2;0;0;255m{' '*procent2}\x1b[0m"
#     return red+blue
# print(f"Первые 125: среднее по модулю = {sr_znach1}, что составляет {(sr_znach1*100)/summ} примерно: {procent1}%")
# print(f"Вторые 125: среднее по модулю = {sr_znach2}, что составляет {(sr_znach2*100)/summ} примерно: {procent2}%")
# print()
# print(bar(procent1,procent2),f"процентное соотношение ср.арифметич. для первых 125 и вторых 125: {procent1}/{procent2}%")
# print(bar(procent1,procent2),f"процент для первых 125: {procent1}%")
# print(bar(procent2,procent1),f"процент для вторых 125: {procent2}%")


# y = int(input())

# def goto(r, c):
#     return f"\x1b[{r};{c}H"

# out = "\x1b[2J\x1b[H"


# for y1 in range(1,y+1):
#     r =y - y1 
#     c =y1**2
#     out += goto(r, c) + "\x1b[48;2;0;0;255m \x1b[0m"

# print(out)
