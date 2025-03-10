class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        a=self.value
        return a 

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        if self.value%2!=0:
            ans=True
        else:
            ans=False
        return ans

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        if self.value%2==0:
            ans=True
        else:
            ans=False
        return ans

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        from math import sqrt
        a = 0
        if(self.value > 1):
	        for i in range(2, int(sqrt(self.value)) + 1):
		        if (self.value % i == 0):
			        a= 1
	        if (a == 0):
                    ans=True
	        else:
                    ans=False
        else:
            ans=False
        return ans

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        a=[]
        for i in range(1, self.value+1):
            if self.value%i==0:
                a.append(i)
        return a

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        return len(str(self.value))

    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        a = self.value%10
        while self.value != 0:
            self.value //= 10
            a += self.value%10
        return a

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        rn=0
        while self.value!=0:
            digit=self.value%10
            rn=10*rn
            rn=rn+digit
            self.value=self.value//10
        return rn

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        if str(self.value)==str(self.value)[::-1]:
            ans=True
        else:
            ans=False
        return ans

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        a=str(self.value)
        return [int(i) for i in a]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        a = [self.value%10]
        while self.value != 0:
            self.value //= 10
            a.append(self.value%10)
        b=list(reversed(a))[1:len(a)]
        c=max(b)
        return c

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        a = [self.value%10]
        while self.value != 0:
            self.value //= 10
            a.append(self.value%10)
        b=list(reversed(a))[1:len(a)]
        c=min(b)
        return c

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        a=str(self.value)
        sum=0
        for i in a:
            sum+=int(i)
        return sum/len(a)
        

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        import statistics
        a = [self.value%10]
        while self.value != 0:
            self.value //= 10
            a.append(self.value%10)
        b=list(reversed(a))[1:len(a)]
        c=statistics.median(b)
        return c

    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        c=[]
        c.append(min(map(int, str(self.value))))
        c.append(max(map(int, str(self.value))))
        return c

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        c={}
        if self.value==0:
            c.update({0:1})
        else:
            a = [self.value%10]
            while self.value != 0:
                self.value //= 10
                a.append(self.value%10)
            b=list(reversed(a))[1:len(a)]
            for i in b:
                c.update({i: b.count(i)})
        return c
    

# Create a new instance of Number
number = Number(6746864446)
print(number.get_frequency())