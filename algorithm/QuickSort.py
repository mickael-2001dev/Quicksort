class QuickSort:

    def __init__(self, vector):

        if vector == None:
            raise Exception('Vetor Nulo!')
        elif len(vector) <= 1:
            raise Exception('Tamanho invalido!')
        else:
            self.__vector = vector

    def partition(self, start, end): 
    
        i = start - 1

        pivot = self.__vector[end]

        for j in range(start, end):
            
            if self.__vector[j] <= pivot:

                i = i+1
                self.__vector[i], self.__vector[j] = self.__vector[j], self.__vector[i]

        self.__vector[i+1], self.__vector[end]  = self.__vector[end], self.__vector[i+1]
       
        return (i+1)


    def sort(self, start, end):

        if start < end:
     
            partitionIndex = self.partition(start,end)

            self.sort(start, partitionIndex-1)
            self.sort(partitionIndex+1, end)
        
        return self.__vector


