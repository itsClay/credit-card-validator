"""
Credit Card Validator - Takes in a credit card number from a
common credit card vendor (Visa, MasterCard, American Express,
Discoverer) and validates it to make sure that it is a valid
number (look into how credit cards use a checksum).
This program works with *most* credit card numbers.
Uses Luhn Algorithm (http://en.wikipedia.org/wiki/Luhn_algorithm).
1. From the rightmost digit, which is the check digit, moving
left, double the value of every second digit; if product of this
doubling operation is greater than 9 (e.g., 7 * 2 = 14), then
sum the digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5).
2. Add together doubled digits with the undoubled digits from the
original number.
This procedure can be changed as: num (>9) - 9
3. If the total modulo 10 is equal to 0 (if the total ends in zero)
then the number is valid according to the Luhn formula; else it is
not valid.
"""

if __name__ == '__main__':
	number = raw_input('Enter credit card number to check: ').replace(' ', '')
	digits = [int(char) for char in number]
	digits = digits[::-1]

	# step 1: double alternating digits
	doubled = []
	for (i, digit) in enumerate(digits):
		if (i + 1) % 2 == 0:
			doubled.append(digit * 2)
		else:
			doubled.append(digit)

	# step 2: take away 9 from all numbers larger than 10
	summed = []
	for num in doubled:
		if num < 10:
			summed.append(num)
		else:
			summed.append(num-9)

	# step 3: add all the numbers together and divide
	if sum(summed) % 10 == 0:
		print 'The number is valid'
	else:
		print 'The number is invalid'

