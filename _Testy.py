def caching_fibonacci():
    cache = {}
    print(cache)    
    
    def fibonacci(n):
        if n <= 1:
            print(n)
            result = n
            cache.update({n: result})
            return result 
        else:
            print(n)
            result = cache.get(n-1) + cache.get(n - 2)
            cache.update({n: result})
            return result
            
    return fibonacci

fibo = caching_fibonacci()

for i in range(0,10):
    print(fibo(i))


    def caching_fibonacci():
    cache = {}
        
    def fibonacci(n):
        print(cache.keys())
        if n in cache.keys():
            print("+++")
            result = cache.get(n)
            return result
        else:
            print("---")
            if n <= 1:
                print(f'n: {n}')
                result = n
                cache.update({n: result})
                return result
            else:
                print(f'n: {n}')
                print(f'n-1: {cache.get(n-1)}')
                print(f'n-2: {cache.get(n-2)}')
                result = cache.get(n-1) + cache.get(n - 2)
                print(f'result: {result}')
                cache.update({n: result})
                return result
        
    print(cache)                  
    return fibonacci

fibo = caching_fibonacci()
for i in range(0,5):
    print(fibo(i))