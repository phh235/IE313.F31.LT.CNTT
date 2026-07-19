# Phan Huy Hoàng - 25410219
import random as rd

def compare(human, bot):
    if human == bot:
        return "Hòa"
    elif (human == "kéo" and bot == "bao") or \
         (human == "búa" and bot == "kéo") or \
         (human == "bao" and bot == "búa"):
        return "Người thắng"
    return "Máy thắng"

human = input("Người nhập (kéo/búa/bao): ")

while human not in ["kéo", "búa", "bao"]:
    human = input("Nhập lại (kéo/búa/bao): ")

bot = rd.choice(["kéo", "búa", "bao"])

print("Máy ra:", bot)
print("Kết quả:", compare(human, bot))