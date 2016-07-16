## String split

# Implement the string split function: split(string, delimiter).

# Examples:

# split('abc,defg,hijk', ',') => ['abc', 'defg', 'hijk']
# split('JavaScript', 'a') => ['J', 'v', 'Script']
# split('JaaScript', 'a') => ['J', '', 'Script']
# split('JaaaScript', 'aa') => ['J', 'aScript']

def str_split(str, delim):
    result = []
    start_idx = 0
    end_idx = str.index(delim)
    while end_idx != -1:
        # find to the end_idx (until delim)
        part = str[:end_idx]
        # append to array
        result.append(part)
        # set start index to next point after delim
        start_idx = end_idx + len(delim)
        # now string is cut from start_idx to leave remainder so you can find next delim
        str = str[start_idx:]
        # if there is no delim in the rest of string
        if delim not in str:
            # put remaining str in array
            result.append(str)
            # terminate loop
            break
        # end_idx is now delim in leftover string
        end_idx = str.index(delim)
    print result

## test before adding input functionality
# str_split('abc,defg,hijk', ',')
# str_split('JavaScript', 'a')
# str_split('JaaScript', 'a')
# str_split('JaaaScript', 'aa')

print "Give string and a delimiter to split the string on."
str = raw_input("Enter a string: ")
delim = raw_input("Enter a delim: ")
str_split(str, delim)
