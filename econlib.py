"""
calculates the expected value of [lottery] where [lottery] is a list of tuples
where index 0 represents the payoff and index 1 represents the probability of
said payoff being realized. 

Example: expected_value([(2,0.5), (3,0.5)]) = 2.5

Requires that: 
– input is a list of tuples
– the sum of probabilities (second index of tuples) be 1
– payoffs and probabilites be ints or float
- the count of each tuple is 2 
"""
def expected_value(lottery):
  assert type(lottery) == list, "input must be a list"
  p_count = 0
  for e in lottery:
    t = type(e[0])
    assert t == int or t == float, "payoffs and probabilites be ints or float"
    p_count += e[1]
  assert p_count == 1, "probabilities must sum to 1"

  ev = 0 

  for e in lottery: 
    ev += (e[1] * e[0])
  
  return ev

"""
propect theory
"""
def prospect_eval(lottery, prob, valuation):
  pass 
  