# two Strings are input name 1- needle 2-haystack
# We have to check first occurence of needle in haystack
haystack = "sadbutsad"
needle = "sad"

#First step check the lenght of needle String make a window of len(needle) in haystack 
#Second step just iterate in haystack of window lenght 
#Third Step move to next window if not found

window=len(needle)
def CheckOccurence(haystack,needle):

    for i in range(len(haystack)-len(needle)+1 ) :
    # i value increase and window is moved forward
        if haystack[i:i+window] == needle:
            return i

    return -1

CheckOccurence(haystack,needle)


# Time Complexity - BigO(n * m)
# Space Complexity - BigO(1)
    