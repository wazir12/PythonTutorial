dynamic_string = "Cisco Model : %s, %d WANSlots,IOS:%f " %("2600XM",2,12.4)
dynamic_string2 = "Cisco Model : %s, %d WANSlots,IOS:%.1f " %("2600XM",2,12.4222)
dynamic_string3 = "Cisco Model : %s, %d WANSlots,IOS:%.2f " %("2600XM",2,12.653)
dynamic_string4 = "Cisco Model : %s, %d WANSlots,IOS:%.f " %("2600XM",2,12.4)

print("dynamic_string_1: %s" %(dynamic_string));
print("dynamic_string_2: %s" %(dynamic_string2));
print("dynamic_string_3: %s" %(dynamic_string3));
print("dynamic_string_4: %s" %(dynamic_string4));

x = "Cisco"
y="Switch"

print("x+y= %s" % (x+y))
print("x*3= %s" % (x * 3))
print("b not in x= %s" %("b" not in x))
print("b in x= %s" %("b" in x))
print("C in x= %s" %("C" in x))
print("Entering '_' in between each element of x= %s " %("_".join(x)))
print("counting utterance of a element in String: %s " %(x.count("c")))

dynamic_string_with_format_method = "Cisco Model : {}, {} WANSlots,IOS:{} ".format("2600XM",2,12.4)

print("dynamic_string_with_format_method: %s" %(dynamic_string_with_format_method));
dynamic_string_with_format_method_with_index = "Cisco Model : {1}, {0} WANSlots,IOS:{2} ".format("2600XM",2,12.4)
print("dynamic_string_with_format_method_with_index: %s" %(dynamic_string_with_format_method_with_index));

print("F Strings in Python for String formatting: ")
model = "2600XM"
WANSlots = 2
IOS = 12.4
f_string = f"Cisco Model: {model}, WANSlots: {WANSlots}, IOS: {IOS}"
print(f"F-String= {f_string}")
s = "Hello"
print("reverse the string %s = %s"%(s,s[::-1]))
print("print string = %s by skipping 2 elements = %s" %(s,s[::2]))
