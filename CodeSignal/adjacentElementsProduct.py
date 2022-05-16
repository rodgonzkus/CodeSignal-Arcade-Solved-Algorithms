def solution(inputArray):
    products = list()
    for i in range(0, len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        products.append(product)
    return max(products)   