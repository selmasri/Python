

def test_execute_addition():
  # setup
  x = 5
  y = 4
  expected = x + y

  # invoke
  actual = calculator.execute("+", x, y)

  # analyze
  assert (expected == actual) 


