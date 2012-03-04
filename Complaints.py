'''
The people at TopCoder invited a bunch of members to a recognition party. At the party, they arranged all of the people in a line ordered by rating. Unfortunately, they may have made mistakes. Each member will file a complaint for every person ahead of them that has a lower rating. For example: line = {1000,800,900,1400} The line is ordered front to back. The member rated 900 (position 2 in the line) will file 1 complaint since there is a member rated 800 (position 1) ahead of him. The member rated 1400 (position 3) will file 3 complaints since there are members rated 1000 (position 0), 800 (position 1), and 900 (position 2) ahead of him. In total there will be 4 (1+3) complaints. Given the list of ratings ordered front to back, you will determine how many complaints TopCoder will receive. Create a class Complaints that contains the method howMany, which takes an int[] line and returns an int that represents the number of complaints TopCoder will receive.

Complaints
Method:
howMany
Parameters:
int[]
Returns:
int
Method signature:
int howMany(int[] line)
-
line must contain between 1 and 50 elements inclusive
-
Each element of line must be between 0 and 4000 inclusive
Examples
0)

{1000,800,900,1400}
Returns: 4
Same as above
1)

{1,2,3,4,5}
Returns: 10
5 - 4 people ahead have lower ratings 4 - 3 people ahead have lower ratings 3 - 2 people ahead have lower ratings 2 - 1 person ahead has a lower rating 4+3+2+1 = 10
2)

{10,9,8,7,6,5}
Returns: 0
Everyone is in order
3)

{0,0,0,0,4000,4000,4000,4000}
Returns: 16
Each 4000 has four 0's ahead of them that have lower ratings: 4+4+4+4 = 16
4)

{1000,0,4000,2000}
Returns: 4

5)

{0}
Returns: 0
'''
class Complaints():
	def howMany(self, values):
		totalComplaints = 0
		for i in range(len(values)):
			currentComplaints = 0
			for j in range(i):
				if values[j] < values[i]: 
					totalComplaints+=1
		return totalComplaints 

def main():
	complaints = Complaints()
	print complaints.howMany([1000, 800, 900, 1400])
	print complaints.howMany([1, 2, 3, 4, 5])
	print complaints.howMany([10, 9, 8, 7, 6, 5])
	print complaints.howMany([0,0,0,0,4000,4000,4000,4000])
	print complaints.howMany([1000,0,4000,2000])
	print complaints.howMany([0])

if __name__ == '__main__':
	main()
