class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # interval_number=[]
        # m=0
        # h=0
        # if flowerbed[0]==1:
        #     interval_number.append(0)
        # else:
        #     m+=1
        #     if len(flowerbed)==1:
        #         interval_number.append(m)
        # for i in range(1,len(flowerbed)):
        #     if flowerbed[i]==1:
        #         interval_number.append(m)
        #         interval_number.append(0)
        #         m=0
        #     elif flowerbed[i] !=1 and i== len(flowerbed)-1:
        #         m+=1
        #         interval_number.append(m)
        #     else:
        #         m+=1
        #     i+=1
        # # return interval_number
        # if interval_number[0] == 0 and interval_number[-1] == 0:
        #     for j in range(len(interval_number)):
        #         if interval_number[j]<=2:
        #             h+=0
        #         if interval_number[j]>2 and interval_number[j]%2 == 0:
        #             h += (interval_number[j]-1) // 2
        #         if interval_number[j]>2 and interval_number[j]%2 != 0:
        #             h+= interval_number[j] // 2
        #         j+=1
        # if interval_number[0] != 0 and interval_number[-1] == 0:
        #     h+=interval_number[0]//2
        #     for j in range(1,len(interval_number)):
        #         if interval_number[j]<=2:
        #             h+=0
        #         if interval_number[j]>2 and interval_number[j]%2 == 0:
        #             h += (interval_number[j]-1) // 2
        #         if interval_number[j]>2 and interval_number[j]%2 != 0:
        #             h+= interval_number[j] // 2
        #         j+=1
        # if interval_number[0] == 0 and interval_number[-1] != 0:
        #     h+=interval_number[-1]//2
        #     for j in range(len(interval_number)-1):
        #         if interval_number[j]<=2:
        #             h+=0
        #         if interval_number[j]>2 and interval_number[j]%2 == 0:
        #             h += (interval_number[j]-1) // 2
        #         if interval_number[j]>2 and interval_number[j]%2 != 0:
        #             h+= interval_number[j] // 2
        #         j+=1
        # if interval_number[0] != 0 and interval_number[-1] != 0:
        #     if len(interval_number) == 1:
        #         if interval_number[-1]%2 == 0:
        #             h= interval_number[-1]//2
        #         else:
        #             h = (interval_number[-1]+1)//2
        #     else:
        #         h+=interval_number[-1]//2
        #         h+=interval_number[0]//2
        #         for j in range(1,(len(interval_number)-1)):
        #             if interval_number[j]<=2:
        #                 h+=0
        #             if interval_number[j]>2 and interval_number[j]%2 == 0:
        #                 h += (interval_number[j]-1) // 2
        #             if interval_number[j]>2 and interval_number[j]%2 != 0:
        #                 h+= interval_number[j] // 2
        #             j+=1
        # if h>=n:
        #     return True
        # else:
        #     return False

        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n


            