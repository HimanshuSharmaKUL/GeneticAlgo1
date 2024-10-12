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

    def mate(self, parent2): #cross 
        child = []
        for i,j in zip(self.sentence, parent2.sentence):
            prob = random.random() #any value 0 to 1
            #check the corresponding letters of these two 
            if prob < 0.46:
                child.append(i)
            elif prob <0.90:
                child.append(j)
            else: #now we're gonna pick a random thing
                child.append(self.create_alpha())

        return sentence(child) #i.e. compute the child and then throw it back by making it a class instance
        pass

    def fitness(self):
        global Target
        fitness_score = 0
        for i,j in zip(self.sentence, Target): #we've to compare, target and the random sentence at the moment
            
            if i!=j :
                fitness_score = fitness_score +1
        return fitness_score #goes to the self.fitness() function in the atribute of the class



def main():

    global population_size #to have access of this variable inside main function
    population =[]
    generation = 1

    found = False
    for i in range(population_size) :

        sen = sentence.create_sentence() #we're calling create_sentence using 'instance method' not 'class method' as we've not created a class instance isse phele
        sen_obj = sentence(sen) #now we're creating an instance of the class
        population.append(sen_obj)
    #print(population)

    while not found:
        population = sorted(population, key= lambda x:x.fitness) #x is an instance inside the population[]. 'key' parameter requires a function, '.' we wanna sort acc to fitness values, we use this
        #now we want to check
        if population[0].fitness == 0 : #checking the fitness attribute of the object, 0th element would be most fit. so, checking the fittest solution
            found = True
            print(population[0].sentence)
            break
        
        new_population = [] 

        new_population.extend(population[0:10]) #appending the top 10 entries of population in the new_population, i.e. selecting the top 10 from previous population

        #for the rest of 90 entries
        for i in range(10,100): #now for the next population members, we'll mate the best 10 members of prev generation 
            parent1 = random.choice(population[:50]) #just selecting the parents from the top 50, ':' is starting, and '50' is ending
            parent2 = random.choice(population[:50])

            child = parent1.mate(parent2)
            print(child.sentence)
            new_population.append(child)
        
        population = new_population

        generation = generation +1
        print("Current generation is ", generation)




if __name__ == "__main__":
    main()
