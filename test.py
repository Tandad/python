#斐波那契数列函数
def fibo(count):
	result = 0
	num = 1
	passnum = 0
	if count == 1:
		outList(result)
	elif count == 2:
		outList(result)
		result = result + num
		outList(result)
	else:
		outList(result)
		result += num
		outList(result)
		for i in range(2,count+1):
			outList(result)
			passnum = result
			result += num
			num = passnum
		pass
	pass
#斐波那契函数结束
#更厉害的菲薄
import time
def fbis(num):
	outList(num)
	result = [0,1]
	for i in range(num-2):
		result.append(result[-2]+result[-1])
		outList(result[-1])
	return result
	pass

def outList(some):
	print(some)
	print()
	pass

#主函数
def main():
	count = int(input("你要计算多少个？"))
	result = fbis(count)
	fobj = open('F:\\Code\\python\\result.txt', 'w+')
	for i, num in enumerate(result):
		print("第%d个数是：%d" % (i+1, num))
		fobj.write("\n%d\n"%num)
		time.sleep(1)
	pass
#主函数结束

# if __name__ = '__main__':
# 	main()
main()