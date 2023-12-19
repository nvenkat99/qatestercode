def count_match_func(arr,x):
                            count =0                        //set the counter to zero 
                            i=0                             // set the array positions, starting from left to 0 
                            j=len(arr)-1                    // set the array positions startng from last / right to length minus one

                            while i < j :                                       //while this condition applies 
                                        sum = arr[i] + arr[j]               //asking the python to sum up first 2 numbers in the array 

                                        if sum = x :                            //if the sum up matches with x  
                                                    count += 1                      // counter will go up by 1
                                                    i += 1                          // the array position will move by 1 position to its right 
                                                    j -= 1                          // the array position will move by one position to its left 
                            
                                       elif sum < x :                       // if sum of those values is less than X 
                                                    i += 1                  // increment the left pointer in array by 1
                                       else :
                                                    j -= 1                  // if the above condition is not valid then decrement the counter of right side array element by 1
                            
                            return count                                    //return the final count 


//example

//arr = [1,2,3,4,5,6]
// arr[0] = 1, arr[1] = 2, sum of them = 3 which is matching with a[2] however, we cant repeat those values again to do sum 
//so the next values are 3 and 4 and we dont have a matching x here so the count = 1 for this array 
//assumptions : array is sorted so we started counter from oth position 
//assumptions : array reads from left 
//this function takes 2 paramters 

           
