line = float(input())
n = int(input())
error_cnt = 0
line_cnt = 0
sum_grad = 0.0
max_grad = -(10**10)
for i in range(n):
    grad = input()
    if grad == "error":
        error_cnt += 1
    else:
        grad = float(grad)
        sum_grad += grad
        if grad > line:
            line_cnt += 1
        if grad > max_grad:
            max_grad = grad
print(n, error_cnt, line_cnt, f"{max_grad:.1f}", f"{sum_grad/(n-error_cnt):.1f}", sep="\n")
