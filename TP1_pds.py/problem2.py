total_second = 18933
hour = total_second//3600
hour_rest= total_second%3600
minute = hour_rest//60
minute_rest=hour_rest%60
print(total_second , "second =" , hour , "h " , minute , "mn " , minute_rest , "s")

 # check true or flase
print("check :" ,hour*3600 + minute *60 + minute_rest == total_second)