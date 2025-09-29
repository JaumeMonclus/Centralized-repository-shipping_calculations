pip install simpy

env = simpy.Environemnt()


#creatre our firs easy function

def process_example(env):
    print(f'Machine starts at {env.now}')
    yield env.timeout(5)
    print(f'Machine stops at {env.now)')
    

def machine(env):
    
    #create a first machine
    print(f'Machine starst now {env.now}')
    yield env.timeout(3)
    print(f'Machine stops now: {env.now}')
    
    #let's create our first resource
    resource = simpy.Resource(env, capacity=1)
    with resource.request() as req:
		
        #wait until the resource is available
        yield req
        
        #use the resource 3 units of time
        yield env.timeout(3)
        
def proccess_with_explicit_request(env, resource):
    
    #acquire the resource
    req = resource.request()
    yield req
    print(f'resource has been aquired at: {env.now}')
    
    #use the resource for 5 units of time
    
    yield env.timeout(5)
    print(f'the resouce has been used for five UT starting at: {env.now}')
    #release the resource explicitely
    
    resource.release(req)
    print(f'The resource has been released at: {env.now}')
    

#simulation in simpy

env = simpy.Enviroment()
resource = simpy.Resource(env,capacity = 1)
env.process(process_with_explicit_request(env, resource))
env.run(until=10)


