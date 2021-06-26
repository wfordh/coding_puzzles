# id, name, health_pkg, num_dep
data = [
'1, John Doe, 2271, 0',
'2, Billy Joel, 11782, 2',
'3, Johnson, Alicia, 5555, 1',
'4, Sam Smoltz, 32118, 2',
'5, Ricky Jones, 23981']

def main():
	clean_data = list()
	for row in data:
		clean_row = list()
		row = row.split(", ")
		if len(row) == 4:
			# basically assuming only one of the two errors happens
			# and so length of 4 means correct	
			clean_data.append(row)
		else:
			cnt = 0
			while row:
				current = row.pop(0)
				cnt += 1	
				if cnt == 1:
					clean_row.append(current)
				elif cnt == 2:
					if len(current.split())==2:
						clean_row.append(current)
					else:
						nxt = row.pop(0)
						cnt += 1
						clean_row.append(nxt + " " + current)
				elif cnt in (3, 4):
					try:
						elem = int(current)
						clean_row.append(current)
					except:
						pass
			if len(clean_row) != 4:
				clean_row.append("0")
			clean_data.append(clean_row)
	print(clean_data)

if __name__ == "__main__":
	main()
