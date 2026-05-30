# Kitob do'konidagi kitoblar sonini hisoblash dasturi
# Kurs: IT Dasturlash
# Mavzu: 1-mavzu: Python va dasturlashga kirish
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
kitob_soni = int(input())
kitob_turlari_soni = int(input())
kitoblar_soni = list(map(int, input().split()))
print(sum(kitoblar_soni))