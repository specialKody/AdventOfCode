from typing import List

### Methods

def readExpenseReport() -> List[int]:
	expenses = []
	with open("expenseReport.txt") as file:
		for expense in file:
			expenses.append(int(expense))
	return expenses

def determinePairedValues(targetSum: int, expenses: List[int]) -> int:
	seenValues = set()
	
	for expense in expenses:
		if (targetSum - expense) in seenValues:
			return (targetSum-expense) * expense
		else:
			seenValues.add(expense)
	return -1
	
def determineNValues(targetSum: int, expenses: List[int], numberOfExpenses: int) -> int:
	if numberOfExpenses == 2:
		return determinePairedValues(targetSum, expenses)
	else:
		for expense in expenses:
			attempt = determineNValues((targetSum - expense), expenses, numberOfExpenses-1)
			if attempt != -1:
				return attempt * expense
				
	
### Execution

expenses = readExpenseReport()
answer = determineNValues(2020, expenses, 3)

print(answer)