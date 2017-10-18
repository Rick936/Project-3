logpars = open("http_access_log.log", "r")

counter = 0
for line in logpars:
    counter += 1
print ("Question 1:",counter)
    