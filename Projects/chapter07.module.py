from urllib import request

target = request.urlopen("http://google.com")
output = target.read()

print(output)
print()

list_a=[1,2,3]
print('#리스트에 뒤에 요소 추가하기')

