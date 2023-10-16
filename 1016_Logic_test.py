def list_character_swap(Score):
    for i in range(len(Score)): 
        if Score[i] >= 10: #需大於2位數
            num_str = str(Score[i])
            Score[i] = int(num_str[-1] + num_str[1:-1] + num_str[0]) #第一跟最後一個字符交換
    return Score

def count_letters(text):
    
    text = sorted(text.lower()) #將所有字母轉換為小寫並排序
    count = {}
    for t in text:
        if t != " ": #去除空格
            count[t] = count.get(t, 0) + 1

    return count

def josephus(n, k): #參考"https://openhome.cc/zh-tw/algorithm/randomness/josephus/" & "https://theriseofdavid.github.io/2021/05/21/Explain_Algorithm/josephus/"
    s = 0  #一開始的編號
    for i in range(2, n + 1):
        s = (s + k) % i  #第i輪中 倖存者的位置是第s個
    return s + 1  #加1代表第1個

print("The 1st question: ")
print(list_character_swap([35, 46, 57, 91, 29]))

print("The 2nd question: ")
#print(count_letters('Hello welcome to Cathay 60th year anniversary'))
ans = count_letters('Hello welcome to Cathay 60th year anniversary')
for t, c in ans.items():
    print(t,": ",c,"次")

print("The 3rd question: ")
print(josephus(41,3))


