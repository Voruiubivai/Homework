
# coding: utf-8

# # Roman numerals

# ## I. Roman numerals to decimals
# 
# Write a function which receives a Roman numeral written out as a string, and returns an integer representing the decimal form of the input number. 

# In[1]:


d = {"I" : 1, 
           "V" : 5,
           "X" : 10,
           "L" : 50,
           "C" : 100,
           "D" : 500,
           "M" : 1000}


# In[2]:


def roman_to_decimal(s):
    #from IPython.core.debugger import Tracer; Tracer()()
    ss=0
    r=0
    for i in range(0,len(s)):
        if r==d[s[i]]:
            continue
        if s[i] in d:
            if i!=len(s)-1:
                if d[s[i+1]]>d[s[i]]:
                    r= d[s[i+1]]
                    ss=ss+d[s[i+1]]- d[s[i]]  
                else:
                    ss=ss+d[s[i]]
            else:
                ss=ss+d[s[i]]  
    return ss


# Проверка данных примеров и несколько своих
# 

# In[16]:


test_pairs = [("IX", 9), ("XI", 11), ("MCCII", 1202), ("MMXVIII", 2018), ("XLIX", 49), ("MCMLXXXIV", 1984), ("MDCCCXXVIII", 1828), ("MMMDCCCLXXXVIII", 3888)]

for rom, dec in test_pairs:
    converted = roman_to_decimal(rom)
    print(converted == dec)
    print(converted)


# ## II. Decimal numbers to roman numerals.
# 

# In[12]:


numerals = [
        {'letter': 'M', 'value': 1000},
        {'letter': 'CM', 'value': 900},
        {'letter': 'D', 'value': 500},
        {'letter': 'C', 'value': 100},
        {'letter': 'XC', 'value': 90},
        {'letter': 'L', 'value': 50},
        {'letter': 'X', 'value': 10},
        {'letter': 'IX', 'value': 9},
        {'letter': 'V', 'value': 5},
        {'letter': 'I', 'value': 1},
    ]


# In[13]:


def decimal_to_roman(number):
    remainder = number
    result = ''
    factor=0
    for numeral_index in range(len(numerals)):
        numeral = numerals[numeral_index]
        next_numeral = numerals[numeral_index + 1] if numeral_index + 1 < len(numerals) else None

        factor = remainder // numeral['value']
        remainder -= factor * numeral['value']

        if next_numeral:
            numeral_difference = numeral['value'] - next_numeral['value']
            if (remainder - numeral_difference >= 0) and (numeral_difference > next_numeral['value']):
                result += next_numeral['letter'] + numeral['letter']
                remainder -= numeral_difference

        if factor > 0:
            result += numeral['letter'] * factor
    
    return result


# You need to come up with test cases to show that your conversion works as expected. 
# NB: the conversion is ambiguous in some cases. Any valid conversion is accepted. 

# In[15]:


test_pairs = [("IX", 9), ("XI", 11), ("MCCII", 1202), ("MMXVIII", 2018), ("XLIX", 49), ("MCMLXXXIV", 1984), ("MDCCCXXVIII", 1828), ("MMMDCCCLXXXVIII", 3888)]

for rom, dec in test_pairs:
    converted = decimal_to_roman(dec)
    print(converted == rom)
    print(converted)

