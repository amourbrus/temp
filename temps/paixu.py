# 选择排序
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i]<smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selected_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest_index = findSmallest(array)
        new_array.append(array.pop(smallest_index))
    return new_array
print(selected_sort([3,5,6,7,23,2]))

# 快速排序
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # 以第一个作为基准
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,8,1,3]))


def bubble_sort(alist):
	"""冒泡排序，重复遍历要排序的数列，一次比较两个元素
	１，从头开始，比较相邻的元素，如果第一个大，就交换
	２，继续后一对相邻的元素，直到最后一对，执行完最后的元素就是最大的数
	３，重复执行以上动作，除了最后一个，直到没有元素需要排序

	"""
	for j in range(len(alist)-1,0,-1):   # 表示每次遍历需要比较的次数，是递减的
		for i in range(j):
			if alist[i] > alist[i+1]:   # 升序 asc
				alist[i],alist[i+1] = alist[i+1],alist[i]


li = [54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)


def selection_sort(alist):

	"""选择排序
	１，在序列中找到最小（升序）的元素，存放到排序序列的起始位置
		２，在从余下数据中找到最小的，放到刚才排的序列后面，以此类推
	"""

	for i in range(len(alist)-1):  # 需要执行n-1次操作
		min_index = i
		for j in range(i+1,n):  # 从i+1位置到末尾选择出最小的数据
			if alist[j] < alist[min_index]:
				min_index = j
		# 如果选择出的数据不在假设位置，进行交换
		if min_index != i:
			alist[i], alist[min_index] = alist[min_index],alist[i]

li = [54,26,93,17,77,31,44,55,20]
selection_sort(li)
print(li)



def insert_sort(alist):
"""插入排序,对前面的数都进行比较,重点时扫描
构建有序序列，对于未排序数据，在已排序序列中从前向后扫描，找到相应位置插入
需要反复把已排元素逐步向后挪位，为最新元素提供空间
"""
	for i in range(1,len(alist)):
		# 从第i　个元素开始向前比较，如果小于前一个，交换位置
		for j in range(i,0,-1):
			if alist[j]<alist[j-1]:
				alist[j],alist[j-1] = alist[j-1],alist[j]

li = [54,26,93,17,77,31,44,55,20]
insert_sort(li)
print(li)


def quick_sort(alist,start,end):
	"""快速排序

	"""
	if start >= end:
		return
	mid = alist[start]
	low = start
	high = end
	while low<high:
		while low<high and alist[high]>= mid: # 找到所有high元素中比start大的
			high -= 1
		alist[low] = alist[high]
		while low<high and alist[low] < mid: # 找到所有
			low+= 1
		alist[high]=alist[low]
	alist[low] = mid


			
