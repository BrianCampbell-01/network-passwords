import subprocess

# commands for windows terminal to find profiles and passwords
# index cmd[0:4] shows all profiles
# index cmd shows passwords but index cmd[4] needs user profile
cmd = ["netsh", "wlan", "show", "profiles","user_profile", "key=clear"]
#command that calls to the teminal
proc = subprocess.Popen(cmd[0:4], stdout=subprocess.PIPE)
#uses this as the string item to find the profiles
id = "All User Profile"
#output seems counter intuitice
output = []
#found profiles and passwords can be made into a dictonary
found_profiles = []
found_passwords =[]

#after the first subprocess call read the output and look for the
#profiles command. if "All User Profile" is in the sentence 
#format the sentece and store the wifi broadcast name
for line in proc.stdout.readlines():
    if id in line.decode("utf-8"):
        found_profiles.append(line.decode("utf-8")[27:-2])
    
#in the second subprocess call we call netsh with each profile 
#to see the password and store it
for item in found_profiles:
    cmd[4] = item
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in proc.stdout.readlines():
        if "Key Content" in line.decode("utf-8"):
            found_passwords.append(line.decode("utf-8")[29:-2])

#output the profiles and passwords to an output file
f= open("output.txt","a")
for index1,index2 in zip(found_profiles,found_passwords):
    f.write(f"username: {index1}      password: {index2} \n")
f.close()
    