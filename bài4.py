N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

so_lon_thu_nhi = None
for so in a:
    if so < a[0]:
        so_lon_thu_nhi = so
        break
print(so_lon_thu_nhi)

#vd:
#nhap input: 5
#           10 4 7 22 15
#-------> output: 15