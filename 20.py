# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко; ● D, G – 2 очка; ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка; ● K – 5 очков; ● J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко; ● Д, К, Л, М, П, У – 2 очка; ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка; ● Ж, З, Х, Ц, Ч – 5 очков; ● Ш, Э, Ю – 8 очков; ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо 
# только русские буквы.

letters_english = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
points_english  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   3,   3,   3,   3,   4,   4,   4,   4,   4,   5,   8,   8,   10,  10]
letters_russian = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ']
points_russian  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   4,   4,   5,   5,   5,   5,   5,   8,   8,   8,   10,  10,  10]


letters = letters_english + letters_russian
points = points_english + points_russian
word = input("Введите слово: ").upper()
word_list = list(word)
index = 0
sum = 0
for char in letters:
    for i in range(len(word_list)):
        if(word_list[i] == char): 
            # print(word_list[i],points[index])
            sum = sum + points[index]
    index += 1
print(f"Слово {word} имеет {sum} очков")