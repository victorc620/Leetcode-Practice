class Solution:
    def romanToInt(self, s: str) -> int:

        answer = 0
        i = 0
        while i < len(s):
 
            # V = 5
            if s[i] == "V":
                current_num = 5
                i+=1
            
            # L = 50
            elif s[i] == "L":
                current_num = 50
                i+=1
            
            # D = 500
            elif s[i] == "D":
                current_num = 500
                i+=1
                
            # M = 1000
            elif s[i] == "M":
                current_num = 1000
                i+=1
            
            # C = 100, CD = 400, CM = 900
            elif s[i] == "C":
                if i+1 == len(s):
                    current_num = 100
                    i+=1
                elif s[i+1] == "D":
                    current_num = 400
                    i+=2
                elif s[i+1] == "M":
                    current_num = 900
                    i+=2
                else:
                    current_num = 100
                    i+=1
            
            # X = 10, XL = 40, XC =90 
            elif s[i] == "X":
                if i+1 == len(s):
                    current_num = 10
                    i+=1
                elif s[i+1] == "L":
                    current_num = 40
                    i+=2
                elif s[i+1] == "C":
                    current_num = 90
                    i+=2
                else:
                    current_num = 10
                    i+=1
            
            # I = 1, IV = 4. IX =9
            elif s[i] == "I":
                if i+1 == len(s):
                    current_num = 1
                    i+=1
                elif s[i+1] == "V":
                    current_num = 4
                    i+=2
                elif s[i+1] == "X":
                    current_num = 9
                    i+=2
                else:
                    current_num = 1
                    i+=1
            else:
                print(f"{s[i]} is not a valid roman number")
                exit()
                      
            answer += current_num

        
        return answer