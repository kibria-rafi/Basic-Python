# Define the list of strings
names_list = ["Shikha", "Haua", "Muzam", "01971700130"]

char1 =0
vowel_total=0
vowel ="aeiouAEIOU"

for item in names_list:
    char1 +=len(item)
    for char in item:
        if char in vowel:
           vowel_total +=1

print(f"Number of vowel : {vowel_total}")
print(f"number of character: {char1}")