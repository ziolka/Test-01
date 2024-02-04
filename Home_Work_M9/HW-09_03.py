def caching_fibonacci():
    cache = {}
    print(cache) 
        
    def fibonacci(n):
        print(cache.keys())
        if n in cache.keys():
            print("+++")
            result = cache.get(n)
            
        else:
            print("---")
            if n <= 1:
                print(f'n: {n}')
                result = n
                print(f'result: {result}')
                cache.update({n: result})
                
            else:
                print(f'n powyżej 1: {n}')
                result = fibonacci(n-1) + fibonacci(n - 2)
                print(f'result: {result}')
                cache.update({n: result})
        return result
        
    return fibonacci
