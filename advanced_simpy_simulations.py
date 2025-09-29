import simpy

env = simpy.Environment()

"""
Priority resource
"""

priotiry_teller = simpy.Priorityresource(env, capacity=1)

def priority_customer(env, name, priority, teller):
	print(f'{name} arrives at the bank at {env.now}')
    
    with teller.request(priority=priority) as req:
		yield req
        print(f'{name} starts being served at {env.now}')
        yield env.timeout(5)     
    		print(f'{name} leaves the bank at {env.now}')

#create a preemtive resource
#it's a resource that can be displaced and it's process interrupted by another process with more priority
	
preemptive_teller = simpy.PreemtiveResource(env, capacity = 1)
    
def preemptive_customer(env, name, priority, teller):
    print(f'{name} arrives at the bank at: {env.now}')
    with teller.request(priority=priority, preemt=True) as req:
    		
        #work untill interruption
        try:
    			yield req
            print(f'{name} starts being served at {env.now}')    
            yield env.timeout(5)
            print(f'{name} stops being served at: {env.now}')
        
        #interruption
        except simpy.Interrupt as interrupt:
            print(f'{name} is interrupted at {env.now} by {interrupt.cause}')
            
            
                
env.process(preemptive_customer(env, "Customer A", priority=1, teller=preemptive_teller))
env.process(preemptive_customer(env, "Customer B", priority=0, teller=preemptive_teller))
#higher priority, lower number.

env.Run(until = 10)
                
        		
            