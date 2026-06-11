# Shaxsiy hisob kitobini avtomatlashtirish dasturi
# Kurs: Dasturlash / IT
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
daromad = int(input())
xarajatlar = list(map(int, input().split(',')))
jami_xarajat = sum(xarajatlar)
qolgan = daromad - jami_xarajat
print(f"Daromad: {daromad}")
print(f"Xarajatlar: {jami_xarajat}")
print(f"Qolgan pul: {qolgan}")