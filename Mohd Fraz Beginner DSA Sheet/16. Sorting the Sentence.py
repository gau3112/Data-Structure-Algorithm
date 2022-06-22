    def sortSentence(self, s: str) -> str:
        s_list = s.split()
        index = 0
        while index<len(s_list):
            if int(s_list[index][-1]) == index+1:
                s_list[index] = s_list[index][0:len(s_list[index])-1]
                index+=1
            else:
                index_found = int(s_list[index][-1])-1
                s_list[index],s_list[index_found] = s_list[index_found],s_list[index]
                
        s = " "
        s = s.join(s_list)
        return s
