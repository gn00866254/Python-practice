birthday = ["19930911", "20010621", "19801110", "19980507", "20100101"]

#スライスで年だけを切り取る
print("Year List:",[ i[:4]+"年" for i in birthday])
#スライスで月だけを切り取る
print("Month List:",[ i[4:6]+"月" for i in birthday])
#スライスで日だけを切り取る
print("Day List:",[ i[6:]+"日" for i in birthday])