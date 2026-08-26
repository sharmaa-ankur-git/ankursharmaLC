class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}  
        result = []
        for name in names:
            if name not in seen:
                seen[name] = 1  
                result.append(name)
            else:
                k = seen[name]
                while True:
                    new_name = f"{name}({k})"
                    if new_name not in seen:                        
                        seen[name] = k + 1  
                        seen[new_name] = 1  
                        result.append(new_name)
                        break
                    k += 1
        
        return result
        