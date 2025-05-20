'''
Problem 1:
Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

Below is my solution:
''''


st = 'Print only the words that start with s in this sentence'

w =[item for item in st.split() if item[0] == 's' or item[0] == 'S']

print(w)