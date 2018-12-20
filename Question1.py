def fib(n):
	a=1
	b=1
	i=0
	sum=0
	while i<n:
		i=a+b
		a=b
		b=i
		if i%2==0:
			sum+=i
	return(sum)

print(fib(4000000))


