class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen={}
        result=[]
        n=len(names)
        for file in names:
            if file in seen:
                k=seen[file]
                new_name=f"{file}({k})"
                while new_name in seen:
                    k+=1
                    new_name=f"{file}({k})"
                seen[file]=k+1
                seen[new_name]=1
                result.append(new_name)
            else:
                seen[file]=1
                result.append(file)
        return result
        







        