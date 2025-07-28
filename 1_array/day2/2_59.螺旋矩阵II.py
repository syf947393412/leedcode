from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_i,start_j=0,0 #!
        offset=1
        nums = [[0 for _ in range(n)] for _ in range(n)] #!二维矩阵的初始化
        count=0

        while start_i<=n-offset:   #!循环终止条件的确定

            for j in range(start_j,n-offset): #!
                count+=1
                nums[start_i][j]=count
            for i in range(start_i,n-offset):
                count+=1
                nums[i][n-offset]=count   #!用n-offset控制坐标
            for j in range(n-offset,start_j,-1):
                count += 1
                nums[n-offset][j] = count
            for i in range(n-offset,start_i,-1):
                count += 1
                nums[i][start_j] = count

            start_j+=1
            start_i+=1
            offset+=1
        if n%2==1:  #!  /    //   % 的区别
            count+=1
            nums[start_i-1][start_j-1] = count

        return nums



    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_x=0
        start_y=0

        stop_x=len(matrix)  #3
        stop_y=len(matrix[0])#4

        offset=1



        list=[]

        while start_x<=stop_x-offset and start_y<=stop_y-offset:  #! 更通用
            for j in range(start_y,stop_y-offset):
                list.append(matrix[start_x][j])

            for i in range(start_x,stop_x-offset):
                list.append(matrix[i][stop_y-offset])

            for j in range(stop_y-offset,start_y,-1):
                list.append(matrix[stop_x-offset][j])

            for i in range(stop_x-offset,start_x,-1):
                list.append(matrix[i][start_y])

            start_x+=1
            start_y+=1
            offset+=1

        if stop_x==stop_y and stop_x%2==1:   #!
            list.append(matrix[start_x][start_y])

        return list



s=Solution()
n=1
nums=s.generateMatrix(n=n)
print(nums)


# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# list=s.spiralOrder(matrix=matrix)
# print(list)



