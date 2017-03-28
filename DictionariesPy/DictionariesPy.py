#Dictionaries Key-value pairs

var={'akarsh':507,'harun':504,'arun':'5g9'}
print var

#other way of creating dictionary

var1=dict();
var1['akarsh']=507;
var1['harun']=504
print var1['akarsh'];
#get method
if var1.get('akars')==None:
    print "No"
#get with default value
if var1.get('akars',0)==0: #get() returns zero as we have mentioned default val as 0
    print "Not present"

var2=dict();
var2[1]=507
var2[2]=504
# printing all values using For loop

for key in var2:
    print key,":",var2[key]

#other way of printing
for keys,valuee in var2.items(): #which creates tuple i.e comma seperated key value pairs
    print keys,valuee

#converint dict to list
print "all keys in dict: ",list(var2)
#   or
print "all keys in dict",var2.keys()

print "all values in dict",var2.values();

#converting to tuples
print "Tuple: ",var2.items();

