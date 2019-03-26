#字符串包含
#给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。请问，如何最快地判断字符串B中所有字母是否都在字符串A里？
#为了简单起见，我们规定输入的字符串只包含大写英文字母，请实现函数bool StringContains(string &A, string &B)
#比如，如果是下面两个字符串：
#String 1：ABCD
#String 2：BAD
#答案是true，即String2里的字母在String1里也都有，或者说String2是String1的真子集。
#如果是下面两个字符串：
#String 1：ABCD
#String 2：BCE
#答案是false，因为字符串String2里的E字母不在字符串String1里。
#同时，如果string1：ABCD，string 2：AA，同样返回true。

def string_contain(str1, str2):
    hash_map = {}
    for v in str1:
        hash_map[ord(v)] = True
    
    for v in str2:
        key = ord(v)
        if key not in hash_map.keys():
            return False
    return True

str1, str2 = 'fdasfdafd', 'chenp'
print(string_contain(str1, str2))

str1, str2 = 'fdasfdafd', 'dafs'
print(string_contain(str1, str2))