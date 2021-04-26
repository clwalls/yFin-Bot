from wallstreet import Stock, Call, Put
import json
## function to parse userInput, we already remove the initial $
def parseUserInput(input):

  errMsg = 'Command not found: use $help'
  if input == '':
    return errMsg
  
  inputArr = firstParam = 0
  inputArr = input.split()
  firstParam = inputArr[0]
  commands = results = ''

  if firstParam == 'help':
    return 'ticker, delta, gamma, vega, theta, rho'

  if firstParam == 'call':
    if len(inputArr) == 5:
      try:
        s = Call(inputArr[1])

      except Exception as e:
        return 'Exception occured: Invalid call arguments', e
    return '$call [\'ticker-name\'] [\'days\'] [\'month\'] [\'year\'] [\'strike\']' 
  

  if firstParam == 'ticker':
    if len(inputArr) >= 2:
      try: 
        s = Stock(inputArr[1])
        return s, s.change, s.last_trade
      except Exception as e: 
        return 'Exception occured: Invalid ticker', e
    return '$ticker [\'ticker-name\']'
  
  ## end parseUserInput
  return errMsg