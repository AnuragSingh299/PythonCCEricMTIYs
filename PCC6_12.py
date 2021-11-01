departments = {
	'information technology': {
		'sem': 5,
		'total_students': 50,
		'university': 'GTU',
	},

	'Computer science': {
		'sem': 3,
		'total_students': 60,
		'university': 'parul university',
	},
}

for department, dept_info in departments.items():
	print(f"{dept_info['total_students']} students from {dept_info['sem']} semester of {department} department {dept_info['university']} were selected for the competetion.")
