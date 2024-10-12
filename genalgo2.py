import random

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

population_size = 100 #number of iterations

Target = "I love Python"

class sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.fitness = self.fitness()
        pass

    @classmethod #'.' we're using it inside create_sentence, so we need to declare this also as class method if we want to use this also without creating an instance of class
    def create_alpha(self): #to draw characters from the GENES
        
        global GENES #to make GENES avilable in this scope
        
        alpha = random.choice(GENES)

        return alpha

    @classmethod #so that create_sentence is not tied up to its class, and we can use it outside of the class as well
    def create_sentence(self):

        global Target

        len_Target = len(Target)
        sen = [self.create_alpha() for i in range(len_Target)]
        
        return sen

    def mate(self): #cross 
        pass

    def fitness(self):
        pass


def main():

    global population_size #to have access of this variable inside main function
    population =[]

    found = False
    for i in range(population_size) :

        sen = sentence.create_sentence() #we're calling create_sentence using 'instance method' not 'class method' as we've not created a class instance isse phele
        sen_obj = sentence(sen) #now we're creating an instance of the class
        population.append(sen_obj)
    print(population)

    while not found:
        population = sorted(population, key= lambda x:x.fitness) #x is an instance inside the population[]. 'key' parameter requires a function, '.' we wanna sort acc to fitness values, we use this
        pass


if __name__ == "__main__":
    main()
