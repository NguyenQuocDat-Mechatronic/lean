# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
"""dùng total"""
# fh = open("mbox.txt")
# total = 0
# i = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#         # print(i)
#     else:
#        line = line.strip()
#        # print(line)
#        # line = line.split(":",1)
#        ipos = line.find(":")
#        # print(line)
#        line = line[ipos+1:]
#        print(line)
#        total += float(line)
#
#        i += 1
#        # print(i)
# print(total,i)
# avg = total/i
# print("Average spam confidence:",avg)


# # print(lst)
# total =0
# for i in lst:
#     total += float(i)
# avg = total/len(lst)

"""dung sum/ len"""
fh = open("mbox.txt")
total = 0
lst =[]
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        print(i)
    else:
       line = line.strip()
       # print(line)
       # line = line.split(":",1)
       ipos = line.find(":")
       # print(line)
       line = line[ipos+1:]
       # print(line)
       line = float(line)
       lst.append(line)
# avg = total/i
# print(lst)

print("Average spam confidence:",sum(lst)/len(lst))
# avg = total/len(lst)
# print(,avg)

# fh = open("mbox.txt")
# lst =[]
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     else:
#        line = line.strip()
#        # print(line)
#        # line = line.split(":",1)
#
#        # print(line)
#        line = line[-6:]
#        # print(line)
#        lst.append(line)
#
# # print(lst)
# total =0
# for i in lst:
#     total +=float(i)
# avg = total/len(lst)
# print("Average spam confidence:",avg)