#load data from txt file --> spectrum

filename = "data\EIS data\EIS_state_I_25C01.txt"

data = []

with open(filename) as file:
    lines = [line.replace('\t', '').rstrip().split(' ') for line in file]

print(lines[1])

# for line in file[1:]:

#     data.append({
#         "cycle": int(file[1]),
#         "freq_Hz": float(file[2]),
#         "Re_Z": float(file[3]),
#         "neg_Im_Z": float(file[4])
#     })

#     print(line)

# print(data)

# for file in file:
#     data.append({
#         "cycle": int(file[1]),
#         "freq_Hz": float(file[2]),
#         "Re_Z": float(file[3]),
#         "neg_Im_Z": float(file[4])
#     })

# print(data)